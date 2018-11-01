FROM node:9.9.0
#安装python
RUN apt-get update
#RUN apt-get upgrade
RUN apt-get install -y aptitude
RUN aptitude -y install gcc make zlib1g-dev libffi-dev libssl-dev
RUN wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
RUN tar -xvf Python-3.6.5.tgz
RUN chmod -R +x Python-3.6.5
RUN cd Python-3.6.5/ \
  && ./configure \
  && make \
  && make install
ENV HOME=/app
WORKDIR $HOME
COPY requirements.txt $HOME
RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host mirrors.tuna.tsinghua.edu.cn \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt
COPY app $HOME
COPY sonar-project.properties $HOME/app
WORKDIR $HOME/frontend
# 加速
RUN npm config set registry https://registry.npm.taobao.org
RUN CHROMEDRIVER_CDNURL=https://npm.taobao.org/mirrors/chromedriver npm install
RUN npm run build
WORKDIR $HOME
EXPOSE 5000
ENV PYTHONUNBUFFERED=true
CMD ["python3", "run.py"]
