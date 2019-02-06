import logging, psycopg2


class SubscriptionDbService:
    def save_subscription(self, cursor, email, nickname, subscription_id):
        sql = 'INSERT INTO users (email, first_name) VALUES(%s, %s) ON CONFLICT(email) DO NOTHING RETURNING id;'
        cursor.execute(sql, (email, nickname))
        id = cursor.fetchone()[0]


        print(id)

        #subscription_sql = 'INSERT INTO'

        return id
