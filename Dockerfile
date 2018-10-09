FROM node

WORKDIR /build
# vue的项目目录，包含package.json
ENV VUE_ROOT app/vue_project/my-project/

# 加速
RUN npm config set registry https://registry.npm.taobao.org

# 安装依赖
COPY $VUE_ROOT/package.json /build/package.json
COPY $VUE_ROOT/package-lock.json /build/package-lock.json
RUN CHROMEDRIVER_CDNURL=https://npm.taobao.org/mirrors/chromedriver npm install

# 编译，预期产物为.js .html
COPY $VUE_ROOT /build
ENV NODE_ENV production
RUN npm run-script build

FROM python:3.6.5

ENV HOME=/app

WORKDIR $HOME

COPY requirements.txt $HOME
RUN pip install --trusted-host mirrors.cloud.tencent.com \
    -i http://mirrors.cloud.tencent.com/pypi/simple/ -r requirements.txt

COPY $(flask 根目录，包含app.py) $HOME

# static目录的内容是从vue编译得到的
# COPY --from=0 /build/$(npm build产物的路径) app/static

# EXPOSE 80

ENV PYTHONUNBUFFERED=true
CMD ["python", "app.py"]
