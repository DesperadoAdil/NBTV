FROM node:9.9.0
#安装python
RUN apt-get update
#RUN apt-get upgrade
#  && apt-get install aptitude
RUN aptitude -y install gcc make zlib1g-dev libffi-dev libssl-dev
RUN wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
RUN tar -xvf Python-3.6.5.tgz
RUN chmod -R +x Python-3.6.5
RUN cd Python-3.6.5/
RUN ./configure
RUN make && make install
ENV HOME=/app
WORKDIR $HOME
COPY requirements.txt $HOME
RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host mirrors.cloud.tencent.com \
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
CMD ["python3", "run.py"]
