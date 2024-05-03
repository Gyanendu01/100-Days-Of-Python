# # Day 4 Challenge

#  1.Ask your users to list a bunch of information about them: things they like, things they hate, names of family and friends... it's up to you how many and what kinds of things you pick. Keep it wacky!

# 2. Now construct your story - it can be about anything you want, but must use the variables you've created in step 1.

#  3.Make sure to only work one paragraph at a time. Otherwise things could get a bit messy
# ====================================================================  code ======================================================

NAME = input("Enter your Name: ")
AGE = int(input("Enter your age: "))
fav_food = input("Enter your favourite food: ")
fav_place = input("Enter your favourite place where you like to sit and chill: ")

friend_name = "Alex"
friend_age = 25
friend_food = "pizza"
friend_place = "beach"

print("\nOnce upon a time, there was a person named " + NAME + " who was " + str(AGE) + " years old. " + NAME +
      " loved to eat " + fav_food + " and often dreamed of enjoying it at " + fav_place + ".")

print("\nOne day, " + NAME + " decided to invite their friend, " + friend_name + ", over for dinner. " + friend_name +
      " was " + str(friend_age) + " years old and had a passion for " + friend_food + ". " + NAME + " suggested they "
      "eat at their favorite place, " + fav_place + ".")

print("\nExcitedly, they both headed to the " + fav_place + ". As they enjoyed their meal, they reminisced about "
      "their fondest memories together and laughed at old jokes.")

print("\nAfter dinner, they took a stroll along the beach, chatting about life and watching the sunset. It was a "
      "perfect evening, filled with good food, great company, and the serenity of their favorite place.")

print("\nAs the night grew darker, they bid farewell, promising to meet again soon for another memorable "
      "adventure at their beloved spot, " + fav_place + ".")
