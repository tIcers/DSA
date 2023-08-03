from stack import Stack

print('\nTowaers of Hanoi!!')

#creating stacks

stacks = []

left_stack = Stack('Left')
right_stack = Stack('Right')
middle_stack = Stack('Middle')

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

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

# Getting User input

def get_input():

    choices = [stack.get_name()[0] for stack in stacks]

    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f'Enter {letter} for {name}')

        user_input = input('')

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

# playing the game

num_user_moves = 0

while right_stack.get_size() != num_disks:
    print('\n\n\n...Current Stacks...')
    for stack in stacks:
        stack.print_items()
    while True:
        print('\nWhich stack do you want to move from?\n')
        from_stack = get_input()
        print('\nWhich stack do you want tot move to?\n')
        to_stack = get_input()
        if from_stack.is_empty():
            print('\n\nInvalid Move.Try Again')
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print('\n\nInvalid Move. Try Again')
    print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")

