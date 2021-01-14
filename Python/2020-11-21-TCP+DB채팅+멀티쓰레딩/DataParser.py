# 사용할 모듈을 Import
import os
import sqlite3
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# chats 변수 초기화
chats = ''

# 현재 해당 python file의 directory name을 구해서 저장
BASE_DIR = os.path.realpath(os.path.dirname(__file__))

# chat.db 객체 생성
conn = sqlite3.connect(os.path.join(BASE_DIR, "chat.db"))
# chat.db 객체에 접속
cur = conn.cursor()
# "SELECT * FROM chat" 쿼리를 실행 (이 쿼리는 chat.db에 저장되어있는 모든 데이터를 불러옴)
cur.execute("SELECT * FROM chat")
rows = cur.fetchall()

# 채팅 내용마다 for문을 실행
for row in rows:
    # 8번째 라인에서 초기화시켜두었던 chats에 채팅 데이터를 추가
    chats += (' ' + str(row[1]))
# database connection close
conn.close()

# wordcloud 객체 생성
wordcloud = WordCloud(font_path=os.path.join(BASE_DIR, "NanumGothic.ttf"), background_color='white').generate(chats)

plt.figure(figsize=(10,5)) #이미지 사이즈 지정
plt.imshow(wordcloud, interpolation='lanczos') #이미지의 부드럽기 정도
plt.axis('off') #x y 축 숫자 제거

# 완성된 wordcloud를 그래픽으로 화면에 표시
plt.show()
try:
    # wordcloud 이미지를 저장
    plt.savefig()
except:
    # 실패시 패싱
    pass