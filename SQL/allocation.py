# 1. make and enter data into table CUSTOMER (Name, contact, address) and perform operations
# 2. make and enter data into table PRODUCTS (ID, Specs, stock, price) and perform operations
# 3. make and enter data into table SALES (cname, prod id, quantity sold) and perform operations
# OPERATIONS ON:  a) customers- add, update delete,view b) products add, update delete,view c) sales: make and view sales
import random
l1=[4,8,16]
for i in range(1,4):
    a=random.choice(l1)
    print(i," allocated to Roll ",a)
    l1.remove(a)