def isuniqueChar(string):
    # you can't form a string of 280 unique characters out of
    # a 128-character alphabet.
    if len(string)>128:
        return False

    unique_map = {}
    for char in string:
        if unique_map.get(char):
            return False
        unique_map[char] = True
    return True

def isuniqueChar2(string):
    # you can't form a string of 280 unique characters out of
    # a 128-character alphabet.
    if len(string)>128:
        return False

    unique_map = [0]*128
    for char in string:
        if unique_map[ord(char)]:
            return False
        unique_map[ord(char)] = True
    return True

def isuniqueChar3(string):
    checker = 0
    for char in string:
        val = ord(char) - ord('a')
        if ((checker & (1<<val))>0): #16 & 1<<4 = 0
            return False
        checker|=1<<val # 0 | 1<<4 = 16
    return True

def isuniqueChar4(string):
    # set will have unique characters
    if len(set(string)) == len(string):
        return True
    return False


if __name__ == '__main__':
    print('Driver utility...')
    print(isuniqueChar('asdfghtr'))
    print(isuniqueChar('asdfghtrrrrtts'))
    print(isuniqueChar2('asdfghtr'))
    print(isuniqueChar2('asdfghtrrrrtts'))
    print(isuniqueChar3('asdfghtr'))
    print(isuniqueChar3('asdfghtrrrrtts'))

    print(isuniqueChar4('asdfghtr'))
    print(isuniqueChar4('asdfghtrrrrtts'))
