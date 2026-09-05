#=================================== MATCH ==================================
# import re

# pattern = r'Code'
# text = "Codegnan"

# res = re.match(pattern, text)
# print(res.group() if res else "Pattern Not Found")

#=================================== SEARCH ==================================

# import re

# pattern = r'[0-9]'
# text = "Codegnan26"

# res = re.search(pattern, text)
# print(res.group() if res else "Pattern Not Found")

#=================================== FINDALL ==================================

# import re

# pattern = r'[a-zA-Z]'
# text = "Codegnan2026"

# res = re.findall(pattern, text)
# print(res)
# print(res.group() if res else "Pattern Not Found")

#=================================== FINDITER ==================================

# import re

# pattern = r'[a-zA-Z]'
# text = "Codegnan2026"

# res = re.finditer(pattern, text)
# for i in res:
#     print(i.group(), i.start())

#=================================== FULLMATCH ==================================

# import re

# pattern = r'[0-9]{6}'
# text = "123456"

# res = re.fullmatch(pattern, text)
# print(res.group() if res else "Pattern Not Found")

#=================================== SPLIT ==================================

# import re

# pattern = r'[,(#]'
# text = "python,java(html#css"

# res = re.split(pattern, text)
# print(res)
# print(res.group() if res else "Pattern Not Found")

#=================================== SUB (REPLACE) ==================================

# import re

# pattern = r'e.t'
# text = "e@t ear eaat ett eat ect eet ete"

# res = re.findall(pattern, text)
# print(res)
# #print(res.group() if res else "Pattern Not Found")



# import re

# pattern = r'^(91)'
# text = "91124524"

# res = re.findall(pattern, text)
# print(res)
# #print(res.group() if res else "Pattern Not Found")




# import re

# pattern = r'to*'
# text = "to t too tooo toooooo"

# res = re.findall(pattern, text)
# print(res)
# #print(res.group() if res else "Pattern Not Found")



# import re

# pattern = r'to+'
# text = "to t too tooo toooooo"

# res = re.findall(pattern, text)
# print(res)
# #print(res.group() if res else "Pattern Not Found")


import re

pattern = r'91|0'
text = "91"

res = re.findall(pattern, text)
print(res)