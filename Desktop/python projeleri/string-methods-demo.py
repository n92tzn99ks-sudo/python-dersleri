website = "https://www.sadikturan.com"
course =  "Python Kursu: Baştan sona python programlama rehberiniz (40 saat)"
 # 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

# result = ' Hello World ' .strip()
# result = ' Hello World ' .lstrip()  # solu siler
# result = ' Hello World ' .rstrip()  # sağı siler

# result = website.lstrip('/:pth')

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

# result = "www.sadikturan.com".strip('w.moc')

# 3- "course" karakter dizisinin tüm karakterleini küçük harf yapın.

# result = course.lower()

# 4- "website" içinde kaç tane a karakteri vardır ? 

# result = website.count('a')
# result = website.count('www')


# 5- "website" "www" ile başlayıp com ile bitiyor mu ? 

#result= website.startswith('www')
#result= website.startswith('http')
#result=website.endswith('com')

# 6- "website" içinde ".com" ifadesi var mı 
result = website.find(".com")
result = website.find(".comm")  # geçmediği için -1 değerini verir
result = course.rfind("python")
result = website.index('com')   # index eğer sonucu bulamazsa hata verir ancak find bulamazsa -1 değerini verir
                                # gelen hata exception
# 7- "course" içindeki karakterlerin hepsi alfabetik mi ? (isalpha, isdigit(rakam mı))
result = course.isalpha()       # => cevaplar true/false olacak 
result = 'Hello'.isalpha()
result = '123'.isdigit()

# 8- "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = 'Contents'.center(50 , "*")
result = 'Contents'.rjust(50 , "*")
result = 'Contents'.ljust(50 , "*")

# 9- "course" karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin 
result = course.replace(' ' , '-')
result = course.replace(' ', '-' , 5) # 5 tane - koyar
result = course.replace(' ' , '')    # boşlukları siler 

# 10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin
result= "Hello World".replace('World' , 'There')

# 11- "course" karakter dizisinin boşluk karakterlerinden ayırın.
result = course.split(' ')
# result = result[2]
result = result[5]

print(result)
