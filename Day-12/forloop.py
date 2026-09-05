# str,list,tuple,dict,set,range()
'''
for var in seq:
'''


'''
s = "codegnan"
for ch in s:
    print(ch)
'''

'''
s = "codegnan"
for ch in s:
    if ch in "aeiouAEIOU":
        print(ch)
  ''' 


'''
l = [2,4,7,9,20,34,57,89,34,12,45,67,89]
for i in l:
    if i%2 == 0:
        print(i,"even")
    else:
        print(i,"odd")
        '''
''' 

marks = (45,67,89,90,34,56,78,90,100,32,30)
for mark in marks:
    if mark>35:
        print(mark,"pass")
    else:
        print(mark,"fail")
'''


'''
followers = {"avinash","bharat","ganesh","lokesh","anil"}
for i in followers:
    print(i)
'''

'''
bus = {'s1':'bookes','s2':'available','s3':'booked','s4':'available','s5':'booked'}
for seat in bus:
    if bus.get(seat)!='available':
        print(seat,bus.get(seat))
'''

'''
for i in range(1,11):
    print(i)
 '''



'''
for i in range(10,0,-1):
    print(i,end=" ")
  '''



'''
for i in range(2,51,2):
    print(i,end=" ")
'''


'''
for i in range(1,100,2):
    print(i,end=" ")
'''


'''
for i in range(5,51,5):
    print(i)
'''


n=int(input("enter the number: "))
for i in range(1,11):
    print(n,"*",i,"=",i*n)