print("Once upon a time...")

class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        while story_node.choices:
            print(story_node.story_piece)
            for i , (choice, _) in enumerate(story_node.choices):
                print(f"{i + 1}: {choice}")

            choice= int(input("Enter your choice (1, 2)"))

            valid_choices = ['1', '2']

            if choice not in valid_choices:
                print("please enter a valid choice, 1 or 2")
            else:
                chosen_index = int(choice) -1
                chosen_choice, chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child

        print(story_node.story_piece)








story_root = TreeNode("""You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you:
1 ) Roar back!
2 ) Run to the left...""")


choice_a = TreeNode(
"""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""
)
choice_b = TreeNode(
"""
You come across a clearing full of flowers.
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""
)
story_root.add_child(choice_a)

story_root.add_child(choice_b)
print(story_root.story_piece)
user_choice = input("What is your name?")
print(user_choice)


print(story_root.traverse())
