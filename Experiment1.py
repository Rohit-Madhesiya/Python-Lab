#Numbers
print("Numbers:")
a = 10
b = 14.5
fl = 2.4e3
print(a, type(a))
print(b, type(b))
print(fl, type(fl))
#Complex Number
print("Complex Numbers:")
com = 2 + 4j
print(com, type(com))
print(com.real, com.imag)
print("com is a complex number:", isinstance(com, complex))
#Character and String
print("Sequence Type:")
c = 'S'
str = "This is a String"
print(c, type(c))
print(str, type(str))
print(str[1:5])
print(str[:5])
print(str[5])
print(str * 2)
#Boolean
print("Boolean Type:")
flag = True
print(flag, type(flag))
print(flag + 10)
#List
print("List Type")
ls = ["hello", "world", 10, 20.4]
ls.append("Python")
print("List:", ls, "Type of:", type(ls))
print(ls[0])
print(ls[4:])
print(ls + ls)
#Tuple
print("Tuple Type:")
tp = ("Rohit", "Rahul", "Raj", "Ravi", "Roshan")
print("Tuple:", tp)
print("Type:", type(tp))
print(tp[5:])
print(tp * 2)
#Dictionary
print("Dictionary Type:")
dc = {
    'Roll': 49,
    "Name": "Rohit Maddheshiya",
    "Course": "MCA",
    "Subject": "Python"
}
print(dc)
for d in dc:
  print(d)
print(dc.keys())
print(dc.values())
#Set
print("Set Type:")
s = {"Rohit", "Rahul", "Rohit", 1, 11.5, "Raj"}
print("Set:", s)
print(type(s))
s.add("Ravi")
print(s)
