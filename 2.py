X=int(input())
A=list(map(int, input().split()))
left, right = 0, len(A) - 1
result_index = -1

while left<=right:
    m=(left+right)//2
    if A[m]==X:
        result_index=m
        left=m+1
    elif A[m]<X:
        left= m+1
    else:
        right=m-1
if result_index!=-1:
    print(result_index+1)
else:
    print("NO")