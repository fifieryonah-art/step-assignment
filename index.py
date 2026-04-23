thomas_age = 3
age_at_kindergarten = 5
print(thomas_age == age_at_kindergarten)


def school_age_calculator(age,name):
    if age < 5:
        print("Enjoy the time!", name, "is only", age)
    elif age == 5:
        print("Enjoy Kindergarten,", name)
    else:
        print("They grow up so fast")

school_age_calculator(3,"Peace")
school_age_calculator(5,"Patience")
school_age_calculator(10,"Tina")


# Returning a value from a function
def add_ten_to_age(age):
    new_age = age + 10
    return new_age

how_old_will_I_be = add_ten_to_age(3)
print(how_old_will_I_be)

# Loops
# While loop
x=0
while(x<5):
    print(x)
    x=x+1

#for loop
print("_________________")
for x in range(5,10):
    print(x)

days = ("monday", "Tue", "Wed", "thursday", "fri", "sat", "sunday")
for d in days:
    print(d)


days = ("monday", "Tue", "Wed", "thursday", "fri", "sat", "sunday")
for d in days:
    if(d=="thursday"):break
    print(d)

print("___________")
days = ("monday", "Tue", "Wed", "thursday", "fri", "sat", "sunday")
for d in days:
    if(d=="thursday"):continue
    print(d)