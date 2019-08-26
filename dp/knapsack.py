def knapsack(v, w, c, n, k):
    if k[n][c] != 0:
        return k[n][c]
    if c==0 or n ==0:
        k[n][c]= 0

    elif w[n] >c:
        k[n][c] = knapsack(v, w, c, n-1, k)
    else:
        temp1 = knapsack(v, w, c, n-1, k)
        temp2 = v[n] + knapsack(v, w, c-w[n], n-1, k)
        k[n][c] = max(temp1, temp2)
    return k[n][c]
# A naive recursive implementation of 0-1 Knapsack Problem

# Returns the maximum value that can be put in a knapsack of
# capacity W
def knapSack(W, wt, val, n):

    # Base Case
    if n == 0 or W == 0 :
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))

# end of function knapSack

# To test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print knapSack(W, wt, val, n)

k = [[0 for x in range(c+1)] for y in range(n)]
print(knapsack(v, w, c, n-1, k))
