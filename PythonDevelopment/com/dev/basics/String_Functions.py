#Capatilize function():- It will return a string with first character capatilze and rest of the character in lower case

str1="hello"
print(str1.capitalize())


#Lower Finction():- converts all character to lower case

str2="HELLO"
print(str2.lower())
print(str2.upper())

#Swapcase():- lower to upper and upper to lower
str3="hello"
print(str3.swapcase())

#Tile:-Fisrt letter will be capital for each word and rest will be in lower case

str4="hello how are you"
print(str4.title())

#islower():True if all the character in lower case otherwise false
str5="HeLLo"
print(str5.islower())

str6="hello"
print(str5.islower())

#isUpper():True if all the character in Upper case otheArwise false

str7="HeLLo"
print(str7.isupper())

str8="HELLO"
print(str8.isupper())

#Example
"""
Enter name:uttam
UTTAM
Enter name:UTTAM
uttam
"""

name = input("Enter name:")

if name.isupper():
    print(name.lower())
else:
    print(name.upper())

"""enter 1 character: a
Its a vowel

b
its not a vowel

"""

char1=input("Enter the character")
if char1 in "aeiou":
    print("It is a vowel")
else:
    print("It is not a vowel")