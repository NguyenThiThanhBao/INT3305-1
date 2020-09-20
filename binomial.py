import math

def prob(n:int,p:float,N: int)-> float:
    combination=math.factorial(N)/(math.factorial(n)*math.factorial(N-n))
    return combination* (p**n)*((1-p)**(N-n))

def infoMeasure (n:int,p:float,N:int)-> float:
    bino= prob(n,p,N)
    re=-math.log2(bino)
    return re

def sumProb(N:int,p:float)->float:
    '''
    BNN (Biến ngẫu nhiên) binomial chỉ có hữu hạn symbol, tổng xs của tất cả các symbol này bằng 1 
    Nên hàm sumProb kiểm tra tổng sx của BNN binomial bằng 1
    '''
    sum=0
    for i in range(0,N+1):
        sum+= prob(i,p,N)
    return sum

def approxEntropy(N:int, p:float) -> float:
    re=0
    for i in range(0,N+1):
        re+=prob(i,p,N)*infoMeasure(i,p,N)
    return re

print(approxEntropy(1000,0.5)) # xấp sỉ 6.03



