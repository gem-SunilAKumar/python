1,2,3,4,5,6,7,8,9,10,11

# 1 Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample
# Items: green-red-yellow-black-white
# Expected
# Result: black-green-red-white-yellow

# str=input("enter the string: ") 
# temp=str.split('-') 
# temp.sort() 
# print('-'.join(temp)) 


#2 write a Python program to access a function inside a function.
# def outerFunction(mess): 
#     print("outer function evoked :",mess)
    
#     def innerFunction(): 
#         print("inner function evoked :" , mess) 
    
#     innerFunction() 

# outerFunction("Sunil kumar")

# 3) Write
# a Python program to reverse a string

# Sample
# String: "1234abcd"

# Expected
# Output: "dcba4321"

# str1 = "1234abcd"
# print("not - reverserd",str1)
# str1 = str1[::-1]    
# print("reverserd",str1)

# 4 Write a Python program to find the first duplicate element in a given array of integers.
# Return -1 If there are no such elements.

# def find_first_dup(arr):
#     present = set()

#     for i in range(len(arr)):
#         if arr[i] in present:
#             return arr[i]
#         else:
#             present.add(arr[i])

#     return -1

# arr = [1,2,3,4,5,6,7,9,8,7]
# print(find_first_dup(arr))

# 5) Write a Python program to get the number of occurrences of a specified element in an array.

# def find_count(my_array, element):
#     count=0
        
#     for i in my_array:
#         if i == element:
#             count = count + 1
            
#     return(count) 
      
# arr=[1,2,3,4,5,3,3] 
    
# res = find_count(arr, 3)
  
# # print the array
# print ('our array :', arr)
 
# # print the value of count 
# print ('Element 3 occurs ' ,(res),' times')

# 6 Write a function that computes the volume of a sphere given its radius.
# def compute(radius):
#     pie=3.14285  
#     return (4.0/3.0)*pie*(radius*radius*radius)  

# radius=6 
# volume= compute(radius);
# print("volume of the sphere=" , (volume))  

#7 Write a function that checks whether a number is in a given range (Inclusive of high and low)
# def if_range(n):
#     if n in range(3,9):
#         print( " Is inside the range")
#     else :
#         print("The number is outside the given range.")

# if_range(5)
# if_range(50)

#8 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# def cal_upper_lower(str):
#   uppers = 0
#   lowers = 0
#   for char in str:
#     if char.islower():
#       lowers += 1
#     elif char.isupper():
#       uppers +=1
#     else:
#       pass # for digits etc.
#   return(uppers, lowers)

# print(cal_upper_lower('abcDeFG'))

# 9 Write a Python function that takes a list and returns a new list with unique elements of the first list.
# def unique(numbers):
#     unique = []
#     for item in numbers :
#         if item not in unique:
#             unique.append(item)
#     return unique

# print(unique([1, 2, 3, 1, 2,7,7]))

# 10 Write a Python function to multiply all the numbers in a list.**\n",
# def mul_List(myList): 
#     result = 1
#     for x in myList:
#         result = result * x
#     return result
 
# print(mul_List([1,2,3,4,5,6,-7]))

# 11 Write a Python function that checks whether a passed string is palindrome or not.
#Define a function 
# def isPalindrome(str):
 
#     for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True
 
# name = "nitin"
# ans = isPalindrome(name)
 
# if (ans):
#     print("Yes")
# else:
#     print("No")

# 12 Write a Python function to check whether a string is pangram or not.
 
# def ispangram(str):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet:
#         if char not in str:
#             return False
#     return True
     
# string = 'abcd efgh ijkl mnop qrstu vwx yz aaa bbb n'
# if(ispangram(string) == True):
#     print("Yes")
# else:
#     print("No")

# 13 Write a Python program to print the following string in a specific format
# String : "Twinkle, twinkle, little star, How I wonder what you are! Up

# above
# the world so high, Like a diamond in the sky. Twinkle, twinkle, little star,

# How I
# wonder what you are"

# Output
# :
# Twinkle,
# twinkle, little star,

# How I
# wonder what you are!

# Up above
# the world so high,

#   Like
# a diamond in the sky.

# Twinkle,
# twinkle, little star,

# How I
# wonder what you are

# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

 
#14 Write a Python program to accept a filename from the user and print the extension of that.
# fn= input("Enter Filename: ")
# f = fn.split(".")
# print ("Extension of the file is : " + f[-1])

# 15 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# num = int(input("Input an integer : "))
# n1 = int( "%s" % num )
# n2 = int( "%s%s" % (num,num) )
# n3 = int( "%s%s%s" % (num,num,num) )
# print (n1+n2+n3)

# 16 Write a Python program to check whether a specified value is contained in a group of values.
# def is_member(group_data, n):
#    for value in group_data:
#        if n == value:
#            return True
#    return False
# print(is_member([1, 5, 8, 3], 3))
# print(is_member([5, 8, 3], -1))

#17 Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527
#     ]

# for x in numbers:
#     if x == 237:
#         print(x)
#         break;
#     elif x % 2 == 0:
#         print(x)

# 18 Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
# def test_number5(x, y):
#    if x == y or abs(x-y) == 5 or (x+y) == 5:
#        return True
#    else:
#        return False
# print(test_number5(2, 2))
# print(test_number5(3, 2))
# print(test_number5(8, 3))

# 19 Write a Python program to display your details like name, age, address in three different lines.
# def detail():
#     name, age = "Sunil", 22
#     address = "Chandigarh"
#     print(name)
#     print(age)
#     print(address)
# detail()

#  20 Write a Python program to solve (x + y) * (x + y).
# x, y = 2, 6
# result = x * x + 2 * x * y + y * y
# print(result)

# 21 Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
# colors_1 = set(["White", "Black", "Red"])
# colors_2 = set(["Red", "Green"])

# print("\nDifferenct of color_list_1 and color_list_2:")
# print(colors_1 - colors_2)

