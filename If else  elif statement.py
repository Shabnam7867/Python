#if else statement sample example

x = 4
if x > 5 :
    print("yes")
else:
    print("no")


age=35
if age>50:
    print("you are senior developer")
elif age>40:
    print("mid level developer")
elif age>38:
    print("younger developer")
else:
    print("doesn't matter the age")

# 'if' statement practice

# 1 - Create an employee dictionary
employees = {
    "Jack": 6,
    "Russel": 10,
    "Keren": 2}


# 2 - Find an employee for 5-8 workings hours, use 'elif'
if employees["Jack"]>=5 or employees["Jack"]<=8:
    print("Boss, we should call Jack")
elif employees["Russel"]>=5 or employees["Russel"]<=8:
    print("Russel is our guy")
elif employees["Keren"]>=5 or employees["Keren"]<=8:
    print("Keren is the one")
else:
    print("No one fits the job")

# 3 - Find someone to work the weekend. Also check if its keren in a 'nested if'
if employees["Jack"]==2 or employees["Jack"]==3:
    print("Boss, we should call Jack")
elif employees["Russel"]==2 or employees["Russel"]==3:
    print("Russel is our guy")
elif employees["Keren"]==2 or employees["Keren"]==3:
    if employees["Keren"]==2:
        pass
    elif employees["Keren"]==3:
        pass
    elif employees["Keren"]==4:
        pass

    else:
        print("Default exist point - nested else")
else:
    print("No one fits the job")