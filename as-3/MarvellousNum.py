def ListPrime(x):
    list = []
    for i in range(0,x):
        el=int(input("Enter elements of list: "))
        list.append(el)
    return list

def chkPrime(list):
    prime = []
    for i in range(len(list)):
        flag = 0
        for j in range(2,int(list[i]/2)+1):
            if list[i] % j == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(list[i])
    return prime
def primeAdd(p):
    pa = 0
    for i in range(len(p)):
        pa= pa + int(p[i])
    return pa
