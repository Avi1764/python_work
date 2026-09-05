'''

greater = lambda a,b: a if a>b else b

print(greater(12,13))
print(greater(23,43))
print(greater(1,90))
print(greater(15,19))

wish = lambda name: f'welcome to the course{name}'

print(wish("avinash"))
print(wish("lokesh"))
print(wish("bharat"))
print(wish("gansesh"))

iseven = lambda n: "even" if n%2==0 else "odd" 

print(iseven(47))
print(iseven(20))
print(iseven(43))

avg = lambda a,b,c: (a+b+c)/3

print(avg(4,5,6))
print(avg(98,89,67))

'''
'''
domain = lambda mail: (mail.split('@')[-1]).split('.')[0]

print(domain('avinash@gmail.com'))
print(domain('lokesh@gmail.com'))
print(domain('bharat@gmail.com'))
print(domain('aganesh@gmail.com'))

'''

'''
gst = lambda price: price + price*0.18

print(gst(1000))
print(gst(5000))
print(gst(8000))
'''

'''
prices = [7380,2790,7219,7189,315,222]
res = list(map(lambda price : price + price*0.18,prices))
print(res)

'''

'''
names = ['avinash','bharat','lokesh','ganesh','anil','vikas']
res = list(map(lambda name : name.title(),names))
print(res)

'''

'''
prices = [7380,2790,7219,7189,315,222]
res = list(map(lambda price : price - price*0.3,prices))
print(res)

'''

'''
prices = [7380,2790,7219,7189,315,222]
res = list(filter(lambda price : price >5000,prices))
print(res)

'''

'''
names = {'avinash','bharat','lokesh','ganesh','anil','vikas'}
res = list(map(lambda name :len(name)>5,names))
print(res)

'''
'''
from functools import reduce
l = [3,45,64,78,84]
res = reduce(lambda sum,i:sum+i,l)
print(res)


names = ['avinash','bharat','lokesh','ganesh','anil','vikas']
res = reduce(lambda res,i: res+' '+i,names)
print(res)

'''


products = {'sugar':60,
            'salt':34,
            'eggs':78,
            'cooking oil':134,
            'bread': 50}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))
print(dict(sorted(products.items(),key = lambda i:i[1])))
print(dict(sorted(products.items(),key = lambda i:i[1],reverse=True)))