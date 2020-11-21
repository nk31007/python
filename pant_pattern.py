#!/usr/bin/env python
n=int(input("Please Enter The Number:"))
for i in range(0,n+1):
 print("* "*(n//2-i)+(" "*i)*4+" *"*(n//2-i))

