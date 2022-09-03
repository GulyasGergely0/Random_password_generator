import random

characters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
            "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
            ".", ",", "/","+", "!", "%","=","(", ")", "'", "_", "-", "?", "[", "]", "*"]

random.shuffle(characters)
random.shuffle(characters)
random.shuffle(characters)

password=[]


length=int(input("Password length: "))

for i in range(length):
    i=random.choice(characters)
    password.append(i)

random.shuffle(password)
random.shuffle(password)
random.shuffle(password)

a=''.join(password)
print(a)





        

