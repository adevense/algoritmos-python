n1= input("insira numero 1: ")
n2= input("insira numero 2: ")
n3= input("insira numero 3: ")
#   maior meio menor
if n1 > n2 > n3:
    print(n1,", ",n2,", ",n3)
elif n1 > n3 > n2:
    print(n1,", ",n3,", ",n2)
elif n2 > n1 > n3:
    print(n2,", ",n1,", ",n3)
elif n2 > n3 > n1:
    print(n2,", ",n3,", ",n1)
elif n3 > n1 > n2:
    print(n3,", ",n1,", ",n2)
elif n3 > n2 > n1:
    print(n3,", ",n2,", ",n1)