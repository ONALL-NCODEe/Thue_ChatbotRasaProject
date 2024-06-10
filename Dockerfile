FROM python:3.10.11 AS BASE

# # Thiết lập biến môi trường SQLALCHEMY_WARN_20
# ENV SQLALCHEMY_WARN_20=1

# # Thiết lập biến môi trường SQLALCHEMY_SILENCE_UBER_WARNING
# ENV SQLALCHEMY_SILENCE_UBER_WARNING=1

# ENV PYTHONWARNINGS="ignore::MovedIn20Warning"

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim

WORKDIR /app

# # Cài đặt các gói từ requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install SQLAlchemy==1.4.26

RUN pip install pandas

RUN pip install --no-cache-dir --upgrade pip

RUN pip install rasa==3.6.20

# Copy tất cả các tệp cần thiết vào thư mục làm việc
COPY . .

# ADD config.yml config.yml
# ADD domain.yml domain.yml
# ADD credentials.yml credentials.yml
# ADD endpoints.yml endpoints.yml 

# # CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug"]
# CMD ["rasa", "run", "--enable-api", "--cors", "*", "--actions", "actions"]
# CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug", "&", "rasa", "run", "actions"]

# Đặt lệnh để chạy server Rasa
CMD ["rasa", "run", "-p", "5005", "--cors", "*"]
CMD ["rasa", "run", "actions"]


