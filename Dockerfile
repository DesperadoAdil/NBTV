FROM alpine
#安装nodejs，python
RUN apk update \
  && apk add --no-cache nodejs:8.12.0-r0
  && apk add --no-cache python:3.6.6-r0
ENV HOME=/app
WORKDIR $HOME
COPY requirements.txt $HOME
RUN pip install --upgrade pip
RUN pip install --trusted-host mirrors.cloud.tencent.com \
    -i http://mirrors.cloud.tencent.com/pypi/simple/ -r requirements.txt
# vue的项目目录，包含package.json
ENV VUE_ROOT app/app/frontend/
# 加速
RUN npm config set registry https://registry.npm.taobao.org
# 安装依赖
COPY $VUE_ROOT/package.json $HOME/package.json
COPY $VUE_ROOT/package-lock.json $HOME/package-lock.json
RUN CHROMEDRIVER_CDNURL=https://npm.taobao.org/mirrors/chromedriver npm install
COPY app $HOME
WORKDIR /app/app/frontend
RUN npm run build
WORKDIR $HOME
EXPOSE 5000
ENV PYTHONUNBUFFERED=true
CMD ["python", "run.py"]
