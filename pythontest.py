list4 = [5,3,4,6,1]
print (sorted(list4))
print(2**0.5)
print (4**2)
print(4*2)
print('hello world')
print('hello My name is {r}'.format(r='jose'))
name='jose'
print (f'hello his name is {name}')
print('division value is {r:1.2f}'.format(r=130/200))
mylist=[1,2,[2,4]]
print (mylist[2][1])
print(mylist[1:])
popitem=mylist.pop()
print (popitem)

mydict={'key1':'abc', 'key2':'def'}
mydic=mydict['key1'].upper()
print(mydic)
mydic = mydict['key1'] + ' ' + mydict['key2']
print(mydic)
mylist=[1,2,3]
mylist[0]=4
print(mylist[0])


mydict_1={'key1':200,'mango':324}
print (mydict_1['key1'])

print(set('missisipi'))

myfile =open('/Users/sohankumar/Desktop/test.txt','w')
myfile.write('Hello World')
myfile.close()
myfile =open('test.txt','r')
print (myfile.read())
myfile.close()
myfile =open('/Users/sohankumar/Desktop/test.txt','a')
myfile.write('\nHello World2')
myfile =open('test.txt','r')
print (myfile.read())



