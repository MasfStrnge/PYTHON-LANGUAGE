# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in
# your list.

guests = ['kurt cobain','alan turing','marie curie']

message = "I would like to invite you for dinner"

print(f"{message}, {guests[0].title()}.")
print(f"{message}, {guests[1].title()}.")
print(f"{message}, {guests[2].title()}.\n")

print(f"Unfortunaly, {guests[1].title()} won't be able to make it.\n")

guests[1] = 'James scholz'

print(f"{message}, {guests[0].title()}.")
print(f"{message}, {guests[1].title()}.")
print(f"{message}, {guests[2].title()}.")



