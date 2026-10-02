# a={1,2,3,4,5,6}
# b={3,4,5,6,7,8}
# c={1,3,4,5,7,8}
# print(a.intersection(b).intersection(c))


# .................
# a={1,2,3,4,5,6}
# b={1,2,4,7,8,9}
# print(a^b)

# .................
# a={1,2}
# b={1,2,3,4}
# print(a.issubset(b))
# print(b.issuperset(a))

# ...................
# a={1,2,3,4,5,6,7}
# b={3,4,5,8,6,7}
# print(a - b)
# print(b-a)

# ...................
# a={1,2,3,4,5,6}
# b={3,4,5,6,7,8}
# print(a | b)

# ...................
# a={1,2,3,4,5,6}
# a.add(7)
# print(a)

# ...................
# a={1,2,3,4,5,6,7}
# a.update([8,9,10])
# print(a)

# ...................
# a={1,2,3,4,5,6,7,8}
# a.remove(8)
# print(a)

# ....................
# a={1,2,3,4,5,6,7}
# a.discard(8)
# print(a)

# .....................
# a={1,2,3,4,6,7}
# a.pop()
# print(a)

# .....................
# a={1,2,3,4,6,7}
# a.clear()
# print(a)

# ....................
# a={1,2,3,4,6,7}
# del(a)
# print(a)

# ....................
# a={1,2,3,4,56,7}
# b=(1,2,3,4,7,8,9)
# print(a.union(b))

# ....................
# a={1,2,3,4,5,6}
# b={3,4,5,6,7,8,9,1}
# print(a.intersection(b))

# ....................
# sentence="python is a programming laguage and python is easy to learn"
# words=set(sentence.split())
# unique_words=set(words)
# print(unique_words)

# ....................
# num=[1,2,3,4,5,5,4,3,2]
# unique=set(num)
# print(unique)

# ....................
# text=input("enter a string:")
# vowel={'a','e','i','o','u'}
# result=set(text.lower()).intersection(vowel)
# print("vowels=",result)

# ........................
# dict={1:"abc",
#       2:"cda",
#       3:"fgh",}
# print(dict)

# ...........................
# dict={"ram":"abc",
#       "shyam":"cda",
#       "keshav":"fgh",}
# print(dict)

# ..........................
# d=dict(name="rahul",id=123)
# print(d)

# ..........................
# sentence="python is a programming laguage and python is easy to learn"
# words=set(sentence.split())
# print(words)

# ..........................
# d={}
# print(type(d))

# ..........................
# d={"roll":100,
#    "age":20,}
# d.update({"branch": "cse"})
# print(d)

# ..........................
# d={"roll":100,
#     "age":20,}
# d.setdefault("branch","cse")
# print(d)
# d.setdefault("age",10)
# print(d)

# ...........................
# subjects=["maths","science","english","hindi"]
# d=dict.fromkeys(subjects,"0")
# print(d)

# ............................
 
# marks = {
#     "math": 80,
#     "python": 90,
#     "english": 75,
#     "science": 85
# }
# sum=0
# for val in marks.values():
#     sum+=val
# print("Total:", sum)

# ............................
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "Python"
# }
# print(student)

# ...........................
# student = {
#     "name": "Rahul",
#     "age": 20
# }
# print(student.update({"course": "Python"}))
# print(student)

# ...........................
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Delhi"
# }
# del student["age"]
# print(student)

# ..........................
# data = {
#     "name": "Amit",
#     "age": 21,
#     "marks": 85,
#     "city": "Patna"
# }
# for key in data.keys():
#     print(key)

# ..........................
# text = "banana"

# freq = {}

# for char in text:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1

# print(freq)

# ..........................
# sentence = "python is easy and python is powerful"
# words = sentence.split()
# frequency = {}
# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print(frequency)

# ..........................
# student = {"name": "Rahul", "age": 20, "course": "B.Tech"}
# student["age"]=21
# print(student)

# ..........................
# student = {"name": "Rahul", "age": 20, "course": "B.Tech"}
# print(student["name"])
# print(student["course"])

# ..........................
# student = {"name": "Rahul", "age": 20}
# student["age"] = "22"
# print(student)

# ..........................
# student = {"name": "Rahul", "age": 20}
# del student["age"]
# print(student)

# ..........................
# square=lambda x:x*x
# print(square(5))

#...........................
# fahrenheit_to_celsius=lambda f:(f-32)*5/9
# print(fahrenheit_to_celsius(100))

# .........................
# check_even_odd=lambda x: "even" if x%2==0 else "odd"
# print(check_even_odd(11))

# .............................
# sI=lambda p,r,t: p*r*t/100
# print(sI(100,5,5))

# ..............................
# student = {"name": "Rahul", "age": 20, "course": "B.Tech"}
# print(student["age"])
# print(student["course"])

# ...........................
# student = {"name": "Rahul", "age": 20, "course": "B.Tech"}
# student["age"]=21
# print(student)

# ..............................
# student = {"name": "Rahul", "age": 20, "course": "B.Tech"}
# student.update({"name": "cse"})
# print(student)

# ..............................
# student = {"name": "Rahul", "age": 20, "course": "B.Tech"}
# student.setdefault("branch", "cse")
# print(student)

# .....................................
# student = {"name": "Rahul", "age": 20, "course": "B.Tech"}
# student.setdefault("city","patna")
# print(student)

# ..................................
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "B.Tech"
# }
# for key in student.keys():
#     print(key)

# ...................................
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "B.Tech"
# }
# for value in student.values():
#     print(value)

# ....................................
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "B.Tech"
# }
# for key,value in student.items():
#     print(key,value)
    
    
# .....................................
# marks = {
#     "Math": 85,
#     "Python": 45,
#     "English": 78,
#     "Science": 90
# }
# large=0
# for value in marks.values():
#     if value > large:
#         large=value
# print(large)

# .......................................
# marks = {
#     "Math": 85,
#     "Python": 45,
#     "English": 78,
#     "Science": 90
# }
# large = 0
# large_key = ""
# for x, value in marks.items():
#     if value > large:
#         large = value
#         large_key = x
# print(large_key, ":", large)


# .......................................
# marks = {
#     "Math": 85,
#     "Python": 90,
#     "English": 78,
#     "Science": 91
# }
# for key,values in marks.items():
#     if values%2==0:
#         print(key)

# ....................................
# marks = {
#     "Rahul": 75,
#     "Aman": 45,
#     "Priya": 82,
#     "Ravi": 55,
#     "Neha": 90
# }
# count=0
# for value in marks.values():
#     if value > 60:
#         count=count+1
# print(count)

# ........................
# student = {"name": "Rahul", "age": 20, "course": "B.Tech"}

# deleted = student.pop("course")

# print(deleted)
# print(student)

# ..............................
# marks = {
#     "Rahul": 75,
#     "Aman": 45,
#     "Priya": 82,
#     "Ravi": 55,
#     "Neha": 90}
# print(marks["Rahul"])

# ................................
# marks = {"Math": 85, "Python": 90, "English": 78}

# search_value = 90

# for key in marks.keys():
#     if marks[key] == search_value:
#         print(key)


    