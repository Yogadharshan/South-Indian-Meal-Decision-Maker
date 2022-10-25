#South Indian Meal Decision Maker

"""
It gets the input from the user to predict what to cook whether 
in lunch or (breakfast or dinner)
"""
import random as rm

food = int(input("Enter-1 to predict for breakfast or dinner\
    \nEnter-2 to predict for lunch\
        \nEnter-3 to add any new recipes\nType 1 or 2 or 3:"))
break_and_dinner_foods =  ["Dosa","Idly","Chappathi","Noodle"]
lunch_foods = ['Turmeric Rice']
side_dish_lunch = ["Fried Potatoes"]
chutney =["Tomato Chutney"]
food_list1 = break_and_dinner_foods

def random_element(x):
    a = rm.randint(0 , len(x)-1)
    return a

#A loop to process the given inputs
if food == 3:
    no_of_recipes = int(input("Enter no. of recipes you are going to enter:"))
    for i in range(no_of_recipes):
        lunch_or_break = int(input("Enter 1 for lunch recipe or\
            \nEnter-2 for breakfast or dinner:\n Type 1 or 2:"))
        if lunch_or_break == 1:
            side_dish = input("Enter a side dish for lunch:")
            side_dish_lunch.append(side_dish)
            lunch_dish = input("Enter lunch:")
            lunch_foods.append(lunch_dish)        
        elif lunch_or_break == 2:
            chutney_input = input("Enter Chutney:")
            chutney.append(chutney_input)
        else:
            print("Invalild number, You have typo.")
    print("Thank you! for giving us recipes")
elif food == 2:
    print("The recipe you can prepare for now is\
        ",lunch_foods[random_element(lunch_foods)],"with",side_dish_lunch[random_element(side_dish_lunch)])
elif food == 1:
    print("The recipe you can prepare for now is",\
        break_and_dinner_foods[random_element(break_and_dinner_foods)],\
            "with",chutney[random_element(chutney)])
else:
    print("Invalid input, You have a typo")