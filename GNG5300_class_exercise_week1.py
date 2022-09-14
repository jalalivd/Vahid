#multiply two numbers

def Multiplynumber(first, second):
    total_product = first * second
    return total_product

number_one = int(input("Please enter first number :"));
number_two = float(input("Please enter second number :"));

print("The sum of your numbers is", Multiplynumber(number_one, number_two))