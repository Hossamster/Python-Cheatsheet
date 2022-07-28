answer = [person[0] for person in ['Elie', 'Tim', 'Matt']]
print(answer)
answer2 = [val for val in [1, 2, 3, 4, 5, 6] if val % 2 == 0]
print(answer2)

answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
print(answer)
answer2 = [val[::-1].lower() for val in ['Hossam', 'Manar', 'Jana']]
print(answer2)

answer = [char for char in "amazing" if char not in "aeiou"]
print(answer)
