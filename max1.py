A = [1, 3, 5, 7, 2, 4, 6, 8]

max = A[0]
for i in range(1, len(A)):
    if A[i] > max:
        max = A[i]

print(max)
