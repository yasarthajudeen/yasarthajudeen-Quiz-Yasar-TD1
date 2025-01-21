from flask import Flask, render_template, request

app = Flask(_name_)

# List of questions and options
questions = [
    {
        "question": "What is the output of the following Python code? python print(2 + 3 * 5) ",
        "options": ["25", "17", "15", "10"],
        "answer": "17"
    },
    {
        "question": "Which of the following is the correct syntax to output \"Hello, World!\" in Python?",
        "options": ["print(\"Hello World\")", "echo \"Hello World\"", "printf(\"Hello World\")", "System.out.println(\"Hello World\")"],
        "answer": "print(\"Hello World\")"
    },
    {
        "question": "How do you define a function in Python?",
        "options": ["function my_function():", "def my_function():", "func my_function():", "define my_function():"],
        "answer": "def my_function():"
    },
    {
        "question": "What is the type of the object 3.14 in Python?",
        "options": ["int", "float", "string", "double"],
        "answer": "float"
    },
    {
        "question": "Which of the following is used to create a list in Python?",
        "options": ["[]", "()", "{}", "<>"],
        "answer": "[]"
    },
    {
        "question": "Which operator is used to divide two numbers in Python?",
        "options": ["/", "//", "%", ""],
        "answer": "/"
    },
    {
        "question": "What will be the output of the following Python code?python x = 10 y = 5 print(x // y)",
        "options": ["2.0", "2", "15", "50"],
        "answer": "2"
    },
    {
        "question": "What will be the output of the following code? python a = \"Hello\" b = \"World\" print(a + b) ",
        "options": ["Hello World", "Hello+World", "HelloWorld", "Error"],
        "answer": "HelloWorld"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        # Get the user's answers from the form
        user_answers = request.form.to_dict()
        score = 0
        results = []  # To store results for each question

        # Calculate the score and prepare detailed results
        for question_key, user_answer in user_answers.items():
            question_index = int(question_key.split('_')[1])  # Extract the question index
            correct_answer = questions[question_index]['answer']
            is_correct = user_answer == correct_answer
            if is_correct:
                score += 1

            # Add detailed feedback for this question
            results.append({
                "question": questions[question_index]['question'],
                "user_answer": user_answer,
                "correct_answer": correct_answer,
                "is_correct": is_correct
            })

        return render_template("result.html", score=score, total=len(questions), results=results)

    # Add the index manually to each question for the template
    questions_with_index = [{"index": i, "question": q} for i, q in enumerate(questions)]

    # Debugging: Ensure there are no duplicates
    unique_questions = {q['question']['question'] for q in questions_with_index}
    print(f"Unique Questions (Debug): {unique_questions}")
    print(f"Number of Unique Questions: {len(unique_questions)}")
    print(f"Number of Total Questions: {len(questions_with_index)}")

    return render_template("index.html", questions=questions_with_index)

if _name_ == "_main_":
    app.run(debug=True)