# Importing the random module to use the randint function
import random

# Function to generate PowerBall numbers
def generate_powerball_numbers():
    # Greeting the user
    print("Welcome to the PowerBall number generator!")
    
    # Generating five random numbers between 1 and 69 for white balls
    white_balls = [random.randint(1, 69) for _ in range(5)]
    
    # Generating one random number between 1 and 26 for the red PowerBall
    red_ball = random.randint(1, 26)
    
    # Displaying the generated numbers with appropriate spaces
    white_ball_string = ' '.join(map(str, white_balls))  # Joining the white balls with spaces
    print(f"Your PowerBall numbers are: {white_ball_string}   {red_ball}")
    
    # Farewell message
    print("Good luck with your PowerBall ticket!")

# Calling the function to generate and display PowerBall numbers
generate_powerball_numbers()
