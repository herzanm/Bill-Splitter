# write your code here
import random

# write your code here
number_of_people = int(input("Enter the number of friends joining (including you):"))
list_of_people = {}
if number_of_people < 1:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(number_of_people):
        list_of_people[input()] = 0
    total_bill = float(input("Enter the total bill value:"))
    equal_split = round(total_bill / number_of_people, 2)
    for i in list_of_people:
        list_of_people[i] = equal_split
    print(list_of_people)
    print()
    lucky_choice = input("""Do you want to use the "Who is lucky?" feature? Write Yes/No:""")
    if lucky_choice == 'Yes':
        lucky_person = random.choice(list(list_of_people.keys()))
        print(f"\n{lucky_person} is the lucky one!")
        equal_split = round(total_bill / (number_of_people - 1), 2)
        for i in list_of_people:
            if i != lucky_person:
                list_of_people[i] = equal_split
            else:
                list_of_people[i] = 0
        print(f"\n{list_of_people}")

    else:
        print("\nNo one is going to be lucky")
        print(f"\n{list_of_people}")
