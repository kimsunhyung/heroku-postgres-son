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
            score TEXT,
            input TEXT
        );"""
    )
    data = pd.read_csv('data/score.csv')
    print(data)
    data.to_sql(name='score', con=engine, schema = 'public', if_exists='replace', index=False)



def area(loc):
    #접속
    conn_string = psycopg2.connect(host="ec2-54-225-234-165.compute-1.amazonaws.com",
    dbname='dcpdo186cscu8t', user='fednehfmarnquy', password= '9de42f09c90aa11fd93a3cd4a1303c58998e421c913de3d6e5f08cfa7c89d1b5')
    cur = conn_string.cursor()
    cur.execute("select * from public.area where location like '%{0}%';".format(loc))
    result = cur.fetchall()
    print(result)
    my_df = pd.DataFrame(result, columns = ['name', 'division','location','notice_date','start_day','end_day','release_date','rink']) 
    #쿼리(평택)
    return my_df
    print(area())

