import re
import pandas as pd

# 로그 형식 패턴
PATTERNS = [
    # 형식1: 2026-05-01 00:00:00 INFO 메시지
    r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(INFO|WARNING|ERROR)\s+(.*)',
    # 형식2: [2026-05-01 00:00:00] [INFO] 메시지
    r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s+\[(INFO|WARNING|ERROR)\]\s+(.*)',
]

def parse_line(line):
    # 한 줄의 로그를 패턴에 따라 파싱하여 시간, 레벨, 메시지 추출
    for pattern in PATTERNS:
        match = re.match(pattern, line.strip())
        if match:
            groups = match.groups()
            return groups[0], groups[1], groups[2]
    return None # 형식에 맞지 않는 경우 None 반환

def load_log(filepath):
    # 로그 파일을 읽고 파싱하여 DataFrame으로 반환
    records = []
    failed = 0

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            result = parse_line(line)
            if result:
                records.append({
                    'time': result[0],
                    'level': result[1],
                    'message': result[2]
                })
            else:
                failed += 1

    df = pd.DataFrame(records)
    df['time'] = pd.to_datetime(df['time']) # datetime으로 변환

    print(f"총 {len(df)}줄 파싱 완료, {failed}줄 파싱 실패")
    return df