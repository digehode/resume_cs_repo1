name="James"
age=18
location="UK"


for age in range(23):

    if location=="UK":
        oldEnough = age >= 18 
    elif location=="USA":
        oldEnough = age >= 21	
    elif location=="SPAIN":
        oldEnough = age >=19
    else:
        oldEnough = False
        print("Assuming you aren't old enough because I don't know where you are")


    if oldEnough:
        print(f"Welcome {name} to the club! You are {age} years old")
    else:
        print(f"I am sorry, at {age} you are not old enough.")


