# Aşağıdaki veri değerlerinin veri yapılarını inceleyiniz.

#1
x = 8
type(x)
y = 3.2
type(y)
z = 8j + 18
type(z)
a = "Hello world"
type(a)
b = True
type(b)
c = 23 < 22
type(c)
l = [1, 2, 3, 4]
type(l)
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)
t = ("Machine learning", "Data Science")
type(t)
s = {"python", "Machine Learning", "Data Science"}
type(s)

#2 Görev 2 yapılamadı.

"""text= "The goal is to turn data into information, and information into insight."
len(strings)
new_string = []
def diveding(strings):
    while (0, 71) in strings:
        return strings.upper()
        while (0, 71) in strings:
           return strings.split()
           while (0, 71) in strings:
               return strings.append(list(new_string))
    print(new_string)
"""

# ÇÖZÜM

text= "The goal is to turn data into information, and information into insight."
text.upper().replace(" ", ".").replace("."," ").split
text.split()

# 3

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
len(lst)
lst[0]
lst[10]
lst.pop(8)
lst[0 : 4]
lst.append("ekleme yapıldı.")
lst.insert(8, "N")


#4

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}
dict.keys()
dict.values()
dict ["Daisy"] = ["England", 13]
dict ["Ahmet"] = ["Turkey", 24]
dict.pop('Antonio')


# 5

list1 = [2, 13, 18, 93, 22]
for item in list1:
    print(item)
A = []
B = []

def function(list1):
    for item in list1:
       if item % 2 == 0:
        A.append(item)
       else:
        B.append(item)
    return A, B

list1 = [2, 13, 18, 93, 22]
print(function(list1))
function(list1)


#6

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, student in enumerate(ogrenciler):
    if index < 3:
        index += 1
        print("Mühendislik Fakültesi" , index , ". öğrenci:" , student)
    else:
        index -= 2
        print("Tıp Fakültesi" ,index , ". öğrenci:", student)