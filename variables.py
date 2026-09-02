maasAli = 5000
maasAhmet = 4000
vergi = 0.27
print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))
print (5000 - (5000 * 0.27))
print(4000 - (4000 * 0.27))

# Değişken Tanımlama Kuralları 

# rakam ile başlamaz 

number1 = 10 
print(number1)
number1 = 20 
print(number1)
number1 += 30
print(number1)

# Büyük küçük harf duyarlılığı vardır 

age = 20
AGE = 30

print(age)
print(AGE)


# Türkçe karakter kullanmayalım

yas = 20 
_age = 20 

x = 1                   # int
y = 2.3                 # float
name = "Çınar"          # string
isStudent = True        # bool

a = 10 
b = 20
print(a+b)     #30

a = "10"
b = "20"
print(a+b)    #1020 string olarak algılanır

firstName = "Arda"
lastName = " Özgök"

print(firstName + lastName)  # Arda Özgök 

#  x, y, name, isStudent = (1, 2.3, "Çınar",True) 