<template>
  <div id="myLivingList">
    <Button type="primary" @click="addModal = true">ADD</Button>
    <Modal
      v-model="addModal"
      title="添加课程"
      @on-ok="addLiving()"
      @on-cancel="cancel">
      <Input v-model="newLiving.title" placeholder="课程名称"></Input>
      <Input v-model="newLiving.thumbnail" placeholder="缩略图（待修改）"></Input>
      <Input v-model="newLiving.url" placeholder="课程url"></Input>
      <Input v-model="newLiving.password" placeholder="课程密码（可空）"></Input>
    </Modal>
    <div v-for="living in myLivingList">
      <Card class="card">
        <img :src="living.thumbnail" class="thumbnail">
        <p class="title">{{ item.title }}</p>
        <span><Button type="success" @click="updateModal = true">UPDATE</Button></span>
        <Modal
          v-model="updateModal"
          title="更新课程"
          @on-ok="ok"
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
          @on-ok="ok"
          @on-cancel="cancel">
          <Input v-model="validate" placeholder="确认删除请输入yes"></Input>
        </Modal>
      </Card>
    </div>
  </div>
</template>
<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        validate: '',
        newLiving: {
          title: '',
          thumbnail: '',
          url: '',
          password: ''
        },
        addModal: false,
        updateModal: false,
        deleteModal: false,
        myLivingList: [{
          title: '111',
          thumbnail: '111',
          url: '111',
          password: '111'
        },],
        userInfo: {
          username: '',
          password: '',
          mobile: '',
          status: '',
        },
      }
    },
    created() {
      this.getMyLivingList();
    },
    methods: {
      getMyLivingList() {
        axios.post("/api/list/user_living_list", data).then((resp) => {

        })
      },
      addLiving() {

        addModal = false;
      },
      updateLiving() {
        axios.post("/api/", data).then((resp) => {

        })
        updateModal = false;
      },
      deleteLiving() {
        if (validate === 'yes') {
          axios.post("/api/", data).then((resp) => {

          })
        }
        deleteModal = false;
      },
      cancel() {
        this.$Message.info('Clicked cancel');
        addModal = false;
        updateModal = false;
        deleteModal = false;
      }
    }
  }
</script>
