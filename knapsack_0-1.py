# DP
def knap_sack_dp(weight_array, value_array, weight, n):
    k = [[0 for x in range(weight + 1)] for x in range(n + 1)]
    for i in range(0, n + 1):
        print("*******")
        for w in range(0, weight + 1):
            print(w)
            if i == 0 or w == 0:
                k[i][w] = 0
            elif weight_array[i - 1] <= w:
                k[i][w] = max(value_array[i - 1] + k[i - 1][w - weight_array[i - 1]], k[i - 1][w])
            else:
                k[i][w] = k[i - 1][w]

    return k[n][weight]


# Recursion
def knap_sack(weight_array, value_array, weight, n):
    if weight == 0 or n == 0:
        return 0
    elif weight_array[n] > weight:
        return knap_sack(weight_array, value_array, weight, n - 1)
    else:
        return max(knap_sack(weight_array, value_array, weight, n - 1),
                   value_array[n] + knap_sack(weight_array, value_array, weight - weight_array[n], n - 1))


# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
val = [8,4,0,5,3]
wt = [1,2,3,2,2]
W = 4
n = len(val)
# res = knap_sack(wt, val, W, n - 1)
res = knap_sack_dp(wt, val, W, n)
print(res)
