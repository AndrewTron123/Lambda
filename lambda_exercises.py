''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
number_list = [1,2,3,4,5,6,7,8,9,10]
filtered_list = list(filter(lambda num: num%2 == 0, number_list))
print(f'Even Numbers: {filtered_list}')

number_list = [1,2,3,4,5,6,7,8,9,10]
filtered_list = list(filter(lambda num: num%2 != 0, number_list))
print(f'Odd Numbers: {filtered_list}')



''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
filtered_weekdays = list(filter(lambda x: len(x) == 6, weekdays))
print(f'Weekdays with 6 characters: {filtered_weekdays}')







''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']

remove_list = ['orange', 'black']

specified_list = list(filter(lambda y: y not in remove_list, original_list))
print(f'New list: {specified_list}')








''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

new_list = list(filter(lambda z: z not in list2, list1))
print(f' New list: {new_list}')







''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''

colors = ['red', 'black', 'white', 'green', 'orange']
substring = 'ack'
substring_list = list(filter(lambda a: substring in a, colors))
print(f'Substring list: {substring_list}')

colors = ['red', 'black', 'white', 'green', 'orange']
substring = 'abc'
substring_list = list(filter(lambda a: substring in a, colors))
print(f'Substring list 2: {substring_list}')



''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world"
str1 = "HELLO"
str1= "hello"

uppercase = lambda p: any(c.isupper() for c in p)
lowercase = lambda p: any(c.islower() for c in p)
digit_case = lambda p: any(c.isdigit() for c in p)
length = lambda p: len(p) >= 8

check_password = lambda s: all(func(s) for func in [uppercase, lowercase, digit_case, length])

passwords = ["Hello8world", "HELLO", "hello"]

for password in passwords:
    if check_password(password):
        print(f"The password '{password}' meets the criteria.")
    else:
        print(f"The password '{password}' does not meet the criteria.")








''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_scores = sorted(original_scores, key = lambda sort: sort[1])
print(f'Sorted scores: {sorted_scores}')