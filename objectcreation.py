#!/usr/bin/python

class Customer(object):
	"""__init() functions as the class constructor"""
	def __init__(customer,id=None, state=None, zipcode=None, segment=None):
		customer.id = id
		customer.state = state
		customer.zipcode = zipcode
		customer.segment = segment

#	def __del__(self):
#		customer.id = None
#		customer.state = None
#		customer.zipcode = None
#		customer.segment = None


class Order(object):
	def __init__(order, number = None, line = None, customerid = None, productnum = None, platform = None, date = None, time = None, amount = None):
		order.number = number
		order.line = line
		order.customerid = customerid
		order.productnum = productnum
		order.platform = platform
		order.date = date
		order.time = time
		order.amount = amount

#	def __del__(self):
#		order.number = None
#		order.line = None
#		order.customerid = None
#		order.prodnum = None
#		order.platform = None
#		order.date = None
#		order.time = None
#		order.amount = None


class Media(object):
	def __init__(Media, productid = None, date = None, starttime = None, endtime = None, airtime = None, Host1 = None, Host2 = None):
		Media.productid = productid
		Media.date = date
		Media.starttime = starttime
		Media.endtime = endtime
		Media.airtime = airtime
		Media.host1 = Host1
		Media.host2 = Host2




print

import csv
f = open('customer_master.csv')
csv_f = csv.reader(f)
customerlist = []
for row in csv_f:
	customerlist.append(Customer(row[0],row[1],row[2],row[3]))


# Test that data is stored correctly
n = 1
#print "ID:" + customerlist[n].id + " State:" + customerlist[n].state + " ZipCode:" + customerlist[n].zipcode + " CustomerSegment:" + customerlist[n].segment


# Lets get crazy and sort in place
import operator 
customerlist.sort(key=operator.attrgetter('id'))

#for customer in customerlist:
#	print "ID:%s State:%s Zipcode: %s" % (customer.id, customer.state, customer.zipcode)

f.close()


f = open('order_master.csv')
csv_f = csv.reader(f)
orderlist = []
for row in csv_f:
	orderlist.append(Order(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

#print "Order Number:" + orderlist[n].number + "\nOrder Line:" + orderlist[n].line + "\nCustomer ID:" + orderlist[n].customerid 
#print "Product Number:" + orderlist[n].productnum + "\nPlatform:" + orderlist[n].platform + "\nDate:" + orderlist[n].date 
#print "Time:" + orderlist[n].time + "\nAmount:" + orderlist[n].amount

f.close()

f = open('product_airtime.csv')
csv_f = csv.reader(f)
medialist = []
for row in csv_f:
	medialist.append(Media(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))


#print "Product Number:" + medialist[n].productid + "\nAir Date:" + medialist[n].date + "\nStart Time:" + medialist[n].starttime
#print "End Time:" + medialist[n].endtime + "\nAirtime:" + medialist[n].airtime + "\nHost 1:" + medialist[n].host1
#print "Host 2:" + medialist[n].host2

f.close()
