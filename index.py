from flask import Flask, render_template, flash, redirect, url_for, request
from .services import db_service, subscription_db_service
import logging, psycopg2

app = Flask(__name__, static_url_path='', static_folder='static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('subscribe'))

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'GET':
        return show_subscription_form()

    if 'email' not in request.form or not request.form['email'].strip():
        flash('Invalid email supplied', 'error')
        return show_subscription_form()

    email = request.form['email']
    nickname = request.form['nickname']
    result = save_subscription(email, nickname)
    if result is None:
        flash('Failed to update subscription. Please try again!', 'error')
        return show_subscription_form()

    return redirect(url_for('thank_you'))

@app.route('/thankyou', methods=['GET'])
def thank_you():
    return render_template('thank_you.html')


def show_subscription_form():
    return render_template('subscription.html')

def save_subscription(email, nickname):
    try:
        db = db_service.DbService()
        db.db_connect()
        sub_service = subscription_db_service.SubscriptionDbService()
        id = sub_service.save_subscription(db.get_cursor(), email, nickname, 1)
        db.commit()
        db.close()

        return id
    except psycopg2.Error as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)

    return None
