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
    rawData.loadMaster()

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
    grouped = rawData.masterList.loc[:,['STATE', \
            'PRODUCT_CATEGORY', 'TOTAL_LINE_AMT']]
    grouped = grouped.groupby(['STATE', 'PRODUCT_CATEGORY']).sum()
    
    # Round data
    #
    grouped['TOTAL_LINE_AMT'] = (np.round(grouped['TOTAL_LINE_AMT'],-2) \
            / 1000000)
    
    # Convert NAN values to zero
    #
    grouped.fillna(0)
    
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
   
    df['text'] = 'Accessories: $' + \
            df['Accessories'].astype(str) + 'M <br>' +  \
            'Apparel: $' + \
            df['Apparel'].astype(str) + 'M <br>' + \
            'Collectibles: $' + \
            df['Collectibles'].astype(str) + 'M <br>' + \
            'Costume Jewelry: $' + \
            df['Costume Jewelry'].astype(str) + 'M <br>' + \
            'Electronics: $' + \
            df['Electronics'].astype(str) + 'M <br>' + \
            'Fun & Leisure: $' + \
            df['Fun & Leisure'].astype(str) + 'M <br>' + \
            'Gift Cards: $' + \
            df['Gift Cards'].astype(str)  + 'M <br>' + \
            'Health: $' + \
            df['Health'].astype(str)  + 'M <br>' + \
            'Health/Beauty: $' + \
            df['Health/Beauty'].astype(str)  + 'M <br>' + \
            'Home Decor: $' + \
            df['Home Decor'].astype(str)  + 'M <br>' + \
            'Housewares: $' + \
            df['Housewares'].astype(str)  + 'M <br>' + \
            'Jewelry: $' + \
            df['Jewelry'].astype(str)  + 'M <br>' + \
            'Textile/Furni: $'+ \
            df['Textile/Furnit'].astype(str) + 'M' 
    
    data = [ dict(
            type='choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = stateTotRev.index.values,
            z = (1000000*stateTotRev['STATE_REV']).astype(int),
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
                        
    fig = dict(data=data, layout=layout)

    url = py.plot( fig, filename='templeAnalytics2015/Sales_Map' )
    
    # Finish Plotting in data
    #   
    logging.info("Done plotting map.")

