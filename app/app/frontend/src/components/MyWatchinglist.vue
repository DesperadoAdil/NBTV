<template>
  <div id="list" class="posi">
    <Layout class="layoutlist">
      <Header>
        <ButtonGroup class="btns" size="large" shape="circle" vertical="false">
          <!--<Tooltip placement="top">-->
          <!--<Button class="addbutton" size="large" type="primary"  shape="circle" icon="md-add" ></Button>-->
          <!--<div slot="content">-->
          <!--<p class="addtext">新建直播间</p>-->
          <!--</div>-->
          <!--</Tooltip>-->
          <Tooltip placement="top">
            <Button class="addbutton" size="large" type="primary"  shape="circle" icon="md-help"></Button>
            <div slot="content">
              <p class="addtext">待创建功能</p>
            </div>
          </Tooltip>
        </ButtonGroup>
        <ButtonGroup class="paixu">
          <!--<ButtonGroup class="listbtns">-->
          <!--<Button class="listtext" type="text" >在线直播</Button>-->
          <Button class="listbtn" type="primary"  @click="timelist">按开播时间排列</Button>
          <Button class="listbtn" type="primary"  @click="audiencelist">按观众人数排序</Button>
        </ButtonGroup>
      </Header>
      <Content class="listclass">

        <!--<ButtonGroup  >-->
          <!--&lt;!&ndash;<ButtonGroup class="listbtns">&ndash;&gt;-->
          <!--<Button class="listtext" type="text" >我的直播</Button>-->
          <!--<Button class="listbtn" type="primary" shape="circle" @click="timelist">按开播时间排列</Button>-->
          <!--<Button class="listbtn" type="primary" shape="circle" @click="audiencelist">按观众人数排序</Button>-->
        <!--</ButtonGroup>-->

        <Row>
          <Col span="12" v-for="item in items" key="item.id">
          <Card class="watchcard">
            <!--<div class="aspectration" data-ratio="16:9">-->
            <img :src="item.thumbnail" class="thumbnail" @click="skip(item)">            <!--</div>-->

            <p class="title">{{ item.title }}
              <Tooltip placement="top">
                <Icon class="delicon" color="red" type="md-close" @click="del(item)"/>
                <div slot="content">
                  <p class="addtext">删除直播间</p>
                </div>
              </Tooltip>
            </p>

            <p class="teacher">授课老师：{{ item.teacher }} </p>
            <p class="audiencenum">当前人数：{{ item.audiencelist.length}}</p>
            <p class="audiencenum">开播时间：{{ item.createtime}}</p>
          </Card>
          </Col>
        </Row>
      </Content>
      <Footer class="layout-footer-center">2018-? &copy; SitTillGraduation</Footer>

    </Layout>

  </div>

</template>
<script>
import axios from 'axios'
export default {
  name: 'List',
  data: function () {
    return {
      userInfo: {
        status: '',
        username: '',
        password: '',
        mobile: '',
        job: 'teacher'
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
          return -1
        } else if (parseInt(date1[0]) > parseInt(date2[0])) {
          return 1
        } else {
          if (parseInt(date1[1]) < parseInt(date2[1])) {
            return -1
          } else if (parseInt(date1[1]) > parseInt(date2[1])) {
            return 1
          } else {
            if (parseInt(date1[2]) < parseInt(date2[2])) {
              return -1
            } else if (parseInt(date1[2]) > parseInt(date2[2])) {
              return 1
            } else {
              if (parseInt(time1[0]) < parseInt(time2[0])) {
                return -1
              } else if (parseInt(time1[0]) > parseInt(time2[0])) {
                return 1
              } else {
                if (parseInt(time1[1]) < parseInt(time2[1])) {
                  return -1
                } else if (parseInt(time1[1]) > parseInt(time2[1])) {
                  return 1
                } else {
                  if (parseInt(time1[2]) < parseInt(time2[2])) {
                    return -1
                  } else if (parseInt(time1[2]) > parseInt(time2[2])) {
                    return 1
                  } else {
                    return 0
                  }
                }
              }
            }
          }
        }
        if (val1 < val2) {
          return -1
        } else if (val1 > val2) {
          return 1
        } else {
          return 0
        }
      }
      this.items.sort(compare)
      this.$Notice.success({
        title: '消息提示',
        desc: '已经按照时间排序'
      })
    },
    audiencelist: function () {
      var compare = function (obj1, obj2) {
        var val1 = obj1.audiencelist.length
        var val2 = obj2.audiencelist.length
        if (val1 > val2) {
          return -1
        } else if (val1 < val2) {
          return 1
        } else {
          return 0
        }
      }
      this.items.sort(compare)
      this.$Notice.success({
        title: '消息提示',
        desc: '已经按照热度排序'
      })
    },
    del: function (a) {
      this.$Modal.confirm({
        title: '警告',
        content: '确认删除直播间吗',
        onOk: () => {
          var params = new URLSearchParams()
          params.append('name', this.userInfo.username)
          params.append('classroom', a)
          axios.post('/api/user/delmyclass', params).then((resp) => {

          })
          Array.prototype.indexOf = function (val) {
            for (var i = 0; i < this.length; i++) {
              if (this[i] == val) return i
            }
            return -1
          }

          Array.prototype.remove = function (val) {
            var index = this.indexOf(val)
            if (index > -1) {
              this.splice(index, 1)
            }
          }
          this.items.remove(a)
        }
      })
      // 传给后端删除信息
    },

    skip: function (a) {
      //        this.$Modal.confirm({
      //          render: (h) => {
      //            return h('Input', {
      //              props: {
      //                id:'passinput',
      //                autofocus: true,
      //                placeholder: 'Please enter the password of this room'
      //              },
      //              on: {
      //                input: (val) => {
      /// /                this.value = val;
      //                  this.currentpassword=val;
      /// /                if(val==="123")
      /// /                  this.$router.push({path: 'living',query:{ id: a.vid}});
      //                }
      //              }
      //            })
      //          },
      //          onOk: () => {
      //            if(this.currentpassword=== a.password)
      this.$router.push({path: 'living', query: { id: a.vid}})
      //            else
      //              this.$Notice.error({
      //                title: '消息提示',
      //                desc: '您输入的密码错误，请仔细检查 '
      //              });
      //          }
      //        });
    },
    getList: function () {
      axios.post('/api/user/mylist', this.userInfo.username).then((resp) => {
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

  .addbutton{
    margin:10px;

  }
  .paixu{
      float:right;
      padding-right: 2%;
  }
  .addtext{
    test-align:left;
    font-size: 20px;
    font-style:normal;
    font-family:"Times New Roman", Times, serif;
  }
  .btns{
    float:left;
    padding-left: 2%;
  }
  .layout-footer-center{
    text-align: center;
    font-size:20px;
  }
  .listclass {
    padding-top: 2%;
    padding-left: 3%;
    padding-right: 3%;
    padding-bottom: 3%;
  }
  .delicon{
    float:right;
  }

  .listtext{
    test-align:left;
    font-size: 40px;
    font-style:normal;
    font-family:"Times New Roman", Times, serif;

  }
  .listbtn{
    test-align:left;
    font-size: 20px;
    font-style:normal;
    font-family:"Times New Roman", Times, serif;
    margin:10px;
  }
  .listbtns{
    float:left;
    width: 100%;

  }
  .oldlist{
    float:left;
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
</style>
