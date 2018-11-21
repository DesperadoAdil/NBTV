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
      <Col span="8" v-for="item in items" :key="item.vid" v-if="item.mode !== 'private'">
        <Card class="listcard" @click.native="skip(item)">
          <img :src="item.thumbnail" class="thumbnail">
          <p class="title">{{ item.title }} </p>
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
  data () {
    return {
      modal1: false,
      userInfo: {
        status: '',
        username: '',
        password: '',
        mobile: '',
        job: ''
      },
      LoginOrLogout: '登录',
      currentpassword: '',
      items: [
        {
          id: '1',
          teacher: 'zsh',
          title: 'math',
          thumbnail: require('../assets/logo.png'),
          password: '123',
          url: 'zsh',
          studentlist: '',
          teacherlist: '',
          audiencelist: [1, 5, 6, 21, 321, 43],
          visible: '',
          vid: '242544',
          createtime: '2018-10-18 13:37:05',
          showtime: '2018-10-18 13:37:05',
          shutuplist: [],
          blacklist: []
        }

      ]
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
        var date1 = new Date(val1.replace(/-/g, '\/'))
        var date2 = new Date(val2.replace(/-/g, '\/'))
        console.log(date1)
        if (date1 > date2) {
          return -1
        } else if (date2 > date1) {
          return 1
        } else {
          return 0
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
        var date1 = new Date(val1.replace(/-/g, '\/'))
        var date2 = new Date(val2.replace(/-/g, '\/'))
        if (date1 > date2) {
          return -1
        } else if (date2 > date1) {
          return 1
        } else {
          return 0
        }
      }
      this.items.sort(compare)
      this.$Notice.success({
        title: '消息提示',
        desc: '已经按照创建时间排序'
      })
    },

    skip: function (item) {
      if (item.blacklist.includes(this.userInfo.username)) {
        this.$Message.error('您已被永久移出教室')
        return
      }
      /*if (item.mode === 'protected') {
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
            if (this.currentpassword === item.password) {
              this.$router.push({path: '/living/' + item.url})
              window.location.reload()
            } else {
              this.$Notice.error({
                title: '消息提示',
                desc: '您输入的密码错误，请仔细检查 '
              })
            }
          }
        })
      } else {*/
        this.$router.push({path: '/living/' + item.url})
      //}
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
#list {
  padding: 0 5%;
}

li {
  list-style: none;
}
.posi{
  position: absolute;
  top: 60px;
  width: 100%;
}
.listbtn{
  test-align:left;
  font-style:normal;
  font-family:"Times New Roman", Times, serif;
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
