num=int(input("Enter a number: ")) #input from the user.
digit=0.
while(num>0):
    digit=num%10
    num=num//10
    print(digit,end="")
