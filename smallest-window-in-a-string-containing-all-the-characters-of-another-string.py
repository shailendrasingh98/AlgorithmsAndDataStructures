#code

testCase = int(input())
for _ in range(testCase):
    string = input()
    text = input()
    ans = len(string)
    n = len(text)
    seen = set()
    c = 0
    start = end = -1
    map = dict()
    m = dict()
    for x in text:
        if map.get(x):
            map[x] +=1
        else:
            map[x] =1
    i = 0
    for j, c in range(len(string)):

        if map.get(c, 0) >0 :
            m[c] =1 + m.get(c, 0)
            if m[c] == map.get(c):
                c+=1

            if c >= len(map):
                if j-i+1 < ans:
                    ans = min(ans, j-i+1)
                    start, end = i, j

                while m.get(string[i], 0) > map.get(string[i], 0) or map.get(string[i], 0) ==0:
                    if m.get(string[i], 0) > map.get(string[i], 0):
                        m[string[i]] -=1
                    i+=1

                if j-i+1 < ans:
                    ans = min(ans, j-i+1)
                    start, end = i, j
    print(-1) if start == -1 else print(string[start:end+1])
