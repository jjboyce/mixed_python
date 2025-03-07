person1 = "you"
person1age = int(input(f'How old are {person1}?'))
person2 = input("what is the name of the potential?")
person2age = int(input(f'How old is {person2}?'))

p2_older_than_p1 = person2age > person1age
minimum_age = (person1age / 2) + 7
maximum_age = (person1age - 7) * 2

print(f'The minimum age is {minimum_age} and the maximum age is {maximum_age}\n')

if person2age < minimum_age:
    print(f'{person2} is too young. Look again. ')

elif person2age > maximum_age:
    print(f'{person2} is too old! Keep looking!!')

else:
    print("Meh, they'll do.")
