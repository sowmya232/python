# for i in range(1, 21):
#     print(i)

# print('=============================================')

# for i in range(1, 41):
#     if i % 2 == 0:
#         print(i)

# print('=====================================')


# # skip value in range

# for i in range(2,41, 2):
#     print(i)


# print('===================================================')

# sum = 0

# for i in range(1, 21):
#     sum += i

# print(sum)


# print('---------------------------------------')

# list1 = [ 1, 2, 3, 4, 5]

# # basically manaki values kavali iterable lo ante e for loop rayali
# for i in  list1:
#     print(i)

# # basically manaki indexes kavali so we can give conditions based on indexes

# for i in range(0, len(list1)):
#     print(i)
#     print(list1[i])


# num = 5

# for i in range(1, 21):
#     print(5 * i)



# # while loop is based on condition

# num1 = 1

# while(num1 < 21):
#     print(num1)
#     num1 += 1

# num1 = 2 

# while(num1  < 41):
#     print(num1)
#     num1 += 2


side1 = 6
side2 = 3
side3 = 3

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    if side1 == side2 == side3:
        print('equilateral triangle')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('isosceles triangle')
    else:
        print('scalene triangle')
else:
    print("can't form a triangle")


flag = True

while flag :
    num = int(input('Enter a number: '))
    
    if(num < 0):
        flag = False
        
        
num = 12345
reverse = 0
sum = 0
count = 0
while(num > 0):
    
    r = num % 10
    if( r % 3 == 0):
        print(r)
    sum = sum + r
    count += 1
    reverse = reverse * 10 + r
    num = num // 10

print(reverse)
print(sum)
print(count)