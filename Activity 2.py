#Ralfy Keifer T. Cerezo
#8-Camia

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

def calculate_sum():
    global num1, num2
    sum = num1 + num2
    print("The sum of your first number and your second number is", sum)

def calculate_difference():
    global num1, num2
    difference = num1 - num2
    print("The difference of your first number and your second number is", difference)

calculate_sum()
calculate_difference()

