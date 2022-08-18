# -*- coding: utf-8 -*-
from flask import Flask
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

## DB 연결 Local
def db_create():
    # 로컬
    engine = create_engine("postgresql://postgres:1234@localhost:5432/chatbot", echo = False)
      
      # Heroku
    engine = create_engine("postgresql://fednehfmarnquy:9de42f09c90aa11fd93a3cd4a1303c58998e421c913de3d6e5f08cfa7c89d1b5@ec2-54-225-234-165.compute-1.amazonaws.com:5432/dcpdo186cscu8t", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS area(
            name TEXT,
            division TEXT,
            score bigint,
            input bigint,
        );"""
    )
    data = pd.read_csv('data/score.csv')
    print(data)
    data.to_sql(name='score', con=engine, schema = 'public', if_exists='replace', index=False)

app = Flask(__name__)

@app.route("/")
def index():
    db_create()
    return "75"

if __name__ == "__main__":
    db_create()
    app.run(host='0.0.0.0', port=int(args[1]),debug=True)