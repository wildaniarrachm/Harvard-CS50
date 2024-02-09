## this input function will always returns a string
## you have to specify the data type you want to input

n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")