<template>
  <div id="myLivingList" class="posi">
    <Button type="primary" @click="addModal = true">ADD</Button>
    <Modal
      :model="newLiving"
      v-model="addModal"
      title="添加课程"
      @on-ok="addLiving()"
      @on-cancel="cancel">
      <Input v-model="newLiving.title" placeholder="课程名称"></Input>
      <Input v-model="newLiving.thumbnail" placeholder="缩略图（待修改）"></Input>
      <Input v-model="newLiving.url" placeholder="课程url"></Input>
      <Input v-model="newLiving.password" placeholder="课程密码（可空）"></Input>
    </Modal>
    <div v-for="(living, index) in myLivingList" :key="living.url">
      <Card class="card">
        <img :src="living.thumbnail" class="thumbnail"  @click="directskip(teacherliving)">
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
          <Input v-model="living.password" placeholder="课程密码（可空）"></Input>
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
    </div>
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
        url: '',
        class_password: ''
      },
      addModal: false,
      updateModal: false,
      deleteModal: false,
      myLivingList: [{
        username: '',
        password: '',
        job: '',
        old_url: '',
        title: '',
        thumbnail: '',
        url: '',
        class_password: ''
      }],
      userInfo: {
        username: '',
        password: '',
        mobile: '',
        status: ''
      }
    }
  },
  created () {
    this.getMyLivingList()
  },
  methods: {
    directskip (teacherliving) {
      this.$router.push({path: 'teacherliving'})
    },
    getBackUp (index) {
      this.updateModal = true
      this.myLivingList[index]['old_url'] = this.myLivingList[index]['url']
    },
    getMyLivingList () {
      const data = this.myLivingList
      axios.post('/api/classroom/user_living_list', data).then((resp) => {
        this.myLivingList = resp.data
      })
    },
    addLiving () {
      this.addModal = false
      this.newLiving['username'] = this.$cookies.get('user').username
      this.newLiving['password'] = this.$cookies.get('user').password
      this.newLiving['job'] = this.$cookies.get('user').job
      const data = this.newLiving
      axios.post('/api/list/add_class', data).then((resp) => {
        this.getMyLivingList()
      })
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
.card {
  width: 320px;
  height: 200px;
}
.posi{
  position: absolute;
  top: 60px;
}
</style>
