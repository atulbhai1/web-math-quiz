from random import randint
from flask_bootstrap import Bootstrap
superscript = "⁰¹²³⁴⁵⁶⁷⁸⁹"
def exponentsQEASY(k):
    a = randint(0, 5)
    b = randint(0, 5)
    symbol = superscript[b]
    q = f"{a}{symbol}= "
    ans = a**b
    return [k, q,ans]
def exponentsQMIX(k):
    choice = randint(1,4)
    if choice == 1:
        return exponentsQEASY(k)
    elif choice == 2:
        return exponentsQMED(k)
    else:
        return exponentsQHARD(k)
def exponentsQMED(k):
    a = randint(0, 10)
    b = randint(0, 7)
    symbol = superscript[b]
    q = f"{a}{symbol}= "
    ans = a**b
    return [k, q, ans]
def exponentsQHARD(k):
    a = randint(0, 10)
    b = randint(0, 10)
    c = randint(1, 6)
    symbol = superscript[c]
    q = f"{a}({b}){symbol}= "
    ans = a*(b**c)
    return [k, q, ans]
def addingQEASY(k):
    a = randint(0, 100)
    b = randint(0, 100)
    q = f"{a} + {b} = "
    ans = a+b
    return [k, q,ans]
def addingQMIX(k):
    choice = randint(1,4)
    if choice == 1:
        return addingQEASY(k)
    elif choice == 2:
        return addingQMED(k)
    else:
        return addingQHARD(k)
def addingQMED(k):
    a = randint(0, 1000)
    b = randint(0, 1000)
    q = f"{a} + {b} = "
    ans = a+b
    return [k, q,ans]
def addingQHARD(k):
    a = randint(0, 10000)
    b = randint(0, 10000)
    q = f"{a} + {b} = "
    ans = a+b
    return [k, q,ans]
def subtractingQEASY(k):
    a = randint(0, 100)
    b = randint(0, 100)
    q = f"{a} - {b} = "
    ans = a-b
    return [k, q,ans]
def subtractingQMIX(k):
    choice = randint(1,4)
    if choice == 1:
        return subtractingQEASY(k)
    elif choice == 2:
        return subtractingQMED(k)
    else:
        return subtractingQHARD(k)
def subtractingQMED(k):
    a = randint(0, 1000)
    b = randint(0, 1000)
    q = f"{a} - {b} = "
    ans = a-b
    return [k, q,ans]
def subtractingQHARD(k):
    a = randint(0, 10000)
    b = randint(0, 10000)
    q = f"{a} - {b} = "
    ans = a-b
    return [k, q,ans]
def multiplyingQEASY(k):
    a = randint(0, 100)
    b = randint(0, 100)
    q = f"{a} x {b} = "
    ans = a*b
    return [k, q,ans]
def multiplyingQMIX(k):
    choice = randint(1,4)
    if choice == 1:
        return multiplyingQEASY(k)
    elif choice == 2:
        return multiplyingQMED(k)
    else:
        return multiplyingQHARD(k)
def multiplyingQMED(k):
    a = randint(0, 1000)
    b = randint(0, 1000)
    q = f"{a} x {b} = "
    ans = a*b
    return [k, q,ans]
def multiplyingQHARD(k):
    a = randint(0, 10000)
    b = randint(0, 10000)
    q = f"{a} x {b} = "
    ans = a*b
    return [k, q,ans]
def dividingQEASY(k):
    a = randint(0, 100)
    b = randint(0, 100)
    q = f"{a} ➗{b} = "
    ans = a//b
    return [k, q,ans]
def dividingQMIX(k):
    choice = randint(1,4)
    if choice == 1:
        return dividingQEASY(k)
    elif choice == 2:
        return dividingQMED(k)
    else:
        return dividingQHARD(k)
def dividingQMED(k):
    a = randint(0, 1000)
    b = randint(0, 1000)
    q = f"{a} ➗ {b} = "
    ans = a//b
    return [k, q,ans]
def dividingQHARD(k):
    a = randint(0, 10000)
    b = randint(0, 10000)
    q = f"{a} ➗ {b} = "
    ans = a//b
    return [k, q,ans]
def mixedEasy():
    qs = []
    for i in range(1,11):
        c= randint(1, 4)
        if c==1:
            qs.append(addingQEASY(i))
        elif c==2:
            qs.append(subtractingQEASY(i))
        elif c==3:
            qs.append(multiplyingQEASY(i))
        elif c==4:
            qs.append(dividingQEASY(i))
    return qs
def mixedMED():
    qs = []
    for i in range(1,11):
        c= randint(1, 4)
        if c==1:
            qs.append(addingQMED(i))
        elif c==2:
            qs.append(subtractingQMED(i))
        elif c==3:
            qs.append(multiplyingQMED(i))
        elif c==4:
            qs.append(dividingQMED(i))
    return qs
def mixedHARD():
    qs = []
    for i in range(1,11):
        c= randint(1, 4)
        if c==1:
            qs.append(addingQHARD(i))
        elif c==2:
            qs.append(subtractingQHARD(i))
        elif c==3:
            qs.append(multiplyingQHARD(i))
        elif c==4:
            qs.append(dividingQHARD(i))
    return qs
def mixedMIX():
    qs = []
    for i in range(1,11):
        c= randint(1, 4)
        if c==1:
            qs.append(addingQMIX(i))
        elif c==2:
            qs.append(subtractingQMIX(i))
        elif c==3:
            qs.append(multiplyingQMIX(i))
        elif c==4:
            qs.append(dividingQMIX(i))
    return qs
def addition(level="MIX"):
    qs = []
    if level == "EASY":
        f = addingQEASY
    elif level == "MED":
        f = addingQMED
    elif level == "HARD":
        f = addingQHARD
    else:
        f = addingQMIX
    for i in range(1, 11):
        qs.append(f(i))
    return qs
def division(level="MIX"):
    qs = []
    if level == "EASY":
        f = divisionQEASY
    elif level == "MED":
        f = divisionQMED
    elif level == "HARD":
        f = divisionQHARD
    else:
        f = divisionQMIX
    for i in range(1,11):
        qs.append(f(i))
    return qs
def subtraction(level="MIX"):
    qs = []
    if level == "EASY":
        f = subtractingQEASY
    elif level == "MED":
        f = subtractingQMED
    elif level == "HARD":
        f = subtractingQHARD
    else:
        f = subtractingQMIX
    for i in range(1,11):
        qs.append(f(i))
    return qs
def multiplying(level="MIX"):
    qs = []
    if level == "EASY":
        f = multiplyingQEASY
    elif level == "MED":
        f = multiplyingQMED
    elif level == "HARD":
        f = multiplyingQHARD
    else:
        f = multiplyingQMIX
    for i in range(1,11):
        qs.append(f(i))
    return qs
def mixed(level="MIX"):
    if level == "EASY":
        f = mixedEASY
    elif level == "MED":
        f = mixedMED
    elif level == "HARD":
        f = mixedHARD
    else:
        f = mixedMIX
    return f()
def exponents(level="MIX"):
    qs = []
    if level == "EASY":
        f = exponentsQEASY
    elif level == "MED":
        f = exponentsQMED
    elif level == "HARD":
        f = exponentsQHARD
    else:
        f = exponentsQMIX
    for i in range(1,11):
        qs.append(f(i))
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
        diff = request.form.get('level')
        print(test)
        if test == "Addition":
            qs = addition(diff)
        elif test == "Subtraction":
            qs = subtraction(diff)
        elif test == "Multiplication":
            qs = multiplying(diff)
        elif test == "Division":
            qs = division(diff)
        elif test == "Exponents":
            qs = exponents(diff)
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
        for i in range(1,11):
            if request.form[f'{i}']:
                responses[f'{i}'] = request.form[f'{i}']
            else:
                responses[f'{i}'] = "42365864526985431367459765492546968254923645923465237452345623549623594763259472452937645946249252694532945274563297459745294659247"
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
