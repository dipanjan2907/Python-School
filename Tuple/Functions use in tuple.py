=dict1={'Physics':22,'Chemistry':9,'Maths':8,'Computer':29}
print(dict1)
print(dict1['Computer'])
dict1['English']=31
print(dict1)
print('Physics' in dict1)
for key,value in dict1.items():
    print(key,'=',value)
dict2={'UT1 F.M.':35}
dict1.update(dict2)
print(dict1)
print(dict1.keys())
print(dict1.values())
del dict1['English']
print(dict1)
