#Python program for nth Catalan Number
# Returns value of Binomial Coefficient C(n, k)
def binomialCoefficient(n, k):

    # since C(n, k) = C(n, n - k)
    if (k > n - k):
        k = n - k

    # initialize result
    res = 1

    # Calculate value of [n * (n-1) *---* (n-k + 1)]
    # / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res // (i + 1)
    return res

# A Binomial coefficient based function to
# find nth catalan number in O(n) time
def catalan(n):
    c = binomialCoefficient(2*n, n)
    return c//(n + 1)

def no_of_bsts(n, s):
    if n<0:
        return 0
    if n <2:
        return 1
    res = 0
    for i in range(n):
        if s[i] ==-1:
            s[i] = no_of_bsts(i, s)
        if s[n-i-1] ==-1:
            s[n-i-1] = no_of_bsts(n-i-1, s)
        res += s[i]*s[n-i-1]
    return res



if __name__ == '__main__':
    for i in range (11):
        print (catalan(i), end=" ")
    print()
    print('=============================== No of bsts=================')
    n = 10
    s = [-1]*n
    print(no_of_bsts(n, s))
