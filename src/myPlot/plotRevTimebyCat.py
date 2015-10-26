#!/usr/bin/env python
import logging
import numpy as np
# Pandas DataManagement
import pandas as pd

# Plotly Graphing
import plotly.plotly as py
import plotly.tools as tls
# Plotting template file
#

# Please give the filename of this plotting fuction a descriptive name
# Also when you have created a plotting function add it to the __init__
# list so it is included in the package.
# More info here:
# https://docs.python.org/2/tutorial/modules.html#importing-from-a-package
#

def plot(rawData):
    logging.info("Creating product Revenue over Time per Category Plot")

    # ----------------
    # - LOAD IN DATA - 
    # ----------------
    logging.info("Loading in data...")
 
    # Use rawData to load in data required.
    # example: rawData.loadOrder
    rawData.loadOrder()
    rawData.loadCustomer()
    rawData.loadProduct()
    
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
    
    # From the Table presumable created above, remove excess columns. Also
    # re-index a table to new column
    #
    grouped = customerOrderDescr.loc[:,['ORDER_DATE','PRODUCT_CATEGORY',
            'TOTAL_LINE_AMT']]
    
    # Group Orders by their date
    #
    grouped = grouped.groupby(['ORDER_DATE', 'PRODUCT_CATEGORY']).sum()
    
    # Remove first index since only a few entries
    #
    grouped = grouped.ix[3:] 
    logging.debug(grouped)
    
    # Pivot the categories to become column names
    #
    df = grouped.unstack(level=-1)

    # Clean up unstacked table
    #
    df.columns = df.columns.get_level_values('PRODUCT_CATEGORY')
    
    # Delete non-applicable columns
    df = df.drop(['PUBLIC RELATION','App/Accss Event','IQVC Divisional',\
            'License Hardgds','PUBLIC RELATION','Returns'],
            axis=1)

    logging.debug(df)

    # Finish Organizing in data
    #        
    logging.info("Done querying data")
    
    # -------------
    # - PLOT DATA - 
    # -------------
    logging.info("Plotting...")
    
    fig = tls.make_subplots(rows=len(df.columns), cols=1, shared_xaxes=True)
    fig['layout'].update(height=2000,width=1600, title='Product Revenue ' +
            'over Time (Seperated by Product Category)')

    i = 1
    
    for col in df.columns:
         fig.append_trace({'x': df.index, 'y': df[col], 'name': col}, i, 1)
         i = i + 1
    
    py.plot(fig, fill=True, filename='templeAnalytics2015/RevTimebyCat')

    #py.plot([{
    #    'x': df.index,
    #    'y': df[col],
    #    'name': col
    #} for col in df.columns], \
    #        shape=(19,1), subplots=True, shared_xaxes=True, fill=True, \
    #        filename='templeAnalytics2015/RevTimebyCat')
    
    # Finish Plotting in data
    #   
    logging.info("Done plotting product Revenue per Category over time")

