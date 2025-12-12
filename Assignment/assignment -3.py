import random

data = {
    1: {
        'question': 'What is the output of the following?\n\nprint(3 * 2 + 4)',
        'options': ('10', '14', '6', '8'),
        'answer': '10'
    },
    2: {
        'question': 'Which function converts a number to a string?',
        'options': ('int()', 'str()', 'float()', 'chr()'),
        'answer': 'str()'
    },
    3: {
        'question': 'Which of the following is a Python boolean value?',
        'options': ('TRUE', 'true', 'False', '0'),
        'answer': 'False'
    },
    4: {
        'question': 'What is the output?\n\nprint(len([10, 20, 30]))',
        'options': ('2', '3', '30', '1'),
        'answer': '3'
    },
    5: {
        'question': 'Which of these is a tuple?',
        'options': ('[1,2,3]', '{1,2,3}', '(1,2,3)', '<1,2,3>'),
        'answer': '(1,2,3)'
    },
    6: {
        'question': 'What is the output?\n\nprint("Python".startswith("Py"))',
        'options': ('True', 'False', 'None', 'Error'),
        'answer': 'True'
    },
    7: {
        'question': 'Which of the following stores key–value pairs?',
        'options': ('list', 'tuple', 'dictionary', 'set'),
        'answer': 'dictionary'
    },
    8: {
        'question': 'Which operator is used for floor division?',
        'options': ('//', '/', '%', '**'),
        'answer': '//'
    },
    9: {
        'question': 'What does the `input()` function return?',
        'options': ('int', 'float', 'string', 'boolean'),
        'answer': 'string'
    },
    10: {
        'question': 'What is the output?\n\nprint(4 > 2 and 10 < 5)',
        'options': ('True', 'False', 'None', 'Error'),
        'answer': 'False'
    },
    11: {
        'question': 'Which method is used to add an item to a set?',
        'options': ('append()', 'insert()', 'add()', 'push()'),
        'answer': 'add()'
    },
    12: {
        'question': 'Which symbol is used to write a comment in Python?',
        'options': ('//', '#', '/* */', '--'),
        'answer': '#'
    },
    13: {
        'question': 'What is the output?\n\nprint(min(5, 2, 9))',
        'options': ('9', '2', '5', '0'),
        'answer': '2'
    },
    14: {
        'question': 'Which of the following is mutable?',
        'options': ('tuple', 'string', 'list', 'int'),
        'answer': 'list'
    },
    15: {
        'question': 'What is the output?\n\nprint("hello".capitalize())',
        'options': ('Hello', 'HELLO', 'hello', 'Error'),
        'answer': 'Hello'
    },
    16: {
        'question': 'Which method returns index of an element in a list?',
        'options': ('find()', 'index()', 'locate()', 'position()'),
        'answer': 'index()'
    },
    17: {
        'question': 'Which of these is NOT a loop in Python?',
        'options': ('for', 'while', 'do-while', 'None'),
        'answer': 'do-while'
    },
    18: {
        'question': 'What is the output?\n\nprint(bool(5))',
        'options': ('True', 'False', '5', 'Error'),
        'answer': 'True'
    },
    19: {
        'question': 'Which of these functions returns absolute value?',
        'options': ('abs()', 'absolute()', 'fabs()', 'value()'),
        'answer': 'abs()'
    },
    20: {
        'question': 'Which keyword is used to create a class?',
        'options': ('object', 'define', 'class', 'struct'),
        'answer': 'class'
    }
}

print("\n\n🔰🔰 Let's Start the Quiz 🔰🔰!!!\n\n")
score = 0
choice = {'a':0, 'b':1, 'c':2, 'd':3}

questions_set = random.sample(range(1,21),15)

for i in questions_set:
    print('Q.', data[i]['question'], '\n')
    l = 0
    for j in data[i]['options']:
        opt = ['a.', 'b.', 'c.', 'd.']
        print(opt[l], j)
        l += 1
    print()

    while True:
        attempt = input("Choose your answer: ").lower()
        if attempt in 'abcd' and attempt != '':
            if data[i]['options'][choice[attempt]].strip() == data[i]['answer'].strip():
                print("✅ Correct answer! You got 1 point 👏👏")
                score += 1
                break
            else:
                print(f"❌ Wrong answer. The correct answer is \"{data[i]['answer']}\"")
                break
        else:
            print("🚫 Invalid choice! Try again. Please select from (a/b/c/d)")
    print("\n\n")

print(f"Your overall Score is {score}/15")

if score == 15:
    print("💯 Outstanding performance! 🏆🏅")
elif score > 10:
    print("👍 Good job! Keep it up 👏🙌")
elif score > 5:
    print("🙂 Average performance! Improve more 🤞")
else:
    print("👎 Poor performance! Focus and practice more 🎯")

while True:
    end = input()
    if end != '':
        break

