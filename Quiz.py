
questions = [
    {
        'prompt': 'Which keyword is used to define a function in Python?',
        'options': ['A. def', 'B. define', 'C. function', 'D. func'],
        'answer_letter': 'A',
        'answer_text': 'def'
    },
    {
        'prompt': 'What is the correct way to create a list in Python?',
        'options': ['A. my_list = (1, 2, 3)', 'B. my_list = {1, 2, 3}', 'C. my_list = [1, 2, 3] ', 'D. my_list = <1, 2, 3> '],
        'answer_letter': 'C',
        'answer_text': 'my_list = [1, 2, 3]'
    },
    {
        'prompt': 'What does the len() function do?',
        'options': ['A. Returns the number of characters in a string', 'B. Returns the number of items in a list', 'C. Returns the size of a data type', 'D. Both A and B'],
        'answer_letter': 'D',
        'answer_text': 'Both A and B'
    },
    {
        'prompt': 'Which of the following is a correct if statement?',
        'options': ['A. if x = 5:', 'B. if (x == 5)', 'C. if x == 5:', 'D. if x := 5'],
        'answer_letter': 'C',
        'answer_text': 'if x == 5'
    },
    {
        'prompt': 'What does the range(5) function return?',
        'options': ['A. A list of 5 elements', 'B. An iterable from 0 to 4', 'C. A tuple from 1 to 5', 'D. An error'],
        'answer_letter': 'B',
        'answer_text': 'An iterable from 0 to 4'
    },
    {
        'prompt': 'Which of the following is not a valid Python data type?',
        'options': ['A. list', 'B. dict', 'C. array', 'D. tuple'],
        'answer_letter': 'C',
        'answer_text': 'array'
    },
    {
        'prompt': 'What is the purpose of indentation in Python?',
        'options': ['A. To make code faster', 'B. To separate comments', 'C. To define code blocks', 'D. It has no effect'],
        'answer_letter': 'C',
        'answer_text': 'To define code blocks'
    },
    {
        'prompt': 'Which of the following is a valid variable name in Python?',
        'options': ['A. 1variable', 'B. @name', 'C. first_name', 'D. class'],
        'answer_letter': 'C',
        'answer_text': 'first_name'
    },
    {
        'prompt': 'What is the output of print(3 * "abc" ) ?',
        'options': ['A. abcabc', 'B. abcabcabcabc', 'C. abcabcabc', 'D. Error'],
        'answer_letter': 'C',
        'answer_text': 'abcabcabc'
    },
    {
        'prompt': 'How do you add an element to a list in Python?',
        'options': ['A. list.append(element)', 'B. list.add(element)', 'C. list.insert(element)', 'D. list + element'],
        'answer_letter': 'A',
        'answer_text': 'list.append(element)'
    }
    
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n" + question["prompt"])
        for option in question["options"]:
            print(option)

        user_input = input("Enter your answer: \n").strip().upper()

        correct_letter = question["answer_letter"].upper()
        correct_value = question["answer_text"].strip().upper()

        if user_input == correct_letter or user_input == correct_value:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_letter}. {question['answer_text']}\n")

    print(f"\nYou got {score} out of {len(questions)} questions correct.")


    if score >=7:
        print("congrats! \U0001F389 ")

    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again == 'yes':
        run_quiz(questions)
    else:
        print("Thanks for playing! 👋")

run_quiz(questions)
