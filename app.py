import random
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    name = "김보인"
    random_number = random.randint(1, 100)
    count = 0

    while (1):
        while (1):
            input_num = input("숫자입력(1~100)")
            try:
                input_num = int(input_num)
            except:
                print("1~100사이의 숫자를 입력해주세요")
            break

        count += 1
        if input_num == random_number:
            print("정답입니다.")
        elif input_num > random_number:
            print("down")
        else:
            print("up")

    context = {
        "name": name,
        "random_number": random_number,
        "input_num": input_num,
    }

    return render_template('main.html', data=context)


if __name__ == '__main__':
    app.run(debug=True)
