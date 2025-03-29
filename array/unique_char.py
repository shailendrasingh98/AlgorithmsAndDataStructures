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
    # Assuming character set is ASCII (128 characters)
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
        # ord(char) returns the ASCII value of the character, and ord('a') returns the ASCII value of 'a'. 
        # The difference between the two gives a number between 0 and 25, corresponding to the position of 
        # the letter in the alphabet ('a' = 0, 'b' = 1, ..., 'z' = 25). This value is stored in val.
        val = ord(char) - ord('a')

        #1 << val shifts the number 1 to the left by val positions. This creates a number where only the val-th bit is set.
        # checker & (1 << val) checks whether the val-th bit in checker is already set
        if ((checker & (1<<val))>0): #16 & 1<<4 = 1
            return False
        #This line updates checker by setting the val-th bit to 1. 
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
