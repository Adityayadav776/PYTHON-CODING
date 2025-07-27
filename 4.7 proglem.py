#Check that tuple type can not be changed in python
tp=(1, 2, 3)
tp[2]= "tplink"
print(tp)
#Output: TypeError: 'tuple' object does not support item assignment