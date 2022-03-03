num1=int(input('enter a number:'))
num2=int(input('enter a number:'))
opr=input('enter the operator')
if opr=='+':
    print(num1+num2)
elif opr=='-':
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)
elif opr=='*':
    print(num1*num2)
elif opr=='/':
    print(num1/num2)
else:
    print('invalid')

