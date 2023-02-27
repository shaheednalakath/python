# li=[]
# num=int(input("enter start"))
# num2=int(input("enter se number"))
# while num<=num2:
#     for i in range(1,num):
#         if i*i==num:
#             res=num
#             li.append(res)
#     num=num+1
#
# print(li)
# for num in li:
#     temp=num
#     while(temp!=0):
#         r=temp %10
#         if(r%2==0):
#             res=temp
#             print(res)
#         else:
#             flag=-1
#         temp=temp//10
#
# # n=1030
# # while(n != 0):
# #     r=n % 10
# #     print(r)
# #     n=n//10
# def calleven(num):
#     temp = num
#     while (temp != 0):
#         r = temp % 10
#         if (r % 2 == 0):
#             res = temp
#             print(res)
# #         temp = temp // 10




# def calleven(n):
#     if (n//100)%2==0 and (n//10)%2==0 and (n//1000) % 2 == 0:
#         print(n)
#
# num=int(input("enter start"))
# num2=int(input("enter se number"))
# while num<=num2:
#     for i in range(1,num):
#         if i*i==num:
#             res=num
#             while(res !=0):
#                 res=res%10
#                 if res % 2==0 :
#                     calleven(num)
#                 res=res//10
#
#     num=num+1

# def calleven(n):
#     if((n//10)%2==0 and (n//100)%2==0 and (n//1000)%2==0):
#         print(n)
#
# num1=int(input("enter a number"))
# num2=int(input("enter a number"))
# while(num1<=num2):
#     for i in range(1,num1):
#         if i*i == num1:
#             res=num1
#             while(res !=0):
#                 res=res%10
#                 if res %2==0:
#                     calleven(num1)
#                 res=res//10
#     num1=num1+1
def calleven(n):
    if (n//10)%2==0 :
        if(n//100)%2==0:
           if(n//1000)%2==0:
               print(n)
num1=int(input("enter a number"))
num2=int(input("end"))
while(num1<=num2):
    for i in range(1,num1):
        if i*i==num1:
            res=num1
            while(res != 0):
                res=res%10
                if(res%2==0):
                    calleven(num1)
                res=res//10
    num1=num1+1