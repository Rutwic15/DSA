def main():
    n = int(input())

    ## Read the first array
    arr1 = list(map(int, input().split()))
    while len(arr1) < n:
        arr1 += list(map(int, input().split()))
    

    ## Read the second array
    arr2 = list(map(int, input().split()))
    while len(arr2) < n:
        arr2 += list(map(int, input().split()))
    
    p1M = []
    p2M = []
    p1F = []
    p2F = []
    for y in arr1:
        if y < 0:
            p2M.append(abs(y))
        else:
            p1M.append(y)
    
    for y in arr2:
        if y < 0:
            p1F.append(abs(y))
        else:
            p2F.append(y)
    

    # Sort arrays
    p2M.sort()
    p1M.sort()
    p2F.sort()
    p1F.sort()
 
    # Count matches
    c = 0
    j = i = 0
    while i < len(p1F) and j < len(p2M):
        if p2M[j] > p1F[i]:
            c += 1
            j += 1
            i += 1
        else:
            j += 1
 
    j = i = 0
    while i < len(p1M) and j < len(p2F):
        if p2F[j] > p1M[i]:
            c += 1
            j += 1
            i += 1
        else:
            j += 1
 
    print(c)
 
if __name__ == "__main__":
    main()