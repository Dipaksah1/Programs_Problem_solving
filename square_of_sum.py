print("Application to find value of Difference between Square of sum and Sum of square")

num=int(input("Enter a number : "))
sum_of_square=0
square_of_sum=0

#making loop for squaring of sum  
for x in range(1,num+1):
    sum_of_square=(x*x)+sum_of_square


#making loop for sum of given n numbers
for y in range(1,num+1):
    square_of_sum=y+square_of_sum



square_of_sum=square_of_sum*square_of_sum


print()
print("Difference between Square of sum and Sum of square:")
print(square_of_sum-sum_of_square)

input()
