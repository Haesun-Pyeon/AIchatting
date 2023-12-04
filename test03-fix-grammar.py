# test03-fix-grammar.py

import openai

# 각자 OPENAI API KEY 지정 : 밑에 값 직접 넣기
openai.api_key = ''

# API KEY 설정에 오류가 있는 지 확인하기 위함
print("api_key :", repr(openai.api_key))

# 텍스트 생성 혹은 문서 요약
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="""
Fix grammar errors:
- I is a boy
- You is a girl""".strip(),
)

print(response.choices[0].text.strip())