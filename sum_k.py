#code



testCase = int(input())
for _ in range(testCase):
    n = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())
    f = True
    i =0
    j = len(arr)-1

    while i !=j:
        if arr[i] + arr[j] ==k:
            print(arr[i], arr[j], k)
            i+=1
            f = False
        elif arr[i] + arr[j] > k:
            j -=1
        else:
            i+=1

    if f :print(-1)






def binarysearch(data , arr):
    l = 0
    r = len(arr)-1

    while(r>=l):
        m = (l + r)//2

        if arr[m] == data:
            return m
        elif data > arr[m]:
            l = m+1
        else:
            r = m -1
    return -1


testCase = int(input())
for _ in range(testCase):
    n = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())
    f = True
    r = 0
    b = arr[1:]
    for i, a in enumerate(arr):
        d = k - a
        if d > arr[-1]:
            print(-1)
            f = False
            break
        if len(b)>1:
            j= binarysearch(d, b)
            print(d, j, b)
            if j!= -1:
                f = False
                print(a, b[j], k)
                r +=1
                b = arr[i+2:-r]
            else:
                b = arr[i+2:-r]


    if f: print(-1)
