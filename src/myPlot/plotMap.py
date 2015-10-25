#!/usr/bin/env python
import logging
import numpy as np
# Pandas DataManagement
import pandas as pd

# Plotly Graphing
import plotly.plotly as py
import cufflinks as cf

# Plotting template file
#

# Please give the filename of this plotting fuction a descriptive name
# Also when you have created a plotting function add it to the __init__
# list so it is included in the package.
# More info here:
# https://docs.python.org/2/tutorial/modules.html#importing-from-a-package
#

def plot(rawData):
    logging.info("Creating Map...")

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
    # Use logging.debug(obj.DataFrame) to print contents of the resulting 
    # table
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
    grouped = customerOrderDescr.loc[:,['STATE', \
            'PRODUCT_CATEGORY', 'TOTAL_LINE_AMT']]
    grouped = grouped.groupby(['STATE', 'PRODUCT_CATEGORY']).sum()
    
    # Pivot the categories to become column names
    #
    df = grouped.unstack(level=-1)
    
    # Clean up unstacked table
    #
    df.columns = df.columns.get_level_values('PRODUCT_CATEGORY')
    logging.debug(df) 
    
    # Sum across the row and store in new column
    #
    stateTotRev = pd.DataFrame()
    stateTotRev['STATE_REV'] = df.sum(axis=1)
    logging.debug(stateTotRev)

    #for category in pd.unique(grouped.PRODUCT_CATEGORY.ravel()):
    #    df[category] = grouped.xs(category, level='PRODUCT_CATEGORY')
    #
    
    # Finish Organizing in data
    #        
    logging.info("Done querying data")

    # -------------
    # - PLOT DATA - 
    # -------------
    logging.info("Plotting...")

    scl = [[0.0, 'rgb(242,240,247)'],
            [0.2, 'rgb(218,218,235)'],
            [0.4, 'rgb(188,189,220)'],
            [0.6, 'rgb(158,154,200)'],
            [0.8, 'rgb(117,107,177)'],
            [1.0, 'rgb(84,39,143)']]

    df['text'] = 'Accessories: $' + df['Accessories'].astype(str) + '<br>' +  \
            'Apparel: $' + df['Apparel'].astype(str) + '<br>' + \
            'Collectibles: $' + df['Collectibles'].astype(str) +  '<br>' + \
            'Costume Jewelry: $' + df['Costume Jewelry'].astype(str) + '<br>' + \
            'Electronics: $' + df['Electronics'].astype(str) + '<br>' + \
            'Fun & Leisure: $' + df['Fun & Leisure'].astype(str) + '<br>' + \
            'Gift Cards: $' + df['Gift Cards'].astype(str)  + '<br>' + \
            'Health: $' + df['Health'].astype(str)  + '<br>' + \
            'Health/Beauty: $' + df['Health/Beauty'].astype(str)  + '<br>' + \
            'Home Decor: $' + df['Home Decor'].astype(str)  + '<br>' + \
            'Housewares: $' + df['Housewares'].astype(str)  + '<br>' + \
            'Jewelry: $' + df['Jewelry'].astype(str)  + '<br>' + \
            'Textile/Furni: $'+ df['Textile/Furnit'].astype(str) 
    
    data = [ dict(
            type='choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = stateTotRev.index.values,
            z = stateTotRev['STATE_REV'].astype(int),
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 2
                )
            ),
            colorbar = dict(
                title = "Revenue USD ($)"
            )
    ) ]

    layout = dict(
        title = 'QVC Revenue per State (Hover for Category Breakdown)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)',
        ),
    )
                        
    fig = dict( data=data, layout=layout )

    url = py.plot( fig, filename='templeAnalytics2015/Sales_Map' )
    
    # Finish Plotting in data
    #   
    logging.info("Done plotting map.")

