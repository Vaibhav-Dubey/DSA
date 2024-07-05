def pivotInteger(n):
    sum=0
    lsum,rums=0,0
    l,r = 1,n
    lsum=l
    rsum=r
    while(l<r):
        
        if lsum == rsum:
            return l
        l+=1
        r-=1
        lsum+=l
        rsum+=r
        print(lsum, rsum , l ,r)
    return -1

pivotInteger(8)