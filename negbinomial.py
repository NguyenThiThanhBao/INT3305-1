import math


def prob(n:int,p:float,r:int) ->float:
    combination=math.factorial(n-1)/(math.factorial(r-1)*math.factorial(n-r))
    re=combination* p**r *(1-p)**(n-r)
    return re

def infoMeasure (n:int, p:float, r:int) -> float:
    info = prob(n,p,r)
    re= -math.log2(info)
    return re

def sumProb(N:int, p:float, r:int)->float:
    '''
        
    '''
    sum=0
    for i in range (r,N+1):
        sum+=prob(i,p,r)

    return sum

def approxEntropy(N:int, p:float, r:int)->float:
    
    re=0
    for i in range(r,N+1):
        re+= prob(i,p,r)* infoMeasure(i,p,r)
    return re

print(approxEntropy(1000,0.5,90))# xấp sỉ 5.7869
