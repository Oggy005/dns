# Kanvi Panchal -> TYCS - 542
# Transposition Cipher Techniques - Simple Columnar Cipher
key = input("Enter Key: ")
userval = input("Enter the value: ")
col = len(key)
if ((len(userval)%col)!=0):userval+="x"*(len(userval)%col)
userval = userval.replace(" ", "")
o=[]

for i in key:
    o.append(i)
    h=[]
for i in range(col):
    h.append(userval[i:len(userval):col])
    dic = dict(zip(o,h))
    so = sorted(dic.keys())
    print("".join(dic[i]for i in so ))
