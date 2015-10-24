#!/usr/bin/env python
import logging

# Pandas DataManagement
import pandas as pd

# Plotly Graphing
import plotly.plotly as py
import cufflinks as cf

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

   
 
