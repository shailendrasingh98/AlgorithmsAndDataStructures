def unique(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def minion_game(string):
    s = ''.join(string.split(' '))
    vowels = {'A':'A', 'E':'E', 'I': 'I', 'O':'O', 'U': 'U'}
    # your code goes here
    consonents =[]
    vow = []
    for c in s:
        if c.strip() not in vowels:
            consonents.append(c.strip())
        else:
            vow.append(c.strip())
    print(consonents, vow)
    resc = 0
    for c in unique(consonents):
        ind = s.index(c)
        for i in range(1, len(s)+1):
            print('ind+i{},{}'.format(ind, i))
            if ind+i >len(s):
                break
            sub = s[ind:i+ind]
            print(sub)
            if s.count(sub):
                resc += s.count(sub)
    resv=0
    for c in unique(vow):
        ind = s.index(c)
        for i in range(1, len(s.strip())+1):
            print('ind+i{},{}'.format(ind, i))
            if ind+i >len(s):
                break
            sub = s[ind:i+ind]
            print(sub)
            if s.count(sub):
                resv += s.count(sub)
    print(resc, resv)
    if resc==resv:
        print('Draw')
    else:
        print('Stuart {0}'.format(resc)) if resc>resv else print('Kevin {0}'.format(resv))

if __name__ == '__main__':
    minion_game('D AA ')
