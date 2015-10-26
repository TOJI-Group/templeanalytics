#!/usr/bin/env python
import logging

# Pandas DataManagement
import pandas as pd

# Plotly Graphing
import plotly.plotly as py
import plotly.graph_objs as go

def plot(rawData):
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
    totalCATsales = rawData.emailCamp.groupby('PRODUCT_CATEGORY').sum()
    df = totalCATsales.drop('All')
    
    logging.debug(df)
    # Finish Organizing in data
    #        
    logging.info("Done querying data")
    
    # -------------
    # - PLOT DATA - 
    # -------------
    logging.info("Plotting...")
    
    # Plot Layout
    #
    layout = go.Layout(
            title='Revenue per Product Category',
            yaxis=dict(
                title='Revenue (USD $)'
            )
    )
    
    # Define the figure using playout and data. Plot After
    #
    data = [
            go.Bar(
                x=df.index,
                y=df['CAMPAIGN_SPEND']
            )
    ]
    
    fig = go.Figure(data=data,layout=layout)
    url = py.plot(fig,
            filename='templeAnalytics2015/' +
            'Email_Campaign_Spend_vs_Product_Category') 
     
    # Finish Plotting in data
    #   
    logging.info("Done plotting Email Campaign vs Product Category Plot")

   
 
