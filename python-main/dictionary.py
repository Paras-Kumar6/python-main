#1 Dictionary is ordered 
#2 Dictionary is changeable
#3 DICTIONARY DOESNOT ALLOW DUPLICATES

members  = {
    'FirstName' : 'Paras',
    'LastName' : 'Kumar',
    'Age' : 19,
    'Birthday' : '6 March',
    'Student' : True
}
print(members)
print(members['Age'])

members['Age'] = 20
print(members['Age'])

print(members.keys()) #for calling only keys

members.pop('Age') #for  removing
print(members)

members.setdefault('happy', True) # for addding new things
print(members)

members.setdefault('Birthday', '6 March') #doesnot allow duplicate
print(members)

