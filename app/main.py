# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import database

## DB 연결 Local

app = Flask(__name__)


# 공고



## 공공분양
@app.route("/")
def index():
    return "333338"

@app.route("/public", methods = ['post'])
def public():
    body = request.get_json()
    #print(body)
    #print(body['userRequest']['utterance'])
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
                                "blockId": "62fca29a8a1240569898c7a6" # 버튼 1에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block", # 버튼 2
                                "label": "특별분양", # 버튼 2 내용
                                "blockId": "62fca30e9465de0507b1ed33" # 버튼 2에서 연결될 버튼 주소
                            },
                            {
                                "action":  "block",# 버튼 3
                                "label": "우선분양",# 버튼 3내용
                                "blockId": "62fca32b8a1240569898c7e3" # 버튼 3에서 연결될 버튼 주소
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
    #print(body)
    #print(body['userRequest']['block'])
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
        
                    "basicCard": {
                        "title": "공공분양 일반공급", # basic 카드에 들어갈 제목
                        "description": "신청자격 표입니다", # 제목 아래에 들어갈 상세 내용
                        "thumbnail": {
                            "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/5d03ff5ee64210755f0baf97eddf3a259c1245ef/data/simple/%EC%9D%BC%EB%B0%98%EA%B3%B5%EA%B8%89%20%EC%9E%90%EA%B2%A9.png",
                            "fixedRatio" : True,
                            "width": 800,
                            "height": 800
                        },
                        "buttons": [ # basic 카드에 소속된 버튼 
                            {
                                "action": "block", # 순위 요건 버튼
                                "label": "순위 요건", # 순위 요건 버튼
                                "blockId": "62fca2f4745ef634f0480557" # 1순위 블록으로 이동 
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
    #print(body)
    #print(body['userRequest']['block'])
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


@app.route("/first", methods = ['post'])
def first():
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
                                    "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/main/data/image/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C6.PNG",
                                    "fixedRatio" : True,
                                    "width": 800,
                                    "height": 800
                                },

                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히보기",
                                        "webLinkUrl": "https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=3&cnpClsNo=1&search_put="
                                    },
                                ]
                            },
                            {
                                "title": "",
                                "description": "",
                                "thumbnail": {
                                    "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/main/data/image/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C7.PNG",
                                    "fixedRatio" : True,
                                    "width": 800,
                                    "height": 800
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히보기",
                                        "webLinkUrl": "https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=3&cnpClsNo=1&search_put="
                                    },
                                ]
                            },
                            {
                                "title": "",
                                "description": "",
                                "thumbnail": {
                                    "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/main/data/image/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C8.PNG",
                                    "fixedRatio" : True,
                                    "width": 800,
                                    "height": 800
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히보기",
                                        "webLinkUrl": "https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=873&ccfNo=2&cciNo=3&cnpClsNo=1&search_put="
                                    },
                        
                                ]
                            },
                        ]
                    }
                }   
            ]
        }
    }

    return jsonify(response)

@app.route("/level", methods = ['post'])
def level():
    body = request.get_json()
    #print(body)
    #(body['userRequest']['block'])
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                    {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": "1순위 요건입니다.",
                                "description": "그 외 2순위는 추첨입니다.",
                                "thumbnail": {
                                    "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/82c3397802efe9d294b5c859b77ebeee36411af5/data/image/1%EC%88%9C%EC%9C%84%20%EC%9A%94%EA%B1%B4.png",
                                    "fixedRatio" : True,
                                    "width": 800,
                                    "height": 800
                                },
                            },
                            {
                                "title": "",
                                "description": "동일 순위 시 경쟁 요건표 입니다.",
                                "thumbnail": {
                                    "imageUrl": "https://raw.githubusercontent.com/kimsunhyung/heroku-postgres-son/82c3397802efe9d294b5c859b77ebeee36411af5/data/image/%EB%8F%99%EC%9D%BC%20%EC%88%9C%EC%9C%84%20%EA%B2%BD%EC%9F%81.png",
                                    "fixedRatio" : True,
                                    "width": 800,
                                    "height": 800
                                },
                                "buttons": [
                                    {
                                        "action": "webLink",
                                        "label": "자세히보기",
                                        "webLinkUrl": "https://www.law.go.kr/LSW/LsiJoLinkP.do?joNo=002700000&languageType=KO&docType=JO&lsNm=%EC%A3%BC%ED%83%9D%EA%B3%B5%EA%B8%89%EC%97%90+%EA%B4%80%ED%95%9C+%EA%B7%9C%EC%B9%99&paras=1#"
                                    },
                                ]
                            },
                        ]
                    }
                }   
            ]
        }
    }

    return jsonify(response)

@app.route("/hello", methods = ['post'])
def hello():

    body = request.get_json()
    print(body)
    loc = body['action']['detailParams']['sys_location']['value'] # 들어간 문단만큼의 괄호가 생겨야함
    print(loc)
    print(type(loc))
    sell = database.area(loc)# 함수 안에 설정한 변수를 넣어야함
    print(sell)
    a = sell['name']
    b = sell['rink']
    c = sell['location']
    if len(sell) > 0:
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                        {
                        "listCard": {
                            "header": {
                                "title": "청약공고입니다."
                            },
                            "items": [
                                {
                                    "title": a[0],
                                    "description": c[0],
                                    "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                    "link": {
                                        "web": b[0]
                                }
                                },
                                {
                                    "title": a[1],
                                    "description": c[1],
                                    "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                    "link": {
                                        "web": b[1]
                                }
                                },
                                {
                                    "title": a[2],
                                    "description": c[2],
                                    "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                    "link": {
                                        "web": b[2]
                                }
                                },
                                ],
                            "buttons": [
                                {
                                    "label": "더보기",
                                    "action": "webLink",
                                    "webLinkUrl": "https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do#"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    else :
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "listCard": {
                            "header": {
                                "title": "공고 내역입니다."
                            },
                            "items": [
                                {
                                    "title": '현재 모집중인 공고가 없습니다.',
                                },
                            ],
                            "buttons": [
                                {
                                    "label": "다른공고더보기",
                                    "action": "webLink",
                                    "webLinkUrl": "https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do#"
                                }
                            ]
                        }
                    }
                ]
            }
        }


    return jsonify(response)