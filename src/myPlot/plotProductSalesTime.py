#!/usr/bin/env python
import logging
import numpy as np
# Pandas DataManagement
import pandas as pd

# Plotly Graphing
import plotly.plotly as py
import cufflinks as cf
import plotly.graph_objs as go
# Plotting template file
#

# Please give the filename of this plotting fuction a descriptive name
# Also when you have created a plotting function add it to the __init__
# list so it is included in the package.
# More info here:
# https://docs.python.org/2/tutorial/modules.html#importing-from-a-package
#

def plot(rawData):
    logging.info("Creating product Revenue vs Product Category Plot")

    # ----------------
    # - LOAD IN DATA - 
    # ----------------
    logging.info("Loading in data...")
 
    # Use rawData to load in data required.
    # example: rawData.loadOrder
    rawData.loadOrder()
    
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
    timeSales = rawData.orderList[['ORDER_DATE','TOTAL_LINE_AMT']]
    logging.debug(timeSales)
    
    #    grp = timeSales.groupby('ORDER_DATE')
    #    logging.debug(grp)
    
    # Group Orders by their date
    #
    sumTimeSales = timeSales.groupby('ORDER_DATE',
            as_index=False).aggregate(sum)
    
    # Round the toal Sales by Order Date
    #
    sumTimeSales['TOTAL_LINE_AMT'] =  np.round(
            sumTimeSales['TOTAL_LINE_AMT'], -2)
    logging.debug(sumTimeSales)
   
    # Finish Organizing in data
    #        
    logging.info("Done querying data")
    
    # -------------
    # - PLOT DATA - 
    # -------------
    logging.info("Plotting...")
    
    trace = go.Scatter(x = sumTimeSales['ORDER_DATE'], 
            y = sumTimeSales['TOTAL_LINE_AMT'])
    data = [trace]
    
    url = py.plot(data, filename = 'templeAnalytics2015/Revenue_over_Time')
    
    # Finish Plotting in data
    #   
    logging.info("Done plotting product Revenue over time")

