# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.
#  • Start with your program from Exercise 3-6. Add a new line that prints a
#  message saying that you can invite only two people for dinner.
#  • Use pop() to remove guests from your list one at a time until only two
#  names remain in your list. Each time you pop a name from your list, print a
#  message to that person letting them know you’re sorry you can’t invite them
#  to dinner.
#  • Print a message to each of the two people still on your list, letting them
#  know they’re still invited.
#  • Use del to remove the last two names from your list, so you have an empty
#  list. Print your list to make sure you actually have an empty list at the end of
#  your program.

guests = ['kurt cobain','alan turing','marie curie']

message = "I would like to invite you for dinner"

print(f"{message}, {guests[0].title()}.")
print(f"{message}, {guests[1].title()}.")
print(f"{message}, {guests[2].title()}.\n")

print(f"Unfortunaly, {guests[1].title()} won't be able to make it.\n")

guests[1] = 'james scholz'

print(f"{message}, {guests[0].title()}.")
print(f"{message}, {guests[1].title()}.")
print(f"{message}, {guests[2].title()}.\n")

print("Hey guys, I just found a bigger dinner table!\n")

guests.insert(0,'lord byron')
guests.insert(1,'paul artreides')
guests.append('mary shelly - the GOAT')

print(f"{message}, {guests[0].title()}.")
print(f"{message}, {guests[1].title()}.")
print(f"{message}, {guests[2].title()}.")
print(f"{message}, {guests[3].title()}.")
print(f"{message}, {guests[4].title()}.")
print(f"{message}, {guests[5].title()}.\n")

print("Just found out I'm ")