#code
testCase = int(input())
for _ in range(testCase):
    string = input()
    len_so_far = 0
    max_len_so_far = 0
    seen = dict()
    i = 0
    while(i<len(string)):
        if seen.get(string[i], -1) == -1:
            seen[string[i]] = i
            len_so_far+=1
            #print(string[i], len_so_far, i)
            i +=1
            max_len_so_far = max(max_len_so_far, len_so_far)
        else:
            i = seen[string[i]] +1
            seen.clear()
            len_so_far = 0

    print(max(max_len_so_far, len_so_far))


def longestContinousSubArray(Arr):
    map = {}
    max_len_so_far = 0
    i = 0#start
    for j, c in enumerate(Arr):
        if map.get(c):
            i = map.get(c) +1
        else:
            max_len_so_far = max(max_len_so_far, j-i+1)
        map[c] = j # update map with index
    return max_len_so_far
