#!/usr/bin/env python
import sys
import operator
import logging
import numpy as np

# Data Class 
from classes.rawFileOp import rawFileOp

# Pandas DataManagement
import pandas as pd

def printBestSeller(rawData):
    logging.info("Finding best selling item")

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
    
    # Create a sub-set of the data containing only product descr
    # and Total Line Amount
    #
    bestSellerRev = rawData.masterList.loc[:,['PRODUCT_DESCRIPTION', 
        'TOTAL_LINE_AMT']]

    # Find the total revenue for every product
    #
    bestSellerRev = bestSellerRev.groupby(['PRODUCT_DESCRIPTION']).sum().sort(
            'TOTAL_LINE_AMT', ascending=0)
    
    # Find percentage of total revenue
    #
    bestSellerRev['Percent of Total Rev'] = 100 * \
            bestSellerRev['TOTAL_LINE_AMT']/\
            bestSellerRev['TOTAL_LINE_AMT'].sum()

    # Create a sub-set of the data containing only product Description
    # repeated for each order number
    #
    bestSellerFreq = rawData.masterList.loc[:,'PRODUCT_DESCRIPTION']
    
    # Count the total number of time each product description repeats itself.
    # Since Value
    bestSellerFreq = bestSellerFreq.value_counts().to_frame()
    
    # Set proper column names
    #
    bestSellerFreq.index.name = 'PRODUCT_DESCRIPTION'
    bestSellerFreq.columns = ['Freq']
    
    # Find percetnage of total Frequency
    #
    bestSellerFreq['Percent of Total Freq'] = 100 * \
            bestSellerFreq['Freq']/ \
            bestSellerFreq['Freq'].sum()
    

    # Merge Best Seller Lists
    #
    bestSeller = pd.merge(bestSellerRev, bestSellerFreq,\
        left_index=True, right_index=True, sort=False)

    # Finish Organizing in data
    #        
    logging.info("Done querying data")
    
    # Print Top 10 Best Sellers (Rev/Count)
    #
    print("Top 10 Items by Revenue:")
    print(bestSeller.sort('TOTAL_LINE_AMT', ascending=0).head(10))
    print("\n\nTop 10 Itmes by Sold Amount:")
    print(bestSeller.sort('Freq', ascending=0).head(10))

    logging.info("Done finding best selling itme")

def printHostStats(rawData):
    logging.info("Finding best host sellers")

    # ----------------
    # - LOAD IN DATA - 
    # ----------------
    logging.info("Loading in data...")
 
    # Use rawData to load in data required.
    # example: rawData.loadOrder
    rawData.loadOrder()
    rawData.loadAirtime()

    # Finish Loading in data
    #
    logging.info("Done loading data")
   
    # --------------
    # - QUERY DATA - 
    # --------------
    logging.info("Querying data...")
   
    # Keep orders placed via On Air Only
    #
    orderSortTime = rawData.orderList[rawData.orderList[
        'ORDER_PLATFORM'].str.contains('On Air')]

    # Combine date ordered with time ordered
    #
    orderSortTime['DATE_TIME_ORDER'] = pd.to_datetime(orderSortTime[
        'ORDER_DATE'] + ' ' + orderSortTime['ORDER_TIME'])
    
    # Index Orders by the time ordered
    #
    orderSortTime = orderSortTime.set_index('DATE_TIME_ORDER')

    # Remove excess order columns at this point
    #
    orderSortTime = orderSortTime.loc[:,['DATE_TIME_ORDER','TOTAL_LINE_AMT']]
       
    # Reample the data into 10min blocks and combine total_line_amt in that
    # hour and the number of orders in that hour
    #
    orderSortTime = orderSortTime['TOTAL_LINE_AMT'].resample(
            '10min', how=['sum', 'count']) 
    
    logging.debug(orderSortTime)  

    # -------------------------------------------------------------------------
    # - orderMaster is now organized the way we want. Let us clean up airtime -
    # - data ------------------------------------------------------------------
    # -------------------------------------------------------------------------

    # Convert the airTime date to a range which we can compare to the order
    # master
    #
    airTimeData = rawData.mediaList.loc[:,['PRODUCT_NBR','ONAIR_START_TMS',
        'ONAIR_END_TMS', 'HOST1', 'HOST2']]
    
    # Convert dates in dataframe to date data types
    #
    airTimeData['ONAIR_START_TMS'] = pd.to_datetime(airTimeData[
        'ONAIR_START_TMS'])
    
    # Round to 10 min intervals
    #
    ns10min = 10*60*1000000000
    airTimeData['ONAIR_START_TMS'] = pd.DatetimeIndex(((
        airTimeData['ONAIR_START_TMS'].astype(np.int64) 
        // ns10min + 1 ) * ns10min))

    # Remove Dirty Data (No Host)
    #
    airTimeData['HOST1'].replace('',np.nan, inplace=True)
    airTimeData['HOST2'].replace('',np.nan, inplace=True) 
    airTimeData = airTimeData.dropna(subset=['HOST1'])
   
    # Remove extra columns
    #
    airTimeData = airTimeData.loc[:,['ONAIR_START_TMS',
        'HOST1', 'HOST2']]
    
    # Groupby if similar times on air
    #
    airTimeData = airTimeData.set_index('ONAIR_START_TMS')
    
    # More cleanup of dirty data. Remove duplicate rows
    #
    airTimeData = airTimeData.drop_duplicates()
    
    # Merge our two tables based on time
    #
    hostProductSales = pd.merge(orderSortTime, airTimeData, left_index=True,
           right_index=True)
 
    # Remove Dirty Data (No Host) again after merger
    #
    hostProductSales['HOST1'].replace('',np.nan, inplace=True)
    hostProductSales['HOST2'].replace('',np.nan, inplace=True) 
    hostProductSales = hostProductSales.dropna(subset=['HOST1'])

    # Groupy by the host and find the host who sales the most
    #
    hostProductSales = hostProductSales.groupby(['HOST1', 'HOST2']).sum()
    

    # Finally sort by the highest gross sum. Then by the highest number of
    # items sold
    #
    print("Top 10 Hosts by Revenue:")
    print(hostProductSales.sort('sum', ascending=0).head(10))
    print("\n\nTop 10 Hosts by Sold Amount:")
    print(hostProductSales.sort('count', ascending=0).head(10))

