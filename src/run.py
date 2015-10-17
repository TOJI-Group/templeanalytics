import sys
import os
import operator
import argparse
import logging
import collections
import numpy as np
# Pandas DataManagement
import pandas as pd
# Plotly Graphing
import plotly.plotly as py
import plotly.graph_objs as go


def main(argv):

    # ------------------------------
    # - PARSE COMMAND LINE / INPUT - 
    # ------------------------------
    
    parser = argparse.ArgumentParser(
        description='Temple Analytics 2015 Analyze Code. [TEAM TOJI]')
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
    args = parser.parse_args()
    if args.verbosity >= 4:
        print("Verbosity Level 4 Turned On")
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbosity == 3:
        print("Verbosity Level 3 Turned On")
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbosity == 2:
        print("Verbosity Level 2 Turned On")
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbosity == 1:
        print("Verbosity Level 1 Turned On")
        logging.basicConfig(level=logging.INFO)
    
    # Catch Directory path for data by using the current working directory
    #
    DataPath = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "data")
    
    # Make data filepaths
    #
    customer_filename = os.path.join(DataPath, "qvc", "customer_master.csv")
    order_filename = os.path.join(DataPath,"qvc", "order_master.csv")
    product_filename = os.path.join(DataPath,"qvc", "product_master.csv")
    airtime_filename = os.path.join(DataPath,"qvc", "product_airtime.csv")
    email_filename = os.path.join(DataPath,"qvc", "email_campaign.csv")
    social_filename = os.path.join(DataPath,"qvc", "social.csv")
    zipToFips_filename = os.path.join(DataPath, "misc", "COUNTY_ZIP_062015.csv")
    fipsToCounty_filename = os.path.join(DataPath, "misc", "countyid_fips.csv")
    
    filenames = [customer_filename, order_filename, product_filename, 
            airtime_filename, email_filename, social_filename]
    
    # ----------------
    # - LOAD IN DATA - 
    # ----------------
    logging.info("Loading in data...")
    
    # Open datafile. We also skip first item in the csv file since it will
    # display the header
    #
    logging.info("Opening File: %s", customer_filename)
    customerList = pd.read_csv(customer_filename, index_col='CUSTOMER_NBR')
    logging.debug(customerList)
    
    # Close file
    #
    logging.info("Closing File: %s", customer_filename)

    # Repeat read in data for orders.
    #
    logging.info("Opening File: %s", order_filename)
    orderList = pd.read_csv(order_filename, index_col='ORDER_NBR',
            parse_dates = True)
    logging.debug(orderList)

    # Close file
    #
    logging.info("Closing File: %s", order_filename)

    # Repeat read in data for Product Listing.
    #
    logging.info("Opening File: %s", product_filename)
    productDescr = pd.read_csv(product_filename)
    logging.debug(productDescr)
  
    # Close file
    #
    logging.info("Closing File: %s", product_filename)
    
    # Repeat read in data for Airtime.
    #
    logging.info("Opening File: %s", airtime_filename)
    mediaList = pd.read_csv(airtime_filename, parse_dates=True)
    logging.debug(mediaList)
  
    # Close file
    #
    logging.info("Closing File: %s", airtime_filename)
    
    # Finish Loading in data
    #
    logging.info("Done loading data")
   
    # -------------------
    # - REORGANIZE DATA - 
    # -------------------
    logging.info("Reorganizing data...")
    
    # Create a master list via the order number
    #
    
    # Combine Order Number and Customer Number
    #
    customerOrder = pd.merge(orderList, customerList, left_on='CUSTOMER_NBR', 
             right_index=True, sort=False);
    
    logging.debug(customerOrder)
    
    # Combine Orders and Product Categories
    #
    customerOrderDescr = pd.merge(customerOrder, productDescr,
             on='PRODUCT_NBR', sort=False);
    
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
    customSub = customerOrderDescr.loc[:,['PRODUCT_CATEGORY', 'TOTAL_LINE_AMT']]
            
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
    logging.info("Plotting data...")
        
    # Define Figure
    #
    customSub.iplot(kind='bar', filename='templeAnalytics2015/Revenue_vs_Product_Category')
    
    # Finish Plotting in data
    #   
    logging.info("Done plotting data")
    
    # Exit Gracefully
    #
    print("Program Finished successfully.")
    
        
# Run main if tihs is ran as main function. 
if __name__ == "__main__":
    main(sys.argv)