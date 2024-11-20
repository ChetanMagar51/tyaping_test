import random
from flask import Flask, render_template, request



app = Flask(__name__)

# Route for the Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for Typing Test Page
@app.route('/setting')
def typing_setting():
    return render_template('setting.html')

# Route for typing tes page
@app.route('/typing_test', methods=['GET'])
def typing_test():
    # time = request.args.get('time')
    time = int(request.args.get('time', 60))
    # difficulty = request.args.get('difficulty')
    difficulty = request.args.get('difficulty', 'easy')
    texts = {
        'easy': [
            "The quick brown fox jumps over the lazy dog. Practice makes perfect.",
            "Typing is fun and helps improve productivity. The more you practice, the better you become."
        ],
        'medium': [
            "Typing tests are excellent for improving typing speed and accuracy. Try to focus on both.",
            "Advanced typing techniques can help you increase your typing speed significantly over time."
        ],
        'hard': [
            "Sophisticated algorithms are often used to measure typing speed. It is essential to maintain accuracy under pressure.",
            "Mastering touch typing is a skill that benefits everyone, from programmers to writers."
        ]
    }
    selected_text = random.choice(texts[difficulty])
    return render_template('typing_test.html',text=selected_text, time=time, difficulty=difficulty)


@app.route('/result')
def result():
    wpm = request.args.get('wpm', 0)
    accuracy = request.args.get('accuracy', 0)
    return render_template('result.html', wpm=wpm, accuracy=accuracy)


# Route for Typing Practice Page
@app.route('/practice')
def typing_practice():
    return render_template('practice.html')

# Route for Tricky Keys Page
@app.route('/tricky_keys')
def tricky_keys():
    return render_template('tricky_keys.html')

# Route for Typing Lessons Page
@app.route('/lessons')
def typing_lessons():
    return render_template('lessons.html')





#
# texts = {
#     'easy': [
#         "The quick brown fox jumps over the lazy dog. Practice makes perfect.",
#         "Typing is fun and helps improve productivity. The more you practice, the better you become."
#     ],
#     'medium': [
#         "Typing tests are excellent for improving typing speed and accuracy. Try to focus on both.",
#         "Advanced typing techniques can help you increase your typing speed significantly over time."
#     ],
#     'hard': [
#         "Sophisticated algorithms are often used to measure typing speed. It is essential to maintain accuracy under pressure.",
#         "Mastering touch typing is a skill that benefits everyone, from programmers to writers."
#     ]
# }


if __name__ == '__main__':
    app.run(debug=True)
