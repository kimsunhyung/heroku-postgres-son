# -*- coding: utf-8 -*-
from flask import Flask
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import psycopg2, csv

## DB 연결 Local
def db_create():
    # 로컬
    engine = create_engine("postgresql://postgres:1234@localhost:5432/chatbot", echo = False)
      
      # Heroku
    engine = create_engine("postgresql://fednehfmarnquy:9de42f09c90aa11fd93a3cd4a1303c58998e421c913de3d6e5f08cfa7c89d1b5@ec2-54-225-234-165.compute-1.amazonaws.com:5432/dcpdo186cscu8t", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS score(
            name TEXT,
            division TEXT,
            score INT,
            input INT
        );"""
    )
    data = pd.read_csv('data/score.csv')
    print(data)
    data.to_sql(name='score', con=engine, schema = 'public', if_exists='replace', index=False)


def area():
    #접속
    conn =psycopg2.connect(host="postgresql://fednehfmarnquy:9de42f09c90aa11fd93a3cd4a1303c58998e421c913de3d6e5f08cfa7c89d1b5@ec2-54-225-234-165.compute-1.amazonaws.com:5432/dcpdo186cscu8t",
    dbname='area', user='fednehfmarnquy', password= '9de42f09c90aa11fd93a3cd4a1303c58998e421c913de3d6e5f08cfa7c89d1b5')

    cur=conn.cursor()
    cur.execute('select * from area;')
    rows = cur.fetchall()
    print(rows)
    #쿼리(평택)



app = Flask(__name__)

@app.route("/")
def index():
    db_create()
    return 'I am sonham'

if __name__ == "__main__":
    db_create()
    app.run(host='0.0.0.0', port=int(args[1]),debug=True)