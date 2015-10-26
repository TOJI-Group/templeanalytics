#!/usr/bin/env python
import sys
import operator
import argparse
import logging
import collections
import numpy as np
# Data Class 
from classes.rawFileOp import rawFileOp
# Plotting Functions
from myPlot import *

# Pandas DataManagement
import pandas as pd

def main(argv):

    # ------------------------------
    # - PARSE COMMAND LINE / INPUT - 
    # ------------------------------
    
    parser = argparse.ArgumentParser(
        description='Temple Analytics 2015 Analyze Code. [TEAM TOJI]')
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
    args = parser.parse_args()
    if args.verbosity >= 2:
        print("Verbosity Level 2 Turned On")
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbosity == 1:
        print("Verbosity Level 1 Turned On")
        logging.basicConfig(level=logging.INFO)
    
    # Call function to read in csv files
    #
    rawData = rawFileOp();

    # rawFileOp class loads in the raw csv files.
    # Functions to loading in different data:
    #    - loadCustomer = customer_master.csv
    #    - loadOrder    = order_master.csv
    #    - loadProduct  = product_master.csv
    #    - loadAirtime  = product_airtime.csv
    #    - loadEmail    = email_campaign.csv
    #    - loadSocial   = social.csv
    # Running any of the above functions load data into the following global
    # variables.
    # Variables containing importated data:
    #    - cusomerList  = customer_master.csv
    #    - orderList    = order_master.csv
    #    - productDescr = product_master.csv
    #    - mediaList    = product_airtime.csv
    #    - emailCamp    = email_campaign.csv
    #    - socialList   = social.csv
    
    # From module plot, plot the desired plots
    # Create plot of revenue vs product category
    #
    #plotRevenueCategory.plot(rawData)

    # Create plot of email campaing spenditure vs product category
    #
    #plotEmailSpendCategory.plot(rawData)
    
    # Create pi chart of sales per category
    #
    #plotSalesCategory.plot(rawData)

    # Plot the map
    #
    #plotMap.plot(rawData)

    # Plot Social Media Sentiment
    #
    #plotSentiment.plot(rawData)

    # Plot Product Sales over time
    #
    #plotProductSalesTime.plot(rawData)
    
    plotRevTimebyCat.plot(rawData)
    # Exit Gracefully
    #
    print("Program Finished successfully.")
    
        
# Run main if tihs is ran as main function. 
if __name__ == "__main__":
    main(sys.argv)
