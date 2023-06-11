from stack import Stack

print('I am going to play Towers of Hanoi in python')

# create stack

stacks = []

left_stack = Stack('Left')

middle_stack = Stack('Middle')

right_stack = Stack('Right')

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# going to set up the game here

nums_disks = int(input('\nHow many disks do you want to play with? \n'))

while nums_disks >= 3:
    nums_disks = int(input("Enter a number greater than or equal to 3\n"))
