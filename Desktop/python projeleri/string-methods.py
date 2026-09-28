message = "Hello There . My name is Sadık Turan"

# message = message.upper()       =>hepsini büyük yazar
# message = message.lower()       =>hepsini küçük yazar
# message = message.title()       =>kelimelerin ilk harfi büyük yazılır
# message = message.capitalize()  =>sadece ilk kelime büyük diğerleri küçük yazılır
# message = message.strip()       =>eğer başlangıçta boşluk varsa o boşluk gider
# message = message.split(".")
# message = message.split()       # =>her kelime ayrılır tırnakla
# message = " * " .join(message)  # =>kelimeler arasına * ekler

index = message.find("Sadık")     # =>Sadık kelimesi geçiyor mu diye baktık 
index = message.find("Sadıkk")    # =>-1 ise o kelime geçmiyordur
isFound = message.startswith('H') #h ile başlayaıp başlamadığına baktık true/false
isFound = message.endswith('n')   #n ile bitiyor yani true

message = message.replace ('Sadık' , 'Çınar').replace(' ' , '-')  #sadık yazan kelimeyi bulup yerine çınar yazar
message = message.center(50 , '*')      # baitan ve sondan eşit boşluklar bırakarak ortalar (başa sona yıldız koydu)

print(index)
print(isFound)
print(message)
print(isFound)
print(message)
print(message)