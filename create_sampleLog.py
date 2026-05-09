import random
import datetime

messages = {
    'INFO': ['센서 데이터 수신 완료', '설비 가동 확인', '네트워크 연결 확인'],
    'WARNING': ['온도 임계값 근접', '센서 응답 지연', '메모리 사용률 80% 초과'],
    'ERROR': ['센서 연결 끊김', '데이터 수신 실패', '설비 과열 감지']
}

with open('sample.log', 'w', encoding='utf-8') as f:
    for i in range(500):
        time = datetime.datetime(2026, 5, 9, 0, 0, 0) + \
               datetime.timedelta(minutes=i*3)
        
        # 5:2:1 비율로 레벨 선택
        level = random.choices(
            ['INFO', 'WARNING', 'ERROR'],
            weights=[5, 2, 1]
        )[0]
        
        message = random.choice(messages[level])

        # 두 가지 형식 섞어서 로그 작성
        if random.random() < 0.5:
            f.write(f"{time} {level} {message}\n")      # 형식1
        else:
            f.write(f"[{time}] [{level}] {message}\n")  # 형식2

print("sample.log 생성 완료")