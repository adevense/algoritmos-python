idade01 = int(input())
idade02 = int(input())
idade03 = int(input())
if idade01 >=5 and idade02 >= 5 and idade03 >= 5 and idade01 <= 100 and idade02 <= 100 and idade03 <= 100:
    if idade01 > idade02 and idade02 > idade03:
       print(idade02) 
    elif  idade01 >=  idade03 and  idade03 >= idade02:
       print(idade03)
    elif  idade02 >=  idade01 and idade01 >= idade03:
       print(idade01)
    elif  idade02 >=  idade03 and idade03 >= idade01:
       print(idade03)
    elif  idade03 >=  idade01 and idade01 >= idade02:
       print(idade01)
    elif  idade03 >=  idade02 and idade02 >= idade01:
       print(idade02) 
else:
   print()