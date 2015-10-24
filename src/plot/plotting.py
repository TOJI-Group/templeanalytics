

def plotRevenueCategory(rawData):
    logging.info("Creating product Revenue vs Product Category Plot")

    # ----------------
    # - LOAD IN DATA - 
    # ----------------
    logging.info("Loading in data...")
 
    # For this plot we need customer, order, and product category data
    #
    rawData.loadCustomer()
    rawData.loadOrder()
    rawData.loadProduct()

    # Finish Loading in data
    #
    logging.info("Done loading data")

    # -------------------
    # - REORGANIZE DATA - 
    # -------------------
    logging.info("Reorganizing data...")
    
    # Combine Order Number and Customer Number
    #
    customerOrder = pd.merge(rawData.orderList, rawData.customerList, 
            left_on='CUSTOMER_NBR', right_index=True, sort=False)
    
    logging.debug(customerOrder)
    
    # Combine Orders and Product Categories
    #
    customerOrderDescr = pd.merge(customerOrder, rawData.productDescr,
             on='PRODUCT_NBR', sort=False)
    
    logging.debug(customerOrderDescr)

    # Finish Organizing in data
    #
    logging.info("Done reorganizing data")
    
    # --------------
    # - QUERY DATA - 
    # --------------
    logging.info("Querying data...")
    
    # Create a sub-set of the data
    #
    customSub = customerOrderDescr.loc[:,
            ['PRODUCT_CATEGORY', 'TOTAL_LINE_AMT']]

    # Create Multi-Index Dataset
    #
    customSub = customSub.groupby('PRODUCT_CATEGORY').sum()
    logging.debug(customSub)
    
    # Finish Organizing in data
    #        
    logging.info("Done querying data")
    
    # -------------
    # - PLOT DATA - 
    # -------------
    logging.info("Plotting...")
     
    # Figure Attributes
    #
    cf.set_config_file(offline=False, world_readable=True, theme='ggplot')
    
    # Plot figure
    #
    customSub.iplot(kind='bar', 
            filename='templeAnalytics2015/Revenue_vs_Product_Category')
    
    # Finish Plotting in data
    #   
    logging.info("Done plotting product Revenue vs Product Category Plot")


def plotEmailSpendCategory(rawData):
    # Plotting template
    logging.info("Creating Email Spenditure vs Product Category Plot")

    # ----------------
    # - LOAD IN DATA - 
    # ----------------
    logging.info("Loading in data...")
 
    # Use rawData to load in data required.
    # example: rawData.loadOrder
    #
    rawData.loadEmail()

    # Finish Loading in data
    #
    logging.info("Done loading data")

    # -------------------
    # - REORGANIZE DATA - 
    # -------------------
    logging.info("Reorganizing data...")
    
    # Combine Necessary Tables 
    # Use logging.debug(obj.DataFrame) to print contents of the resulting table
    #

    # Finish Organizing in data
    #
    logging.info("Done reorganizing data")
    
    # --------------
    # - QUERY DATA - 
    # --------------
    logging.info("Querying data...")
    
    # From the Table presumable created above, remove excess columns. Also
    # re-index a table to new column
    #
    totalCATsales = rawData.emailCamp.groupby('PRODUCT_CATEGORY').aggregate(sum)
    totalCATsalesedit = totalCATsales.drop('All')

    # Finish Organizing in data
    #        
    logging.info("Done querying data")
    
    # -------------
    # - PLOT DATA - 
    # -------------
    logging.info("Plotting...")
    

    cf.set_config_file(world_readable=True, theme='ggplot')
    totalCATsalesedit.iplot(kind='bar', 
            filename="templeAnalytics2015/" \
            "Email_Campaign_Spend_vs_Product_Category", 
            title="Email Campaign Cost per Product Category")

    # Finish Plotting in data
    #   
    logging.info("Done plotting product Revenue vs Product Category Plot")


