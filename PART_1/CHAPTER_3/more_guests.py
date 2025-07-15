# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
#  • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
#    end of your program, informing people that you found a bigger table.
#  • Use insert() to add one new guest to the beginning of your list.
#  • Use insert() to add one new guest to the middle of your list.
#  • Use append() to add one new guest to the end of your list.
#  • Print a new set of invitation messages, one for each person in your list.

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