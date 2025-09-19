end = 100

sum_of_squares = 0
for i in range(end+1):
    sum_of_squares = sum_of_squares + (i**2)

square_of_sum = (int((1+end)*end/2))**2

answer = square_of_sum - sum_of_squares

print(answer)


#Time Complexity O(n^2) (n=end)
#Space Complexity O(1)