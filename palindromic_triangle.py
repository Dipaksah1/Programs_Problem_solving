print("Application for printing Palindromic triangle of size")
print()
print()

Num=int(input("Enter a size of Palindromic triangle : "))

#looping for arranging in palindromic ways using string method
for i in range(1,Num+1):
    print(int(str(1)*i)*int(str(1)*i))

input()
