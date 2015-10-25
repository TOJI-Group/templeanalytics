#!/usr/bin/env python
import os
import logging

# Pandas DataManagement
import pandas as pd


class rawFileOp():
    # Catch Directory path for data by using the current working directory
    #
    dataPath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))), "data")
    
    # Initialize Variables
    #
    def __init__(self):
        self.customerList = pd.DataFrame()
        self.orderList = pd.DataFrame()
        self.productDescr = pd.DataFrame
        self.mediaList = pd.DataFrame
        self.emailCamp = pd.DataFrame
        self.socialList = pd.DataFrame

    def loadCustomer(self):
        customer_filename = os.path.join(self.dataPath, \
                "qvc", "customer_master.csv")
        if self.customerList.empty:
            # Open customer datafile.
            #
            logging.info("Opening File: '%s'", customer_filename)
            self.customerList = pd.read_csv(customer_filename, \
                    index_col='CUSTOMER_NBR')
            logging.debug(self.customerList)

            # Close file
            #
            logging.info("Closing File: '%s'", customer_filename)
        else:
            logging.info("Skip Loading '%s'. Already Loaded", 
                    customer_filename)
 
    def loadOrder(self):
        order_filename = os.path.join(self.dataPath, \
                "qvc", "order_master.csv")
        if self.orderList.empty:
            # Repeat read in data for orders.
            #
            logging.info("Opening File: %s", order_filename)
            self.orderList = pd.read_csv(order_filename, \
                    index_col='ORDER_NBR', parse_dates = True)
            logging.debug(self.orderList)

            # Close file
            #
            logging.info("Closing File: %s", order_filename)
        else:
            logging.info("Skip Loading '%s'. Already Loaded.", order_filename)

    def loadProduct(self):
        product_filename = os.path.join(self.dataPath, \
                "qvc", "product_master.csv")
        if self.productDescr.empty:
            # Repeat read in data for orders.
            #
            logging.info("Opening File: %s", product_filename)
            self.productDescr = pd.read_csv(product_filename)
            logging.debug(self.productDescr)

            # Close file
            #
            logging.info("Closing File: %s", product_filename)
        else:
            logging.info("Skip Loading '%s'. Already Loaded.", 
                    product_filename)

    def loadAirtime(self):
        airtime_filename = os.path.join(self.dataPath, \
                "qvc", "product_airtime.csv")
        if self.mediaList.empty:
            # Repeat read in data for orders.
            #
            logging.info("Opening File: %s", airtime_filename)
            self.mediaList = pd.read_csv(airtime_filename, \
                    parse_dates = True)
            logging.debug(self.mediaList)

            # Close file
            #
            logging.info("Closing File: %s", airtime_filename)
        else:
            logging.info("Skip Loading '%s'. Already Loaded.", 
                    airtime_filename)

    def loadEmail(self):
        email_filename = os.path.join(self.dataPath, \
                "qvc", "email_campaign.csv")
        if self.emailCamp.empty:
            # Repeat read in data for orders.
            #
            logging.info("Opening File: %s", email_filename)
            self.emailCamp = pd.read_csv(email_filename, \
                    parse_dates = True)
            logging.debug(self.emailCamp)

            # Close file
            #
            logging.info("Closing File: %s", email_filename)
        else:
            logging.info("Skip Loading '%s'. Already Loaded.", email_filename)

    def loadSocial(self):
        social_filename = os.path.join(self.dataPath, \
                "qvc", "social.csv")
        if self.socialList.empty:
            # Repeat read in data for orders.
            #
            logging.info("Opening File: %s", social_filename)
            self.socialList = pd.read_csv(social_filename, \
                    parse_dates = True)
            logging.debug(self.socialList)

            # Close file
            #
            logging.info("Closing File: %s", social_filename)
        else:
            logging.info("Skip Loading '%s'. Already Loaded.",
                    social_filename)


