'''

s = 'python programming'
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])
'''



'''
l=[23,45,67,89,34,12,45,67,89]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
        print(i,l[i])
print(sum)
'''


'''
n=int(input("enter the number: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f"factorial of {n} is {fact}")
'''


'''
data={}
n=int(input("enter the no of sutdents: "))
max_marks=0
for i in range(n):  
    name = input("enter the name: ")
    marks = int(input("enter the marks: "))
    if marks>max_marks:
        max_marks=marks
    data[name]=marks
print(data)
print("maximum marks: ",max_marks)

'''


n=int(input("enter the number of priducts: "))
total=0
data={}
for i in range(n):
    product_name = input("enter the product name: ")
    price = eval(input("enter the price: "))
    quantity = eval(input("enter the quantity: "))
    total = total + price * quantity
print(f"total price:{total}")   