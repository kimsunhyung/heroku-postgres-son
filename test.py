{
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
