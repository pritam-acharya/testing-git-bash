import random
films = []
n = int(input("Please enter the number of films:"))
for i in range(0, n):
    films.append(input(" "))
film2watch = random.choice(films)
print(f"I think you should watch {film2watch}.")