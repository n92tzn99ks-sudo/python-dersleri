website = "https://www.sadikturan.com"
course = "python Kursu: Baştan sona python programlama rehberiniz (40 saat))"

print(len(course))
print(website[7:10])
print(website[23:26])
print(course[:15])
print(course[15:])
print(course[-15:-1])
print(course[::-1])

s = '12345' * 5 
print(s)
print(s[::5])

name , surname , age , job = 'Bora' , 'Yılmaz' , 32 ,'muhendis'
print("My name is {} {} I'm {} years old and I'm job {}".format(name , surname , age , job)) 
print (f"benim adım {name} {surname} ben {age} yaşındayım benim mesleğim {job}")

s = "Hello world"
s = (s[0:6] + 'W' + s[-4:])
print(s)

x = "abc" * 3
print(x)
print(x[::3])
