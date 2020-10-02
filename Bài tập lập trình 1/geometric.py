import math

def prob(n: int, p: float) -> float:
    re= p * (1-p) ** (n-1)
    return re

def infoMeasure (n:int, p:float) -> float:
    inf = prob(n,p)
    re= -math.log2(inf)
    return re

def sumProb(N: int, p:float) ->float:
    '''
        Tổng vô hạn của re= pr(1,p) +Pr(2,p)+.... bằng 1 đây là một dãy dương, lùi vô hạn nên N càng lớn thì tổng của chúng càng tiến tới 1
        nên hàm sumProb có thể kiểm chứng tổng xác suất của phân bố geometric bằng 1 
        Ta chứng minh công thức bằng việc áp dụng công thức tính cấp số nhân lùi vô hạn do N tiến đến vô cùng
        re= p/(1-(1-p))=1
        hoặc tính theo cấp số nhân bình thường
        re= p* ((1-p)^N -1)/(1-p-1) khi N-> vô cùng thì re->1
    '''
    re=0
    for i in range(1,N+1):
        re=re+ prob(i,p)
    return re

def approxEntropy(N:int,p:float)->float:

    '''
       p(i)=prob(i,p)
       Tổng vô hạn của -p(1)log(p(1))+ -p(2)log(p(2))+... 
       Đây là một dãy dương tăng và có giới hạn là entropy của biến ngẫu nhiên geometric nên khi N càng lớn thì hàm approxEntropy dẽ tiến đến entropy của biến ngẫu nhiên geometric
       

    '''
    re=0
    for i in range(1,N+1):
        re += prob(i,p)*infoMeasure(i,p)
    return re

print(approxEntropy(1000,0.5)) # xấp sỉ 2