import random

# rules-------------------------
RULES = {
    "rock": ["scissors", "fire"],
    "scissors": ["paper", "water"],
    "paper": ["rock", "fire"]
}


def load_rating(username):
    """
    Load user's rating from rating.txt
    """
    try:
        with open("rating.txt", "r", encoding="utf-8") as file:  # open UTF-8
            for line in file:
                name, score = line.strip().split()
                if name.strip().lower() == username.strip().lower():  # compare in lower case
                    return int(score)
    except FileNotFoundError:  # if rating not found - -0 score
        pass
    return 0  # if name not found - 0 score


# ----------------------------------
def get_result(user_move, computer_move, rules):
    """
    return game result
    user_move -  user choice
    computer_move - comp choice
    return - game result
    """
    if user_move == computer_move:
        return f"Its draw ({computer_move})", "draw"

    if computer_move in rules[user_move]:  # if comp lose
        return f"Computer chose {computer_move} and comp lose", "win"
    else:  # if comp win
        return f"Computer chose {computer_move} and comp win", "lose"


# -------------------------------------------------------------------------------

def generate_custom_rules(symbols):
    """
    Generate rules for user symbols
    left half list - win, the right half lose
    """
    rules = {}
    total_symbols = len(symbols)

    for i, symbol in enumerate(symbols):
        # Left part of the list win this symbol
        left_part = symbols[i + 1: i + 1 + total_symbols // 2]
        # Right part loses to this symbol
        right_part = [s for s in symbols if s not in left_part and s != symbol]

        rules[symbol] = left_part

    return rules


def main():
    """
    Main func
    """
    # input player's name
    username = input("Enter your name: ").strip()
    print(f"Hello, {username}")

    # Load user rating
    score = load_rating(username)

    options = []  # initalisation options
    rules = {}  # initialization rules

    # Menu
    while True:
        print("\n--- Main Menu ---")
        print("1. View rating")
        print("2. Play classic game (rock, paper, scissors)")
        print("3. Play extended game (user symbols)")
        print("4. Play with custom symbols")  # custom symbols
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print(f"Your rating: {score}")
            continue  # return to menu option - not change
        elif choice == "2":
            options = ["rock", "paper", "scissors"]  # Classic
            rules = RULES  # Use usr rules
        elif choice == "3":
            # Check if user symbols are already defined
            if not options or options == ["rock", "paper", "scissors"]: #check - if == user not enter sybm. if != - user enter symb
                print("Please enter user custom symbols first")
                continue  # Return to menu

            rules = generate_custom_rules(options)  # Generate rules for user symbols
            print("\nUse user symbols:", ", ".join(options))  # show user symbols
        elif choice == "4":  # User symb
            while True:
                custom_symbols = input("Enter your custom symbols (separated with , ): ").strip().split(",")
                # Convert all symbols to lowercase and remove extra spaces
                custom_symbols = [s.strip().lower() for s in custom_symbols if s.strip()]

                if len(custom_symbols) < 3:  # List must have 3+ elements
                    print("You must enter >3 symbols.")
                    continue
                if len(custom_symbols) % 2 == 0:  # List size must be not even
                    print("Enter odd number")
                    continue

                options = custom_symbols
                rules = generate_custom_rules(custom_symbols)
                print("\nCustom symbols saved:", ", ".join(options))  # show saved symbols
                break
        elif choice == "5":
            print("Bye!")
            break  # exit
        else:
            print("Invalid choice, try again")
            continue  # check choice

        print("\nAvailable options:", ", ".join(options))
        print("Type '!rating' to view your score or '!exit' to quit the game.")

        while True:
            user_input = input("Your move: ").strip().lower()

            if user_input == "!exit":  # exit
                print("Returning to main menu...")
                break
            elif user_input == "!rating":  # show rating
                print(f"Your rating: {score}")
            elif user_input in options:  # if correct input
                computer_choice = random.choice(options)  # comp random
                result, outcome = get_result(user_input, computer_choice, rules)  # Get result and outcome
                print(result)

                # Update rating
                if outcome == "draw":
                    score += 50
                elif outcome == "win":
                    score += 100
            else:
                print("Invalid input. Please choose from:", ", ".join(options))


# Game run
if __name__ == "__main__":
    main()