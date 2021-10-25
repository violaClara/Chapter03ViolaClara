#fungsi formasi bintang semakin ke bawah semakin banyak
def starFormation1(n):
    for i in range(1,n+1):
        print('*'*i)
#fungsi formasi bingan semakin ke bawah semaikn sedikit
def starFormation2(n):
    i=1
    while(i<=n):
        print('*'*n)
        n-=1
#membedakan perintah antara n ganjil/genap sehingga formasi terbentuk sempurna
n=7
if(n%2!=0):
    q= n//2+1
else:
    q=n//2
p=n//2

starFormation1(q)
starFormation2(p)