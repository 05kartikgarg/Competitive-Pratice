def findElement(arr, n):
    # Forming prefix sum array from 0
    prefixSum = [0] * n
    prefixSum[0] = arr[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]

        # Forming suffix sum array from n-1
    suffixSum = [0] * n
    suffixSum[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffixSum[i] = suffixSum[i + 1] + arr[i]

        # Find the point where prefix
    # and suffix sums are same.
    for i in range(1, n - 1, 1):
        if prefixSum[i] == suffixSum[i]:
            return arr[i]

    return -1


# Driver Code
if __name__ == "__main__":
    x = int(input())
    arr = [j+1 for j in range(x)]
    # print(arr)
    n = len(arr)
    print(findElement(arr, n))
