motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Using the append() method

# motorcycles.append('ducati')
# print(motorcycles)

motorcycles2 = []

motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')

# print(motorcycles2)

# Using the insert() method

motorcycles2.insert(0,'royal enfield')

print(motorcycles2)

# Using the del statement

#del motorcycles2[0]
#print(motorcycles2)
#del motorcycles2[1]
#print(motorcycles2)

# Using the pop() method

# popped_motorcycle = motorcycles2.pop()
# print(motorcycles2)
# print(popped_motorcycle)

#last_owned = motorcycles.pop()
#print(f"The last motorcycle I owned was a {last_owned.title()}.")

#first_owned = motorcycles.pop(0)
#print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Using the .remove method

#print(motorcycles)
#motorcycles.remove('ducati')
#print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
