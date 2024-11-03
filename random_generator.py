import random

def get_valid_input(prompt, input_type=int):
    """Helper function to get and validate user input"""
    while True:
        try:
            value = input_type(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def generate_random_number(min_num, max_num):
    """Generate a random number between min_num and max_num"""
    return random.randint(min_num, max_num)

def main():
    print("Welcome to the Random Number Generator!")
    
    # Get minimum number
    min_num = get_valid_input("Enter the minimum number: ")
    
    # Get maximum number
    while True:
        max_num = get_valid_input("Enter the maximum number: ")
        if max_num > min_num:
            break
        print(f"Maximum number must be greater than {min_num}")
    
    # Generate and display the random number
    result = generate_random_number(min_num, max_num)
    print(f"\nYour random number between {min_num} and {max_num} is: {result}")
    
    # Ask if user wants to generate another number
    while input("\nWould you like to generate another number? (y/n): ").lower() == 'y':
        result = generate_random_number(min_num, max_num)
        print(f"\nYour random number between {min_num} and {max_num} is: {result}")

if __name__ == "__main__":
    main()
