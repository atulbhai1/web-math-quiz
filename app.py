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
    ans = a/b
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
Bootstrap(app)
test = "Mixed"
@app.route('/', methods=('GET', 'POST'))
def home():
    global test
    if request.method == 'POST' and request.form.get('GoThere') == 'GoThere':
        test = request.form.get('choice')
        print(test)
        return redirect(url_for("quiz"))
    return render_template('home.html')

@app.route('/quiz', methods=('GET', 'POST'))
def quiz():
    global test
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
    print(request.method)
    if request.method == 'POST' and request.form.get('Submit') == 'Submit':
        print("gotthere")
        print(request.form['one'])
        return redirect(url_for('home'))

    return render_template('quiz.html', data=data)
app.run()
