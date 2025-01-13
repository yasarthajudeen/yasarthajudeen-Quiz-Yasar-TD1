from flask import Flask, render_template, request

app = Flask(__name__)

# List of questions and options
questions = [
    {
        "question": "What is the output of the following Python code?\n```python\nprint(2 + 3 * 5)\n```",
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
        "options": ["/", "//", "%", "**"],
        "answer": "/"
    },
    {
        "question": "What will be the output of the following Python code?\n```python\nx = 10\ny = 5\nprint(x // y)\n```",
        "options": ["2.0", "2", "15", "50"],
        "answer": "2"
    },
    {
        "question": "How do you create a dictionary in Python?",
        "options": ["{}", "[]", "()", "<>"],
        "answer": "{}"
    },
    {
        "question": "What will be the output of the following code?\n```python\na = \"Hello\"\nb = \"World\"\nprint(a + b)\n```",
        "options": ["Hello World", "Hello+World", "HelloWorld", "Error"],
        "answer": "HelloWorld"
    },
    {
        "question": "Which of the following is used to check if a condition is true in Python?",
        "options": ["if condition:", "check condition:", "condition check:", "when condition:"],
        "answer": "if condition:"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        # Get the user's answers from the form
        user_answers = request.form.to_dict()
        score = 0
        
        # Calculate the score
        for question, answer in user_answers.items():
            question_index = int(question.split('_')[1])  # Extract the question index
            if answer == questions[question_index]['answer']:
                score += 1
        
        return render_template("result.html", score=score, total=len(questions))
    
    # Add the index manually to each question
    questions_with_index = [{"index": i, "question": q} for i, q in enumerate(questions)]
    
    return render_template("index.html", questions=questions_with_index)

if __name__ == "__main__":
    app.run(debug=True)
