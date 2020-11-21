#!/usr/bin/env python
n=int(input("Please Enter The Number:"))
for i in range(1,n//2+1):
  print("* "*i)
  print("")

for i in range(n//2+1,0,-1):
  print("* "*i)
  print(" ")
