def _findSum(arr, N):
    if N <= 0:
        return 0
    else:
        return _findSum(arr, N - 1) + arr[N - 1]


arr = [1, 2, 3, 4, 5]
N = len(arr)
    
ans= _findSum(arr,N)
print(ans)