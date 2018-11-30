<template>
  <div id="myLivingList" class="posi">
    <h1 class="list-info">
      <Icon type="ios-time" />
      我的直播
    </h1>
    <Divider />
    <h2 class="list-info">
      <Button type="primary" @click="readyToAdd">新建直播间</Button>
    </h2>
    <Modal
      :model="newLiving"
      v-model="addModal"
      title="添加课程"
      @on-ok="addLiving()"
      @on-cancel="cancel">
      <Form :model="newLiving" :label-width="80">
        <FormItem label="课程名称">
          <Input v-model="newLiving.title" placeholder="给自己的课程起一个好听的名字吧"></Input>
        </FormItem>
        <a href="javascript:;" class="upf">上传封面
          <input type="file" name="fileinput" id="fileinput" accept="image/gif, image/jpeg, image/png, image/jpg">
        </a>
        <output id="list"></output>
        <FormItem label="课程URL">
          <Input v-model="newLiving.url" placeholder="课程url"></Input>
        </FormItem>
        <FormItem label="课程Mode">
          <Select v-model="newLiving.mode">
            <Option v-for="item in modeList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </FormItem>
        <FormItem label="课程密码" v-if="newLiving.mode === 'protected' || newLiving.mode === 'private'" >
          <Input  v-model="newLiving.class_password" placeholder="课程密码"></Input>
        </FormItem>
      </Form>

    </Modal>
    <Row class="myLivingList-flex-container">
      <Col span="8" v-for="(living, index) in myLivingList" :key="living.url">
        <card class="myLivingList-flex-item" >
          <img :src="living.thumbnail" class="thumbnail" @click="directskip(living)">
          <p class="my-class-title">{{ living.title }}</p>
          <span><Button type="success" @click="getBackUp(index)">更新课程</Button></span>
          <Modal
            v-model="updateModal"
            title="更新课程基本信息"
            @on-ok="updateLiving(modalIndex)"
            @on-cancel="cancel">
            <Form :model="myLivingList[modalIndex]" :label-width="80">
              <FormItem label="课程名称">
                <Input v-model="myLivingList[modalIndex].title" placeholder="课程名称"></Input>
              </FormItem>
              <a href="javascript:;" class="upf">上传封面
                <input type="file" name="fileinput" id="filezsh2" accept="image/gif, image/jpeg, image/png, image/jpg">
              </a>
              <output id="listUp"></output>
              <FormItem label="课程URL">
                <Input v-model="myLivingList[modalIndex].url" placeholder="课程URL"></Input>
              </FormItem>
              <FormItem label="课程密码" v-if="myLivingList[modalIndex].mode === 'protected' || myLivingList[modalIndex].mode === 'private'" >
                <Input v-model="myLivingList[modalIndex].class_password" placeholder="课程密码"></Input>
              </FormItem>
            </Form>
          </Modal>
          <span><Button type="error" @click="getBackUpForDel(index)">删除课程</Button></span>
          <Modal
            v-model="deleteModal"
            title="删除课程"
            @on-ok="deleteLiving(modalIndex)"
            @on-cancel="cancel">这将永久删除您的直播间，确认删除请输入yes
            <Input v-model="validate"></Input>
          </Modal>
        </card>
      </Col>
    </Row>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      modalIndex: 0,
      validate: '',
      newLiving: {
        username: '',
        password: '',
        job: '',
        title: '',
        thumbnail: '',
        img: '',
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
      myLivingList: [],
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
//      this.$Modal.confirm({
//        title: '提示',
//        content: '是否确认进入直播间',
//        onOk: () => {
//          window.location.reload()
//        },
//        onCancel: () => {
//          history.go(-1)
//        }
//      })
    },
    readyToAdd () {
      document.getElementById('fileinput').addEventListener('change', this.handleFileSelect, false)
      this.addModal = true
    },
    getBackUp (index) {
      this.modalIndex = index
      this.updateModal = true
      this.myLivingList[index]['old_url'] = this.myLivingList[index]['url']
      document.getElementById('filezsh2').addEventListener('change', this.handleFileSelectForUp, false)
    },
    getBackUpForDel (index) {
      this.modalIndex = index
      this.deleteModal = true
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
        for (let i = 0; i < resp.data.length; i++) {
          const living = {}
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
      formData.append('img', document.querySelector('input[id=fileinput]').files[0])
      formData.append('title', this.newLiving.title)
      formData.append('url', this.newLiving.url)
      formData.append('class_password', this.newLiving.class_password)
      formData.append('mode', this.newLiving.mode)
      var options = {
        url: '/api/classroom/add_class',
        data: formData,
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axios(options).then((resp) => {
        if (resp.data.status !== 'success') {
          this.$Message.error(resp.data.status)
        }
        this.getMyLivingList()
      })

      this.addModal = false
    },
    updateLiving (index) {
      var fileInput00 = document.getElementById('filezsh2')
      var formData = new FormData()
      formData.append('username', this.$cookies.get('user').username)
      formData.append('password', this.$cookies.get('user').password)
      formData.append('job', this.$cookies.get('user').job)
      formData.append('img', document.querySelector('input[id=filezsh2]').files[0])
      formData.append('title', this.myLivingList[index]['title'])
      formData.append('url', this.myLivingList[index]['url'])
      formData.append('class_password', this.myLivingList[index]['class_password'])
      formData.append('mode', this.myLivingList[index]['mode'])
      formData.append('old_url', this.myLivingList[index]['old_url'])
      var options = {
        url: '/api/classroom/update_class',
        data: formData,
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axios(options).then((resp) => {
        if (resp.data.status !== 'success') {
          this.$Message.error(resp.data.status)
        }
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
    },
    handleFileSelect (evt) {
      var files = evt.target.files // FileList object

      // Loop through the FileList and render image files as thumbnails.
      for (var i = 0, f; f = files[i]; i++) {
        // Only process image files.
        if (!f.type.match('image.*')) {
          continue
        }

        var reader = new FileReader()

        // Closure to capture the file information.
        reader.onload = (function (theFile) {
          return function (e) {
            // Render thumbnail.
            var span = document.createElement('span')
            span.innerHTML = ['<img class="thumb" style="height:100px" src="', e.target.result,
              '" title="', escape(theFile.name), '"/>'].join('')
            document.getElementById('list').insertBefore(span, null)
          }
        })(f)

        // Read in the image file as a data URL.
        reader.readAsDataURL(f)
      }
    },
    handleFileSelectForUp (evt) {
      var files = evt.target.files // FileList object

      // Loop through the FileList and render image files as thumbnails.
      for (var i = 0, f; f = files[i]; i++) {
        // Only process image files.
        if (!f.type.match('image.*')) {
          continue
        }

        var reader = new FileReader()

        // Closure to capture the file information.
        reader.onload = (function (theFile) {
          return function (e) {
            // Render thumbnail.
            var span = document.createElement('span')
            span.innerHTML = ['<img class="thumb" style="height:100px" src="', e.target.result,
              '" title="', escape(theFile.name), '"/>'].join('')
            document.getElementById('listUp').insertBefore(span, null)
          }
        })(f)

        // Read in the image file as a data URL.
        reader.readAsDataURL(f)
      }
    }

  }
}
</script>
<style>
.myLivingList-flex-container {
  padding: 0;
  margin: 0;
  list-style: none;

  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;

  -webkit-flex-flow: row wrap;
}
li {
  list-style: none;

}
.myLivingList-flex-item {
  padding: 3%;
  margin: 6%;
}
#myLivingList {
  padding: 0 5%;
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
.my-class-title {
  font-size: 20px;
  text-align: left;
}
</style>
