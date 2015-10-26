#!/usr/bin/env python
import logging

# Pandas DataManagement
import pandas as pd

# Plotly Graphing
import plotly.plotly as py

# Plotting template file
#

# Please give the filename of this plotting fuction a descriptive name
# Also when you have created a plotting function add it to the __init__
# list so it is included in the package.
# More info here:
# https://docs.python.org/2/tutorial/modules.html#importing-from-a-package
#

def plot(rawData):
    logging.info("Creating Pi Chart Sales in Each Category")

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

    # --------------
    # - QUERY DATA - 
    # --------------
    logging.info("Querying data...")
    
    # From the Table presumable created above, remove excess columns. Also
    # re-index a table to new column
    #
    platformCounts = rawData.orderList['ORDER_PLATFORM'].value_counts()
    Onlinecount = platformCounts['QVC.COM']    
    OnAircount = platformCounts['On Air'] + \
            platformCounts['On Air - 2nd Channel']
    Magazinecount = platformCounts['QVC INSIDER MAGAZINE']
    Othercount = platformCounts['QVC Voices'] + \
            platformCounts['Streaming video']

    # Finish Organizing in data
    # 
    logging.info("Done querying data")
    
    # -------------
    # - PLOT DATA - 
    # -------------
    logging.info("Plotting...")
   
    fig = {
        'data': [{'labels': ['Online', 'QVC Magazine', 'On Air', 'Other'],
        'values': [Onlinecount, Magazinecount, OnAircount, Othercount],
        'type': 'pie'}],
        'layout': {'title': 'Percentage of Total Sales from Each Domain'}
    }
    url = py.plot(fig, filename='templeAnalytics2015/Total_Sales_Breakdown')

    # Finish Plotting in data
    #   
    logging.info("Done plotting Pi Chart")

