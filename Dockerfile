FROM node:9.9.0
RUN npm config set registry https://registry.npm.taobao.org \
 && npm config set sass_binary_site=https://npm.taobao.org/mirrors/node-sass/ \
 && npm config set phantomjs_cdnurl=https://npm.taobao.org/mirrors/phantomjs/

# use tuna mirror
Run echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main" > /etc/apt/sources.list \
 && echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main" >> /etc/apt/sources.list \
 && echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian-security/ stretch/updates main" >> /etc/apt/sources.list

RUN apt-get update \
 && apt-get install -y --no-install-recommends openjdk-8-jre

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
WORKDIR /app
RUN CHROMEDRIVER_CDNURL=https://npm.taobao.org/mirrors/chromedriver npm install
COPY . /app
ENV TEST_ROOT /app
ENV PORT 80
EXPOSE 80
CMD npm start
