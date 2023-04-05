import random

top_of_range = input("please write a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please write number greater than 0.")
        quit()
else:
    print("please write a number next time")
    quit()

random_number = random.randint(0 , top_of_range)

print(random_number)
