from flask import render_template
import logging, psycopg2
from db_service import DbService
from subscription_db_service import SubscriptionDbService

def show_subscription_form():
    return render_template('subscription.html')

def save_subscription(email, nickname):
    try:
        db = DbService()
        db.db_connect()
        sub_service = SubscriptionDbService()
        id = sub_service.save_subscription(db.get_cursor(), email, nickname, 1)
        db.commit()
        db.close()

        return id
    except psycopg2.Error as e:
        logging.error(e)
    except Exception as e:
        logging.error(e)

    return None