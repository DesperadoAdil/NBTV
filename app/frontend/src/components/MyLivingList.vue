<template>
  <div id="myLivingList" class="posi">
    <h1 class="list-info">
      <Icon type="ios-time" />
      我的直播
      <Button type="primary" @click="addModal = true">新建直播间</Button>
    </h1>
    <Divider />
    <Modal
      :model="newLiving"
      v-model="addModal"
      title="添加课程"
      @on-ok="addLiving()"
      @on-cancel="cancel">
      <Input v-model="newLiving.title" placeholder="课程名称"></Input>
      <Input v-model="newLiving.thumbnail" placeholder="缩略图（待修改）"></Input>
      <a href="javascript:;" class="upf">上传缩略图
        <input type="file" name="fileinput" id="fileinput">
      </a>
      <!--<input  type="file" value="上传图片" placeholder="缩略图（待修改）"></input>-->
      <Input v-model="newLiving.url" placeholder="课程url"></Input>
      <Input v-model="newLiving.class_password" placeholder="课程密码（可空）"></Input>
      <Select v-model="newLiving.mode">课程Mode
        <Option v-for="item in modeList" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
    </Modal>
    <Row>
      <Col span="8" v-for="(living, index) in myLivingList" :key="living.url">
          <Card class="living-card">
            <img :src="living.thumbnail" class="thumbnail"  @click="directskip(living)">
            <p class="title">{{ living.title }}</p>
            <span><Button type="success" @click="getBackUp(index)">UPDATE</Button></span>
            <Modal
              v-model="updateModal"
              title="更新课程"
              @on-ok="updateLiving(index)"
              @on-cancel="cancel">
              <Input v-model="living.title" placeholder="课程名称"></Input>
              <Input v-model="living.thumbnail" placeholder="缩略图（待修改）"></Input>
              <Input v-model="living.url" placeholder="课程url"></Input>
              <Input v-model="living.class_password" placeholder="课程密码（可空）"></Input>
            </Modal>
            <span><Button type="error" @click="deleteModal = true">DELETE</Button></span>
            <Modal
              v-model="deleteModal"
              title="删除课程"
              @on-ok="deleteLiving(index)"
              @on-cancel="cancel">
              <Input v-model="validate" placeholder="确认删除请输入yes"></Input>
            </Modal>
          </Card>
      </Col>
    </Row>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      validate: '',
      newLiving: {
        username: '',
        password: '',
        job: '',
        title: '',
        thumbnail: '',
        img:'',
        url: '',
        class_password: '',
        mode: ''
      },
      modeList: [
        {
          value: 'private',
          label: '只有我的学生能看到'
        },
        {
          value: 'protected',
          label: '有密码就可以进入'
        },
        {
          value: 'public',
          label: '公开课'
        }
      ],
      addModal: false,
      updateModal: false,
      deleteModal: false,
      myLivingList: [{
        username: '',
        password: '',
        job: '',
        old_url: '',
        title: '',
        thumbnail: '../assets/logo.png',
        url: '1',
        class_password: ''
      },{},{},{},{}],
      userInfo: {
        username: '',
        password: '',
        mobile: '',
        status: '',
        job: ''
      }
    }
  },
  created () {
    this.getMyLivingList()
  },
  methods: {
    directskip (living) {
      this.$router.push({path: '/teacherliving/' + living.url, params: {url: living.url}})
      this.$Modal.confirm({
        title: '提示',
        content: '是否确认进入直播间',
        onOk: () => {
          window.location.reload()
        },
        onCancel: () => {
          history.go(-1)
        }
      })
    },
    getBackUp (index) {
      this.updateModal = true
      this.myLivingList[index]['old_url'] = this.myLivingList[index]['url']
    },
    getMyLivingList () {
      this.userInfo['username'] = this.$cookies.get('user').username
      this.userInfo['status'] = this.$cookies.get('user').status
      this.userInfo['job'] = this.$cookies.get('user').job
      this.userInfo['password'] = this.$cookies.get('user').password
      this.userInfo['mobile'] = this.$cookies.get('user').mobile
      const data = this.userInfo
      axios.post('/api/classroom/user_living_list', data).then((resp) => {
        this.myLivingList = []
        for (var i = 0; i < resp.data.length; i++) {
          var living = {}
          living['title'] = resp.data[i]['title']
          living['url'] = resp.data[i]['url']
          living['thumbnail'] = resp.data[i]['thumbnail']
          living['class_password'] = resp.data[i]['password']
          living['mode'] = resp.data[i]['mode']
          this.myLivingList.push(living)
        }
      })
    },
    addLiving () {
        var formData = new FormData()
        formData.append('username', this.$cookies.get('user').username)
        formData.append('password', this.$cookies.get('user').password)
        formData.append('job', this.$cookies.get('user').job)
        formData.append('img', document.querySelector('input[type=file]').files[0])
          var options = {
          url: '/api/classroom/add_class',
          data: formData,
          method: 'post',
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
        axios(options).then((resp) => {
          this.getMyLivingList()
      })
      console.log(document.querySelector('input[type=file]').files[0])
      this.addModal = false
//      this.newLiving['username'] = this.$cookies.get('user').username
//      this.newLiving['password'] = this.$cookies.get('user').password
//      this.newLiving['job'] = this.$cookies.get('user').job
//      console.log("1231")
//      this.newLiving['img']=document.querySelector('input[type=file]').files[0]
//      console.log("1231")
      console.log(document.querySelector('input[type=file]').files[0])
//      console.log("4564")
//      const data = this.newLiving
//      axios.post('/api/classroom/add_class', data).then((resp) => {
//        this.getMyLivingList()
//      })
    },
    updateLiving (index) {
      this.myLivingList[index]['username'] = this.$cookies.get('user').username
      this.myLivingList[index]['password'] = this.$cookies.get('user').password
      this.myLivingList[index]['job'] = this.$cookies.get('user').job
      const data = this.myLivingList[index]
      axios.post('/api/classroom/update_class', data).then((resp) => {
        this.getMyLivingList()
      })
      this.updateModal = false
    },
    deleteLiving (index) {
      this.myLivingList[index]['username'] = this.$cookies.get('user').username
      this.myLivingList[index]['password'] = this.$cookies.get('user').password
      this.myLivingList[index]['job'] = this.$cookies.get('user').job
      const data = this.myLivingList[index]
      if (this.validate === 'yes') {
        axios.post('/api/classroom/delete_class', data).then((resp) => {
          this.getMyLivingList()
        })
      }
      this.deleteModal = false
    },
    cancel () {
      this.$Message.info('Clicked cancel')
      this.addModal = false
      this.updateModal = false
      this.deleteModal = false
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
.living-card {
  padding: 3%;
  margin: 6%;
}
.posi{
  position: absolute;
  top: 60px;
}
.upf {
  position: relative;
  display: inline-block;
  background: #D0EEFF;
  border: 1px solid #99D3F5;
  border-radius: 4px;
  padding: 4px 12px;
  overflow: hidden;
  color: #1E88C7;
  text-decoration: none;
  text-indent: 0;
  line-height: 20px;
}
.upf input {
  position: absolute;
  font-size: 100px;
  right: 0;
  top: 0;
  opacity: 0;
}
.upf:hover {
  background: #AADFFD;
  border-color: #78C3F3;
  color: #004974;
  text-decoration: none;
}
</style>
