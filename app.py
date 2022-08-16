# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

## DB 연결 Local


app = Flask(__name__)

@app.route("/")
def index():
    #db_create()
    return "Hello World!"

@app.route("/test", methods = ['post'])
def test():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "공공분양", # basic 카드에 들어갈 제목
                        "description": "궁금하신 분양유형을 눌러주세요", # 제목 아래에 들어갈 상세 내용
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 버튼 1
                                "label": "일반분양", # 버튼 1 내용
                                "blockId": "지역 입력용 블록" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": "특별분양", # 버튼 2 내용
                                "blockId": "특별분양 블록" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": "우선분양",# 버튼 3내용
                                "blockId": "우선분양 블록" # 버튼 3에서 연결될 버튼 주소
                            }   
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)


@app.route("/test1", methods = ['post'])
def test1():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "공공분양 일반공급", # basic 카드에 들어갈 제목
                        "description": "신청자격 표입니다", # 제목 아래에 들어갈 상세 내용
                        "thumbnail": {
                            "imageUrl": "https://github.com/kimsunhyung/heroku-postgres-son/blob/main/data/test1.png"
                        },
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 순위 요건 버튼
                                "label": "순위 요건", # 순위 요건 버튼
                                "blockId": "1 순위 요건 블록" # 1순위 블록으로 이동 
                            },
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    #db_create()
    app.run(host='0.0.0.0', port=int(args[1]),debug=True)