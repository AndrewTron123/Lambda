remainder = lambda num: num % 2       #this will create 'remainder' as a function object

print(remainder(5))

product = lambda x,y: x*y
print(product(2,3))


def testfunc(num):
    return lambda x:x * num
result10 = testfunc(10)
result100 = testfunc(100)

print(result10(9))
print(result100(9))

number_list = [2,6,8,10,11,4,12,7,13,17]
filtered_list = filter(lambda num: (num>7), number_list)
print(filtered_list)

mapped_list = list[map(lambda num: num%2, number_list)]
print(mapped_list)