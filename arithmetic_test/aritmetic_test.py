import random

#-------------------
def get_operation():
    """Random operation"""
    return random.choice(['+', '-', '*'])
#---------------------

def generate_task(level):
    """Generation task to difficult level"""
    if level == 1:
        num1, num2 = random.randint(2, 9), random.randint(2, 9)
        operation = get_operation()     #call func
        question = f"{num1} {operation} {num2}"
        answer = eval(question)
    else:
        num1 = random.randint(11, 29)
        question = f"{num1}"
        answer = num1 ** 2
    return question, answer
#---------------------------------------

def get_valid_input():
    """Check input value"""
    while True:
        user_input = input("> ").strip() #del space
        if user_input.lstrip('-').isdigit(): #del -, check num
            return int(user_input)
        print("Incorrect input")
#---------------------------------------

def arithmetic_test():
    """Main test"""
    print("Enter a number difficult level:")
    print("1 - simple, with num. 2-9")
    print("2 - high level num. 11-29")

    while True:
        level = input("> ").strip()
        if level in ('1', '2'):
            level = int(level)
            break
        print("Incorrect input")

    correct_answers = 0
    for _ in range(5):
        question, correct_answer = generate_task(level)
        print(question)
        user_answer = get_valid_input()
        if user_answer == correct_answer:
            print("Right")
            correct_answers += 1
        else:
            print("Wrong")

#------------
    print(f"Your mark is {correct_answers}/5.")
    save_result(correct_answers, level) # send correct ans in save result as score


def save_result(score, level):
    """Ask user and wright to file"""
    description = "simple operations with numbergits 2-9" if level == 1 else "integral squares of 11-29"
    print("Save the result? Enter yes or no")

    if input("> ").strip().lower() in ('yes', 'y'):
        print("What is your name?")
        name = input("> ").strip()
        with open("results.txt", "a") as file: #-open-----add to file
            file.write(f"{name}: {score}/5 in level {level} ({description}).\n") # format name+
        print("The result saved in \"results.txt\".")


if __name__ == "__main__":
    arithmetic_test()
