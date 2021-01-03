# for loop sample
number_a=[1,2,3,4,5]
for cell in number_a:
    cell=cell*5
    print(cell)

# for loop and if statement

fruit_name=["banana","apple","orange"]
for fruit_items in fruit_name:
    if fruit_items== "orange":
        print(fruit_items)
        break

# string character in loop statement
fruit="banana"
for fruit_character in fruit:
    if fruit_character == "n":
        print(fruit_character)
        break



# range()

for x in range(6):
    print(x)

# range() start and end points

for x in range(3,12,7):
    print(x)

    # For loops advanced examples

    """" Guideliness for bonues

    1) I want you to build a formula for bonuses
    2) Employees are placed in cells by their work ethic
    3) give each employee a bonus which will be based on his place in the list, multiply it by 100 (bonus = place * 100)
    4) The boss said to give bonus by jumping +3 each time in the list
    5) The boss said the the first employee (cell index 0) does not deserve any bonus

    """

    salary = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

    for place in range(0, 9, 3):
        if place == 0:
            pass

        else:
            salary_with_bonus = salary[place] + place * 1000
            print(salary_with_bonus)




# For loop practice

"""
Assignment Rules :
1) Businesses with gross  incomes in between 1 - 2k will pay 5% tax.

2) Businesses with gross  incomes in between 2k - 5k will pay 10% tax.

3) Businesses with gross incomes in between 5k - 15k will pay 15% tax.

4) Above 15k , will all pay 17% tax from gross income.

5) All businesses will pay an additional 2% for healthcare out of
net income as well, after tax reduction, and just print it.

6) Also calculate the total tax you got from the given 10 business in the list (exclude healthcare)

7)businesses_list = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10 , 15001]

"""

# Create a list of businesses
businesses_list = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10 , 15001]
total_taxes = 0



for single_income in businesses_list:
    if single_income>=1 or single_income<=2000:
        tax = single_income * 0.05

    elif single_income>=2001 and single_income<=5000:
        tax = single_income * 0.1

    elif single_income>=5001 and single_income<=15000:
        tax = single_income * 0.15

    else:
        tax = single_income * 0.17

    net_income = single_income - tax
    income_after_healthcare_reduction = net_income * 0.98

    print("Print of the 'tax' variable : " +str(tax))
    print("Printing income after healthcare reduction : " +str(income_after_healthcare_reduction))
    print("\n")

    total_taxes = total_taxes + tax

print("Print the total of taxes : " +str(total_taxes))






