# your code goes here# cook your dish here
def max_tips(n,x,y,a,b):
    base_sum = sum(b)
    diff = [a[i] - b[i] for i in range(n)]
    diff.sort(reverse=True)
    print(diff)
    
    prefix = [0] * (n+1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + diff[i-1]
    
    print(prefix)
    max_tip = 0
    for i in range(n + 1):
        if i <= x and (n - i) <= y:
            max_tip = max(max_tip, base_sum + prefix[i])
            print("base sum is: ", base_sum+prefix[i])
            print(max_tip)
 
    return max_tip
 
 
# Reading input
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
# Computing and printing result
print(max_tips(n, x, y, a, b))