#!/usr/bin/env python
import logging

# Pandas DataManagement
import pandas as pd

# Plotly Graphing
import plotly.plotly as py
import plotly.graph_objs as go

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
    rawData.loadSocial()
    
    # Finish Loading in data
    #
    logging.info("Done loading data")

    # -------------------
    # - REORGANIZE DATA - 
    # -------------------
    logging.info("Reorganizing data...")
   
    # Finish Organizing in data
    #
    logging.info("Done reorganizing data")
    
    # --------------
    # - QUERY DATA - 
    # --------------
    logging.info("Querying data...")
   
    # Group by common Sentiment
    #
    sentimentCol = rawData.socialList.groupby('SENTIMENT').size()
    logging.debug(sentimentCol)
     
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
            title='Customer Feedback via Social Media',
            yaxis=dict(
                title='Number of Comments'
            )
    )
    
    # Define the figure using playout and data. Plot After
    #
    data = [
            go.Bar(
                x=sentimentCol.index,
                y=sentimentCol.values
            )
    ]
    
    fig = go.Figure(data=data,layout=layout)
    url = py.plot(fig, 
            filename='templeAnalytics2015/Sentiment_vs_Product_Category')    
     
    # Finish Plotting in data
    #   
    logging.info("Done plotting product Revenue vs Product Category Plot")
