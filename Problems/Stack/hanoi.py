from stack import Stack

print('\nTowaers of Hanoi!!')

#creating stak

stack = []

left_stack = Stack('Left')
right_stack = Stack('Right')
middle_stack = Stack('Middle')

stack.append(left_stack)
stack.append(right_stack)
stack.append(middle_stack)


# set up game

num_disks = int(input('\nHow many disks do you want to play with?\n'))

while num_disks < 3:
    num_disks = int(input('\nEnter a number greater than or equal to 3:\n'))

# Set up the initial config of the Tower of Hanoi
for i in range(num_disks, 0, -1):
    left_stack.push(i)

# the number of optimal moves is always 2 * number of disks  - 1
num_optimal_moves = (2 ** num_disks)-1
print('\nTHe fastest you can solve this game is in {0} moves'.format(num_optimal_moves))
