# Mad Libs Game Script

# Function to collect inputs from the user
def collect_words():
    # Prompting the user to provide words based on the given categories
    print("Please provide the following words to complete the Mad Lib story:")
    
    large_object = input("A large object: ")
    large_objects_plural = input("Large objects (plural): ")
    adjective = input("An adjective: ")
    body_part = input("A body part: ")
    restaurant = input("A restaurant: ")
    food1 = input("A food: ")
    food2 = input("Another food: ")

    # Returning a dictionary with all user inputs
    return {
        "large_object": large_object,
        "large_objects_plural": large_objects_plural,
        "adjective": adjective,
        "body_part": body_part,
        "restaurant": restaurant,
        "food1": food1,
        "food2": food2
    }

# Function to generate the story using the collected words
def generate_story(words):
    # Inserting the words into the story template using a formatted string
    story = (
        f"I’ve had a very {words['adjective']} day.\n"
        f"This morning, I dropped a box of {words['large_objects_plural']} on my {words['body_part']}.\n"
        f"Then, at lunch, I went to {words['restaurant']} for their delicious {words['food1']},\n"
        f"But the waiter brought me {words['food2']}, which I was not hungry for.\n"
        f"Finally, on my way home, I was cut off by a van with a large {words['large_object']} strapped to the roof."
    )
    # Returning the completed story
    return story

# Main function to run the Mad Libs game
def mad_libs_game():
    # Collecting words from the user
    user_words = collect_words()
    
    # Generating the story using the user's words
    story = generate_story(user_words)
    
    # Displaying the completed story
    print("\nHere is your Mad Libs story:\n")
    print(story)

# Calling the main function to start the game
mad_libs_game()
