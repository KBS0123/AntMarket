# 베이스 이미지로 Python 3.9 사용
FROM python:3.9-slim

# 작업 디렉토리를 설정
WORKDIR /code

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y netcat-openbsd

# 필요한 파일들을 복사
COPY requirements.txt /code/

# 의존성 패키지를 설치
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드를 복사
COPY . /code/

# 포트 노출
EXPOSE 8000

# 시작 명령어 설정
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
