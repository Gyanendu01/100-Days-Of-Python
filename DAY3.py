#  Day 3 Challenge
# The Ultimate Wacky Recipe Maker

# We have learned enough skills for a simple, but cool, project!

# Remember when you were a kid and thought the ideal dinner would just be all your favorite things mixed in a bowl? How did that Nutella Mac & Cheese taste? Well - let's come up with a recipe generator to build us an amazing dish for today's evening meal!

# You will need to:

#     Create these as a variable:
#         A type of food
#         A type of plant
#         A method of cooking
#         A word to describe burned food
#         A household item

# 2. Output a nice looking Recipe page that *concatenates* a dish in this format:

#     cooking food with burned plant on a bed of item
# =============================================================================== code ========================================================================

food = input("Name a food: ")
plant = input("Name a plant: ")
method_cooking = input("Name a method of cooking: ")
random_word = input("What word describes burned food? ")
DIY_ITEM = input("Name a DIY item: ")
DIY_ITEM2 = input("Name a 2nd DIY items: ")
bad_food = input("Enter a dish which you hate: ")

print("\n\nMENU")
print("STARTER COURSE")
print(f"{food} with {method_cooking} {plant} on a bed {DIY_ITEM}")
print("\nMAIN COURSE")
print(f"{food} with {method_cooking} {plant} on a bed {DIY_ITEM2}")
print("\nDINNER COURSE")
print(f"{bad_food} with {method_cooking} {plant} on a bed {DIY_ITEM}")
