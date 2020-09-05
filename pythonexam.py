# use aithmetic operators to print 100.25
import math
number1=2*(10+30)+(60-30)-10+(1/4)
print (number1)
print (4*(6+5))
print (4*6+5)
print (4+6*5)
num2=3+1.5+4
print (type(num2))
num3=5
squarenu=num3 *num3
print (math.sqrt(25))

s='hello'
print(s[1])
print(s[::-1])
print (s[4])
print(s[-1])
print ([0]*3)
list2=[0,0,0]
print (list2)
list3=[1,2,[3,4,'Hello']]
list3[2][2]='goodbye'
print (list3)
list4=[5,3,4,6,1]
print (sorted(list4))
d={'simple key':'hello'}
e=d['simple key']

print (e)
d1={'k1':{'k2':'hello'}}

e1=d1['k1']['k2']
print (e1)

d2={'k1':[{'nest_key':['This is deep',['hello']]}]}

d3=d2['k1'][0]['nest_key'][1][0]

print(d3)

list5=[1,2,2,33,4,4,11,22,3,3,2]
print(list5)
print (sorted(set(list5)))

