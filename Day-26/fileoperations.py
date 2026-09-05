'''

with open('pfs-63.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readline())

'''

'''
with open('mysql.txt','w') as file:
    file.write("DDL,DML,DQL")
'''

'''
with open('pfs-63.txt','w') as file:
    file.write("Shifted to Branch-1")

'''

'''
with open('pfs-63.txt','a') as file:
    file.write("\nonly for today")

'''

with open('pfs-63.txt','a+') as file:
    file.write("\ntom same branch 5")
    file.seek(0)
    print(file.read())

