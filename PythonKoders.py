'''def fullname(firstname,lastname):
    return firstname,lastname
returned_value=fullname("Sannya","Wasim")
print("Person's name is : ",returned_value)'''

#def fun(x,y):
    #ans=print(x**y+100)

#fun(2,3)

'''string="Pakistan"
print(string[::-1])#inseeting -1 we canrun the string in reverse
print(string[0:])

print(help(print))
print("hello",end="@")#weoverride the property of end
print("hi")

variable = "Class7"
length = len(variable) #6
for i in range(0,length): #5
    print(i,variable[i])


alphabets = input("Enter string: ").lower()
vowels = ["a","e","i","o","u"]
vowel_count = 0
consonant_count = 0
for i in alphabets:
    if i in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print("Our vowel count is ", vowel_count)
print("Our consonant count is", consonant_count)

# alphabets.extend(digits)
# print(alphabets)

for i in digits:
    alphabets.append(i)

print(alphabets)

students = {
    1: {
        'name': 'Hasham',
        'father_name': 'Khalid'
    },
    2: {
        'name': 'Midha',
        'father_name': 'Tahir'
    }
}'''

# key => unique

# print(students[1])
# print(students[2])

# items -> key, value
# keys
# values

# for key in students.keys():
#     print(key)

# for value in students.values():
#     print(value)

# for key, value in students.items():
#     print(key, ":", value)

#x,y,z=1,2,3
#print(x,y,z)

# my_tuple = ("apple","mango","banana")
# print(len(my_tuple))

#
# days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
#
# days = list(days)
# print(type(days))

#
# a = 1,
# print(type(a))


#x, *y = (1, 2, 3, 4)
#print(x)
#print(y)

'''fname=input("Enter your First name: ")
lname=input("Enter your Last name: ")
date=input("Enter your year of birth: ")
enter=input("Press Enter Key to generate an Email ID")
print(fname+"."+lname+date,end="@")
print("gmail.com")'''

'''string="bangtan sonyeodan"
for i in string:
    print(i,end="   ")'''


# set1 = {1,2,3,1,2,3,4}
# print(set1)
#
# basket = {"apple","mango","apple","pear"}
# print(basket)
#
# empty_dict = {}
# print(type(empty_dict))
# empty_set = set()
# print(type(empty_set))
#
# set_string = set("abcdsgajaabdsch")
# set_string.add("z")
# # print(set_string[-1]) #error
# print(set_string)
#
# frozen_set_string = frozenset("abcdsgajaabdsch")
# # frozen_set_string.add("z") #immutable
# print(frozen_set_string)


s1 = {1,2,3,4,5}
s2 = {4,5,1,2,6,7}

# # intersection
# print(s1.intersection(s2))
# print(s1 & s2)
#
# #union
# print(s1.union(s2))
# print(s1 | s2)
#
# #difference
# print(s2.difference(s1))
# print(s2 - s1)
#
# #symmetric difference
# print(s1.symmetric_difference(s2))
# print(s1 ^ s2)
#
# #superset
# print(s1.issuperset(s2))
# print(s1 >= s2)
#
# #subset
# print(s1.issubset(s2))
# print(s1 <= s2)


# s1 = {1,2,3,4,5}
# s2 = {4,5,1,2,6,7}
# print(2 in s1)
# # s1.discard(7)
# # print(s1)
# # s
# # print(s1)
# # s1.remove(7)
# # print(s1)
# s1.update(s2)
# print(len(s1))

#remove duplicates
# restaurants = ["Mcdonalds","Pizza Hut","KFC","Pizza Hut"]
# another_collection = list(set(restaurants)) #duplicates will be removed
# print(another_collection)

# no=int(input("Enter the number of players participated: "))
# scores=input("Enter scores of the player: ").strip().split()
# scores=list(map(int,scores))
# print(scores)
# scores.sort()
# scores.pop()
# sec_score=scores[-1]
# print("Score of the runner up is: ",sec_score)
#
# print()

#string-->list==split
#list-->string==join

# l=['s','a','n','n','y','a']
# s="S a n n y a"
#
# print(s.split(" "))
# print("".join(l))

# string="this is a string"
# save=string.split(" ")
# print(save)
# print("-".join(save))




















