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

@app.route("/public", methods = ['post'])
def public():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])
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
                                "blockId": "62fb438d70055f434dcd2f9a" # 버튼 1에서 연결될 버튼 주소
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


@app.route("/normal", methods = ['post'])
def normal():
    body = request.get_json()
    print(body)
    print(body['userRequest']['block'])
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "공공분양 일반공급", # basic 카드에 들어갈 제목
                        "description": "신청자격 표입니다", # 제목 아래에 들어갈 상세 내용
                        "thumbnail": {
                            "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/main/data/test1.png"
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


@app.route("/special", methods = ['post'])
def special():
    body = request.get_json()
    print(body)
    print(body['userRequest']['block'])
    response = {
         "version": "2.0",
         "template": {
            "outputs": [
                {
                 "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                            "thumbnail": {
                                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                                "width": 800,
                                "height": 800
                        },
                            "buttons": [
                        {
                            "action": "weblink",
                            "label": "자세히보기",
                            "webLinkUrl": "짜잔! 우리가 찾던 보물입니다"
                        },
                        {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                        }
                        ]
                        },
                        {
                            "title": "보물상자2",
                            "description": "보물상자2 안에는 뭐가 있을까",
                            "thumbnail": {
                                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                        },
                            "buttons": [
                        {
                            "action": "message",
                            "label": "열어보기",
                            "messageText": "짜잔! 우리가 찾던 보물입니다"
                        },
                        {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                        }
                        ]
                        },
                        {
                            "title": "보물상자3",
                            "description": "보물상자3 안에는 뭐가 있을까",
                            "thumbnail": {
                                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
                        },
                            "buttons": [
                        {
                            "action": "message",
                            "label": "열어보기",
                            "messageText": "짜잔! 우리가 찾던 보물입니다"
                        },
                        {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                        }
                    ]
                }
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