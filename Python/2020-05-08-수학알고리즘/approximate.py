n = [-379.99418604651157, 47.517234218543351, 0.0]
def approx_pi(n):
    x, y, z = n
    return abs(x - -370) < 10

print(approx_pi(n))