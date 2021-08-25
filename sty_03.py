num1=int(input())
num2=input()

# print((num1*(num2%10)))
# print((num1*((num2%100)-(num2%10)))//10)
# print(num1*(num2//100))
# print(num1*num2)

lst=list(num2)
for i in reversed(lst):
    print(num1*int(i))
print(num1*int(num2))