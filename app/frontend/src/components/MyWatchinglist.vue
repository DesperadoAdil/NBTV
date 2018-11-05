<template>
  <div id="list" class="posi">
    <h1 class="list-info">
      <Icon type="ios-time" />
      正在播出
      <Button class="listbtn" @click="timelist">开播时间</Button>
      <Button class="listbtn" @click="audiencelist">创建时间</Button>
    </h1>
    <Divider />
    <Row>
      <Col span="12" v-for="item in items" :key="item.vid">
        <Card class="watchcard">
          <img :src="item.thumbnail" class="thumbnail" @click="skip(item)">
          <p class="title"></p>
            {{ item.title }}
          <Tooltip placement="top">
            <Icon class="delicon" color="red" type="md-close" @click="del(item)"/>
            <div slot="content">
              <p class="addtext">删除直播间</p>
            </div>
          </Tooltip>
          <p class="teacher">授课老师：{{ item.teacher }} </p>
          <p class="audiencenum">开播时间：{{ item.showtime}}</p>
          <p class="audiencenum">创建时间：{{ item.createtime}}</p>
        </Card>
      </Col>
    </Row>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'List',
  data: function () {
    return {
      mylistform: {
        username: '',
        job: ''
      },
      delmyclassform: {
        username: '',
        job: '',
        classroom: ''
      },
      userInfo: {
        status: '',
        username: '',
        password: '',
        mobile: '',
        job: ''
      },
      LoginOrLogout: '登录',
      currentpassword: '',
      imgwitd: '100px',
      items: []
    }
  },
  created: function () {
    this.showUserInfo()
    this.getList()
  },
  methods: {
    showUserInfo () {
      this.userInfo['username'] = this.$cookies.get('user').username
      this.userInfo['status'] = this.$cookies.get('user').status
      this.userInfo['password'] = this.$cookies.get('user').password
      this.userInfo['mobile'] = this.$cookies.get('user').mobile
      this.userInfo['job'] = this.$cookies.get('user').job
      if (this.userInfo['status'] === 'success') {
        this.LoginOrLogout = this.userInfo['username']
      }
    },
    timelist: function () {
      var compare = function (obj1, obj2) {
        var val1 = obj1.showtime
        var val2 = obj2.showtime
        var datas1 = val1.split(' ')
        var datas2 = val2.split(' ')

        var date1 = datas1[0].split('-')
        var date2 = datas2[0].split('-')

        var time1 = datas1[1].split(':')
        var time2 = datas2[1].split(':')
        console.log(parseInt(date1[0]))
        if (parseInt(date1[0]) < parseInt(date2[0])) {
          return 1
        } else if (parseInt(date1[0]) > parseInt(date2[0])) {
          return -1
        } else {
          if (parseInt(date1[1]) < parseInt(date2[1])) {
            return 1
          } else if (parseInt(date1[1]) > parseInt(date2[1])) {
            return -1
          } else {
            if (parseInt(date1[2]) < parseInt(date2[2])) {
              return 1
            } else if (parseInt(date1[2]) > parseInt(date2[2])) {
              return -1
            } else {
              if (parseInt(time1[0]) < parseInt(time2[0])) {
                return 1
              } else if (parseInt(time1[0]) > parseInt(time2[0])) {
                return -1
              } else {
                if (parseInt(time1[1]) < parseInt(time2[1])) {
                  return 1
                } else if (parseInt(time1[1]) > parseInt(time2[1])) {
                  return -1
                } else {
                  if (parseInt(time1[2]) < parseInt(time2[2])) {
                    return 1
                  } else if (parseInt(time1[2]) > parseInt(time2[2])) {
                    return -1
                  } else {
                    return 0
                  }
                }
              }
            }
          }
        }

      }
      this.items.sort(compare)
      this.$Notice.success({
        title: '消息提示',
        desc: '已经按照开播时间排序'
      })
    },
    audiencelist: function () {
      var compare = function (obj1, obj2) {
        var val1 = obj1.createtime
        var val2 = obj2.createtime
        var datas1 = val1.split(' ')
        var datas2 = val2.split(' ')

        var date1 = datas1[0].split('-')
        var date2 = datas2[0].split('-')

        var time1 = datas1[1].split(':')
        var time2 = datas2[1].split(':')
        console.log(parseInt(date1[0]))
        if (parseInt(date1[0]) < parseInt(date2[0])) {
          return 1
        } else if (parseInt(date1[0]) > parseInt(date2[0])) {
          return -1
        } else {
          if (parseInt(date1[1]) < parseInt(date2[1])) {
            return 1
          } else if (parseInt(date1[1]) > parseInt(date2[1])) {
            return -1
          } else {
            if (parseInt(date1[2]) < parseInt(date2[2])) {
              return 1
            } else if (parseInt(date1[2]) > parseInt(date2[2])) {
              return -1
            } else {
              if (parseInt(time1[0]) < parseInt(time2[0])) {
                return 1
              } else if (parseInt(time1[0]) > parseInt(time2[0])) {
                return -1
              } else {
                if (parseInt(time1[1]) < parseInt(time2[1])) {
                  return 1
                } else if (parseInt(time1[1]) > parseInt(time2[1])) {
                  return -1
                } else {
                  if (parseInt(time1[2]) < parseInt(time2[2])) {
                    return 1
                  } else if (parseInt(time1[2]) > parseInt(time2[2])) {
                    return -1
                  } else {
                    return 0
                  }
                }
              }
            }
          }
        }

      }
      this.items.sort(compare)
      this.$Notice.success({
        title: '消息提示',
        desc: '已经按照创建时间排序'
      })
    },

    del: function (a) {
      this.$Modal.confirm({
        title: '警告',
        content: '确认删除直播间吗',
        onOk: () => {
          //var params = new URLSearchParams()
          //params.append('name', this.userInfo['username'])
          //params.append('classroom', a)
          //params.append('job', this.userInfo['job'])
          const data = this.delmyclassform
          data['username'] = this.userInfo['username']
          data['job'] = this.userInfo['job']
          data['classroom'] = a
          axios.post('/api/user/delmyclass', data).then((resp) => {

          })
          Array.prototype.indexOf = function (val) {
            for (var i = 0; i < this.length; i++) {
              if (this[i] === val) return i
            }
            return -1
          }

          Array.prototype.remove = function (val) {
            var index = this.indexOf(val)
            if (index > -1) {
              this.splice(index, 1)
            }
          }
        }
        // 传给后端删除信息
      })
    },
    skip: function (a) {
      this.$router.push({path: '/living/'+ a.url})
    },
    getList: function () {
      //var params = new URLSearchParams()
      //params.append('name', this.userInfo['username'])
      //params.append('job', this.userInfo['job'])
      const data = this.mylistform
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      axios.post('/api/user/mylist', data).then((resp) => {
        this.items = resp.data
      })
    }
  }

}
</script>
<style>
  ul {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
  li {
    list-style: none;
  }
  .posi{
    position: absolute;
    top: 60px;
    width: 100%;
  }
  .addtext{
    test-align:left;
    font-size: 20px;
    font-style:normal;
    font-family:"Times New Roman", Times, serif;
  }
  .delicon{
    float:right;
  }
  .listbtn{
    test-align:left;
    font-style:normal;
    font-family:"Times New Roman", Times, serif;
    margin:10px;
  }
  .layoutlist{
    min-height:850px;
  }
  .watchcard {
    padding: 2%;
    margin: 2%;
  }
  .thumbnail {
    height:150px;
    width: 100%;
  }
  .title{
    font-size:30px ;
    text-align:left;
    width: auto;
  }
  .teacher{
    font-size:20px ;
    text-align:left;
  }
  .audiencenum{
    font-size:20px ;
    text-align:left;
  }
  .list-info {
    text-align: left;
  }
</style>
