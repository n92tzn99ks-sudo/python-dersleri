# message = "Hello There. My mame is Sadık Turan".split()
# print(message[0])

# my_list = [1,2,3]
# my_list = ['bir' , 2 , True , 5.6]
# print(my_list)

list1 = ['one' , 'two' , 'there']
list2 = ['four' , 'five' , 'six' ,]

numbers = list1 + list2

print(numbers)
print(len(numbers))   # kaç elaman olduğunu öğreniyoruz
print(numbers[2])

userA = ['Arda' , 19]
userB = ['Çınar' , 2]

users = userA + userB
users = userA , userB

# a = users[1]        # user[1] ['Çınar' , 2] oluyor

# print(a[0])

print(users[1][0])    # çınar oluyor eğer 0 değil 1 deseydi sonuç 2 olurdu
                      # ilk parantez 0 olsaydı Arda yazardı 