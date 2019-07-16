#Given an array of distinct integers. The task is to count all the triplets such
# sum of two elements equals the third element.
testCase = int(input())
for _ in range(testCase):
    n = int(input())
    a = [int(x) for x in input().split()]

    i = j =c =s=0
    m = dict()
    for x in a:
        m[x] = m.get(x, 0) +1

    j = i+1
    a.sort()
    while(j<n):
        s = a[i] + a[j]
        if s > a[-1]:
            j +=1
            i = 0
            continue
        if m.get(s, 0) !=0:
            c +=1
        #print(i,j,s, c)
        if i < j-1:
            i+=1
        else:
            j+=1
            i = 0
    print(c) if c else print(-1)
