name = 'arda'
surname = 'ozgok'
age = 19

#print('My name is {} {}'.format(name, surname))
print('My name is {0} {1}' .format(name, surname))
print('My name is {1} {0}' .format(name, surname))
print('My name is {s} {n}' .format(n=name, s=surname))
print("My name is {} {} and I'm {} years old. " .format(name, surname,'36'))

result = 200 / 700
print('the result is {}' .format(result))
print('the result is {r:1.3}'.format(r=result))

print(f"My name is {name} {surname} and I'm {age} years old.  ")