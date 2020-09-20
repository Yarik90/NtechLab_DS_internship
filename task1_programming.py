def findMaxSubArray(A):
    n = len(A)
    ans = A[0]
    ans_l = 0
    ans_r = 0
    sum = 0
    minus_pos = -1;
    for i in range(n):
        sum += A[i]
        if sum > ans:
            ans = sum
            ans_l = minus_pos + 1
            ans_r = i
        if sum < 0:
            sum = 0
            minus_pos = i
    print(A[ans_l:ans_r+1])


a = [-2,1,-3,4,-1,2,1,-5,4]
findMaxSubArray(a)