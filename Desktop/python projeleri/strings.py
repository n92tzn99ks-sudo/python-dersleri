name = 'arda'
surname = 'ozgok'
age = 19 

print('My name is ' + name + ' ' + surname + ' and I am ' + str(age) + ' years old. ' )


name = 'arda'
surname = 'ozgok'
age = 19 

print('My name is ' + name + ' ' + surname + ' and \n I am ' + str(age) + ' years old. ' )

name = 'arda'
surname = 'ozgok'
age = 19 

greeting = 'My name is ' + name + ' ' + surname + ' and I am ' + str(age) + ' years old. ' 

# print(greeting)
print(greeting[0])  
print(greeting[2])
print(greeting[3])
# print(len(greeting))   => len kac harfli oldugunu soyler

name = 'arda'
surname = 'ozgok'
age = 19 

greeting = 'My name is ' + name + ' ' + surname + ' and I am ' + str(age) + ' years old.' 
length = len(greeting)
#print(greeting[length -1])
#print(greeting[-1])

print(greeting[2:5])
print(greeting[3:7])
print(greeting[3:])
print(greeting[:15])
print(greeting[2:40:2])