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
    return "34"

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
                                "title": "",
                                "description": "",
                                "thumbnail": {
                                    "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/main/data/simple/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C1.PNG",
                                    "fixedRatio" : True,
                                    "width": 800,
                                    "height": 800
                                },

                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히보기",
                                        "webLinkUrl": "https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=4&cnpClsNo=1&search_put="
                                    },
                                ]
                            },
                            {
                                "title": "",
                                "description": "",
                                "thumbnail": {
                                    "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/main/data/simple/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C2.PNG",
                                    "fixedRatio" : True,
                                    "width": 800,
                                    "height": 800
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히보기",
                                        "webLinkUrl": "https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=4&cnpClsNo=2&search_put="
                                    },
                                ]
                            },
                            {
                                "title": "",
                                "description": "",
                                "thumbnail": {
                                    "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/main/data/simple/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C3.PNG",
                                    "fixedRatio" : True,
                                    "width": 800,
                                    "height": 800
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히보기",
                                        "webLinkUrl": "https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=4&cnpClsNo=1&search_put="
                                    },
                        
                                ]
                            },
                            {
                                "title": "",
                                "description": "",
                                "thumbnail": {
                                    "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/main/data/simple/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C4.PNG",
                                    "fixedRatio" : True,
                                    "width": 800,
                                    "height": 800
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히보기",
                                        "webLinkUrl": "https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=4&cnpClsNo=1&search_put="
                                    },
                                ]
                            },
                            {
                                "title": "",
                                "description": "",
                                "thumbnail": {
                                    "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/main/data/simple/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C5.PNG",
                                    "fixedRatio" : True,
                                    "width": 800,
                                    "height": 800
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히보기",
                                        "webLinkUrl": "https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=4&cnpClsNo=2&search_put="
                                    },
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