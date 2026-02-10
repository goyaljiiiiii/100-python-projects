# List of questions and their options
questions = [
    {
        "question": 'What does "HTTP" stand for in web browsing?',
        "options": {
            'a': "HyperText Transfer Protocol",
            'b': "HyperText Technical Processor",
            'c': "High-Tech Transfer Protocol",
            'd': "HyperText Transport Program"
        },
        "correct_answer": 'a'
    },
    {
        "question": 'Which programming language is known for its snake logo and is popular for data science?',
        "options": {
            'a': "JavaScript",
            'b': "Python",
            'c': "Ruby",
            'd': "C++"
        },
        "correct_answer": 'b'
    },
    {
        "question": 'Who is known as the father of the computer?',
        "options": {
            'a': "Alan Turing",
            'b': "Bill Gates",
            'c': "Charles Babbage",
            'd': "Steve Jobs"
        },
        "correct_answer": 'c'
    },
    {
        "question": 'Which operating system is developed by Microsoft?',
        "options": {
            'a': "Linux",
            'b': "Windows",
            'c': "macOS",
            'd': "Android"
        },
        "correct_answer": 'b'
    },
    {
        "question": 'What does "URL" stand for in a website address?',
        "options": {
            'a': "Universal Resource Locator",
            'b': "Uniform Resource Locator",
            'c': "Universal Registered Locator",
            'd': "Uniform Registered Locator"
        },
        "correct_answer": 'b'
    },
    {
        "question": 'What part of the computer is referred to as the "brain" of the computer?',
        "options": {
            'a': "RAM",
            'b': "Hard Drive",
            'c': "CPU",
            'd': "GPU"
        },
        "correct_answer": 'c'
    },
    {
        "question": 'Who co-founded Apple Inc. along with Steve Jobs?',
        "options": {
            'a': "Steve Wozniak",
            'b': "Mark Zuckerberg",
            'c': "Bill Gates",
            'd': "Tim Cook"
        },
        "correct_answer": 'a'
    },
    {
        "question": 'Which software is commonly used for creating presentations?',
        "options": {
            'a': "Microsoft Word",
            'b': "Microsoft Excel",
            'c': "Microsoft PowerPoint",
            'd': "Adobe Photoshop"
        },
        "correct_answer": 'c'
    },
    {
        "question": 'What do we call the main circuit board in a computer?',
        "options": {
            'a': "Hard Drive",
            'b': "RAM",
            'c': "Motherboard",
            'd': "Processor"
        },
        "correct_answer": 'c'
    },
    {
        "question": 'What was the name of the first video game ever created?',
        "options": {
            'a': "Pac-Man",
            'b': "Pong",
            'c': "Super Mario",
            'd': "Space Invaders"
        },
        "correct_answer": 'b'
    }
]

# Loop through all the questions
for q in questions:
    # Display question and options
    print(q["question"])
    for option, answer in q["options"].items():
        print(f"{option}: {answer}")
    
    # Get user's answer
    user_answer = input("Enter your answer (a, b, c, or d): ").lower()
    
    # Check if the user's answer is correct
    if user_answer == q["correct_answer"]:
        print("Correct! You got it right.")
    else:
        print(f"Incorrect. The correct answer was '{q['correct_answer']}': {q['options'][q['correct_answer']]}")
    
    print()  