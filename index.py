from flask import Flask, render_template, flash, redirect, url_for, request
import route_handler

app = Flask(__name__, static_url_path='', static_folder='static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('show_blog'))


@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'GET':
        return route_handler.show_subscription_form()

    if 'email' not in request.form or not request.form['email'].strip():
        flash('Invalid email supplied', 'error')
        return route_handler.show_subscription_form()

    email = request.form['email']
    nickname = request.form['nickname']
    result = route_handler.save_subscription(email, nickname)
    if result is None:
        flash('Failed to update subscription. Please try again!', 'error')
        return route_handler.show_subscription_form()

    return redirect(url_for('thank_you'))


@app.route('/thankyou', methods=['GET'])
def thank_you():
    return render_template('thank_you.html')


@app.route('/lessons', methods=['GET'])
def show_blog():
    return render_template('blog.html')


@app.route('/lessons/<page>', methods=['GET'])
def show_page(page):
    if page not in ['heap.html']:
        return redirect(url_for('show_blog'))

    return render_template(page)


@app.route('/exercises', methods=['GET'])
def show_exercises():
    return render_template('exercise.html')


@app.route('/exercises/<page>', methods=['GET'])
def show_exercise_page(page):
    if page not in ['find-smallest-difference.html']:
        return redirect(url_for('show_blog'))

    return render_template(page)


if __name__ == '__main__':
    app.run()