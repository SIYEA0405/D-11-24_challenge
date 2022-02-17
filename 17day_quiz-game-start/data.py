from question_model import Question

question_data = [
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The logo for Snapchat is a Bell.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "RAM stands for Random Access Memory.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Ada Lovelace is often considered the first computer programmer.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Windows ME operating system was released in the year 2000.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers",
     "type": "boolean", "difficulty": "easy",
     "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
     "correct_answer": "True",
     "incorrect_answers": ["False"]}]

question_bank = []

for i in question_data:
    question_question = i["question"]
    question_answer = i["correct_answer"]
    question_dic = Question(question_question, question_answer)
    question_bank.append(question_dic)
