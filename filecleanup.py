#!/usr/bin/python



print("Cleaning up customer_master.csv")
with open("customer_master.csv",'r') as f:
    with open("updated_customer_master.csv",'w') as f1:
        f.next() # skip header line
        for line in f:
            f1.write(line)

f1.close()
f.close()

print("Done cleanup of customer_master.csv")
print
print("Cleaning up order_master.csv")

with open("order_master.csv",'r') as f:
    with open("updated_order_master.csv",'w') as f1:
        f.next() # skip header line
        for line in f:
            f1.write(line)
f1.close()
f.close()

print("Done cleanup of order_master.csv")
print
print("Cleaning up product_master.csv")

with open("product_master.csv",'r') as f:
    with open("updated_product_master.csv",'w') as f1:
        f.next() # skip header line
        for line in f:
            f1.write(line)

f.close()
f1.close()

print("Done cleanup of product.csv")
print
print("Cleaning up social.csv")

with open("social.csv",'r') as f:
    with open("updated_social.csv",'w') as f1:
        f.next() # skip header line
        for line in f:
            f1.write(line)

f.close()
f1.close()

print("Done cleanup of social.csv")
print
print("Cleaning up product_airtime.csv")

with open("product_airtime.csv",'r') as f:
    with open("updated_product_airtime.csv",'w') as f1:
        f.next() # skip header line
        for line in f:
            f1.write(line)

f.close()
f1.close()

print("Done cleanup of product_airtime.csv")
print
print("Cleaning up email_campaign.csv")


with open("email_campaign.csv",'r') as f:
    with open("updated_email_campaign.csv",'w') as f1:
        f.next() # skip header line
        for line in f:
            f1.write(line)

f.close()
f1.close()

print("Done cleanup of email_campaign.csv")
