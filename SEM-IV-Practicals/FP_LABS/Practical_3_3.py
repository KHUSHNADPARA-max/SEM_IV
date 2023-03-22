import time

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": 1
    },
    {
        "question": "What is the currency used in Japan?",
        "options": ["Yen", "Dollar", "Euro", "Pound"],
        "answer": 0
    },
    {
        "question": "What is the highest mountain peak in the world?",
        "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
        "answer": 0
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["Saharan Desert", "Arabian Desert", "Gobi Desert", "Kalahari Desert"],
        "answer": 0
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["Nile", "Amazon", "Yangtze", "Yellow"],
        "answer": 0
    }
]


def take_quiz():
    start_time = time.time()
    score = 0
    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{j + 1}. {option}")
        answer = int(input("Enter Your Answer: "))
        if answer == question['answer'] + 1:
            score += 1
            print("Correct!\n")
        else:
            print(
                f"Incorrect. The correct answer is {question['options'][question['answer']]}.\n")
    end_time = time.time()
    print(f"You scored {score} out of {len(questions)}")
    print(f"Time spent: {end_time - start_time:.2f} seconds")


take_quiz()
