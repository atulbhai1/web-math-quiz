from random import randint
from flask_bootstrap import Bootstrap
def addingQ(k):
    a = randint(0, 10000)
    b = randint(0, 10000)
    q = f"{a} + {b} = "
    ans = a+b
    return [k, q,ans]
def subtractingQ(k):
    a = randint(0, 10000)
    b = randint(0, 10000)
    q = f"{a} - {b} = "
    ans = a-b
    return [k,q,ans]
def multiplyingQ(k):
    a = randint(0, 100)
    b = randint(0, 100)
    q = f"{a} x {b} = "
    ans = a*b
    return [k,q,ans]
def dividingQ(k):
    a = randint(0, 100)
    b = randint(0, 100)
    q = f"{a} ➗ {b} = "
    ans = a//b
    return [k,q,ans]
def mixed():
    qs = []
    for i in range(1,11):
        c= randint(1, 4)
        if c==1:
            qs.append(addingQ(i))
        elif c==2:
            qs.append(subtractingQ(i))
        elif c==3:
            qs.append(multiplyingQ(i))
        elif c==4:
            qs.append(dividingQ(i))
    return qs
def addition():
    qs = []
    for i in range(1, 11):
        qs.append(addingQ(i))
    return qs
def division():
    qs = []
    for i in range(1,11):
        qs.append(dividingQ(i))
    return qs
def subtraction():
    qs = []
    for i in range(1,11):
        qs.append(subtractingQ(i))
    return qs
def multiplying():
    qs = []
    for i in range(1,11):
        qs.append(multiplyingQ(i))
    return qs
from flask import Flask, render_template, request, url_for, flash, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = '17bb05ad203765f49322692652f2bf6d761bf939885c0fc6'
Bootstrap(app)
test = "Mixed"
data = []
responses = {}
score = 0
@app.route('/', methods=('GET', 'POST'))
def home():
    global test, data
    if request.method == 'POST':
        test = request.form.get('choice')
        print(test)
        if test == "Addition":
            qs = addition()
        elif test == "Subtraction":
            qs = subtraction()
        elif test == "Multiplication":
            qs = multiplying()
        elif test == "Division":
            qs = division()
        else:
            qs = mixed()
        data = qs
        return redirect(url_for("quiz"))
    return render_template('home.html')

@app.route('/quiz', methods=('GET', 'POST'))
def quiz():
    global data, responses, score
    if request.method == 'POST':
        print("gotthere")
        responses['1'] = request.form['1']
        responses['2'] = request.form['2']
        responses['3'] = request.form['3']
        responses['4'] = request.form['4']
        responses['5'] = request.form['5']
        responses['6'] = request.form['6']
        responses['7'] = request.form['7']
        responses['8'] = request.form['8']
        responses['9'] = request.form['9']
        responses['10'] = request.form['10']
        t = 0
        for d in data:
            if int(float(responses[f'{d[0]}'])) == d[2]:
                t += 10
        score = t
        return redirect(url_for('see'))
    return render_template('quiz.html', data=data)
@app.route('/score', methods=('GET', 'POST'))
def see():
    global score
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('see.html', data=score)
app.run()
