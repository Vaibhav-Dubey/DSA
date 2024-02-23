def topKfrequent(arr, k):
    count = {}
    freq = [[] for i in range(len(arr)+1)]

    for n in arr:
        count[n] = 1 + count.get(n,0)
    for n, c in count.items():
        freq[c].append(n)
    res=[]

    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
            
print(topKfrequent([1],1))