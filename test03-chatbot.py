# test03-chatbot.py

import openai

# 각자 OPENAI API KEY 지정 : 밑에 값 직접 넣기
openai.api_key = ""

# API KEY 설정에 오류가 있는 지 확인하기 위함
print("api_key :", repr(openai.api_key))

# 챗봇 응답 생성
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 지식이 풍부한 도우미입니다."},
        {"role": "user", "content": "세계에서 가장 큰 도시는 어디인가요?"},
    ],
)

print(response)
print(response["choices"][0]["message"]["content"])