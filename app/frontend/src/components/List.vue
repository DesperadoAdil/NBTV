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
      <Col span="8" v-for="item in items" :key="item.id">
        <Card class="listcard">
          <img :src="item.thumbnail" class="thumbnail" @click="skip(item)">
          <p class="title">{{ item.title }} </p>
          <p class="teacher">授课老师：{{ item.teacher }} </p>
          <p class="audiencenum">当前人数：{{ item.audiencelist.length}}</p>
          <p class="audiencenum">开播时间：{{ item.createtime}}</p>
        </Card>
      </Col>
    </Row>
  </div>

</template>
<script>
import axios from 'axios'
export default {
  name: 'List',
  data () {
    return {
      userInfo: {
        status: '',
        username: '',
        password: '',
        mobile: '',
        job: ''
      },
      LoginOrLogout: '登录',
      currentpassword: '',
      items: []
    }
  },
  created () {
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

    skip: function (aab) {
      this.$Modal.confirm({
        render: (h) => {
          return h('Input', {
            props: {
              id: 'passinput',
              autofocus: true,
              placeholder: 'Please enter the password of this room'
            },
            on: {
              input: (val) => {
                //                this.value = val;
                this.currentpassword = val
                //                if(val==="123")
                //                  this.$router.push({path: 'living',query:{ id: a.vid}});
              }
            }
          })
        },
        onOk: () => {
          if (this.currentpassword === aab.password) { this.$router.push({path: 'living', query: { id: aab.vid}}) } else {
            this.$Notice.error({
              title: '消息提示',
              desc: '您输入的密码错误，请仔细检查 '
            })
          }
        }
      })
    },
    getList: function () {
      axios.get('/api/list').then((resp) => {
        console.log(resp)
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
.layout-footer-center{
  text-align: center;
  font-size:20px;
}
.listbtn{
  test-align:left;
  font-style:normal;
  font-family:"Times New Roman", Times, serif;
}
.layoutlist{
  min-height:850px;
}
.listcard {
  padding: 3%;
  margin: 6%;
}
.thumbnail {
  height:250px;
  width: 100%;
}
.title{
  font-size:30px ;
  text-align:left;
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
