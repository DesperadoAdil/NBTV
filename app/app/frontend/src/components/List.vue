<template>
	<div id="list">
    <Layout class="layoutlist">
      <Header>
          <ButtonGroup class="btns" size="large" shape="circle" vertical="false">
            <Tooltip placement="top">
              <Button class="addbutton" size="large" type="primary"  shape="circle" icon="md-add" ></Button>
              <div slot="content">
                <p class="addtext">新建直播间</p>
              </div>
            </Tooltip>
            <Tooltip placement="top">
              <Button class="addbutton" size="large" type="primary"  shape="circle" icon="md-help"></Button>
              <div slot="content">
                <p class="addtext">待创建功能</p>
              </div>
            </Tooltip>
          </ButtonGroup>
      </Header>
      <Content class="listclass">



        <ButtonGroup  >
        <!--<ButtonGroup class="listbtns">-->
          <Button class="listtext" type="text" >在线直播</Button>
          <Button class="listbtn" type="primary" shape="circle" @click="timelist">按开播时间排列</Button>
          <Button class="listbtn" type="primary" shape="circle" @click="audiencelist">按观众人数排序</Button>
        </ButtonGroup>

        <Row>
          <Col span="8" v-for="item in items">
            <Card class="card">
              <img :src="item.thumbnail" class="thumbnail" @click="skip(item)">

              <p class="title">{{ item.title }} </p>
              <p class="teacher">授课老师：{{ item.teacher }} </p>
              <p class="audiencenum">当前人数：{{ item.audiencenum }}</p>
            </Card>
          </Col>
        </Row>



        <!--<ul class="oldlist">-->
          <!--<li  v-for="item in items">-->
            <!--<Card class="card" >-->
              <!--<img :src="item.thumbnail" class="thumbnail" @click="skip(item)">-->
              <!--<div class="classroomDetail" style="text-align:center">-->
						<!--<span class="title">-->
							<!--{{ item.title }}-->
						<!--</span>-->
						<!--<span class="teacher">-->
							<!--{{ item.teacher }}-->
						<!--</span>-->
						<!--<span class="audience">-->
							<!--{{ item.audiencenum }}-->
						<!--</span>-->
              <!--</div>-->
            <!--</Card>-->
          <!--</li>-->
        <!--</ul>-->
      </Content>
      <Footer class="layout-footer-center">2018-? &copy; SitTillGraduation</Footer>

    </Layout>




	</div>

</template>
<script>
	import axios from 'axios';
	export default {
	  name: 'List',
	  data () {
	    return {
        currentpassword:"",

				items: [
					{
						id: '1',
						teacher: 'zsh',
						title: 'math',
						thumbnail: require('../assets/logo.png'),
						password: '',
						url: '',
						studentlist: '',
						teacherlist: '',
						audiencelist: '',
						visible: '',
            audiencenum:'10',
            vid:'242544',
            password:'123'
					},
          {
            id: '2',
            teacher: 'zsh',
            title: 'math',
            thumbnail: require('../assets/logo.png'),
            password: '',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: '',
            visible: '',
            audiencenum:'20',
            vid:'242544',
            password:'123'
          },
          {
            id: '3',
            teacher: 'zsh',
            title: 'math',
            thumbnail:require( '../assets/logo.png'),
            password: '',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: '',
            visible: '',
            audiencenum:'30',
            vid:'242544',
            password:'123'
          },
          {
            id: '1',
            teacher: 'zsh',
            title: 'math',
            thumbnail: require('../assets/logo.png'),
            password: '',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: '',
            visible: '',
            audiencenum:'10',
            vid:'242544',
            password:'123'
          },
          {
            id: '2',
            teacher: 'zsh',
            title: 'math',
            thumbnail: require('../assets/logo.png'),
            password: '',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: '',
            visible: '',
            audiencenum:'20',
            vid:'242544',
            password:'123'
          },
          {
            id: '3',
            teacher: 'zsh',
            title: 'math',
            thumbnail:require( '../assets/logo.png'),
            password: '',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: '',
            visible: '',
            audiencenum:'30',
            vid:'242544',
            password:'123'
          },
          {
            id: '1',
            teacher: 'zsh',
            title: 'math',
            thumbnail:'should be some url',
            password: '',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: '',
            visible: '',
            audiencenum:'10',
            vid:'242544',
            password:'123'
          },
				]

	    }
	  },
		created() {
			this.getList();
		},
		methods: {
      timelist(){
        axios.get('/api/timelist').then((resp) => {
          console.log(resp)
          this.items = resp.data;
        })
        this.$Notice.success({
          title: '消息提示',
          desc: '已经按照时间排序'
        });
      },
      audiencelist(){
        axios.get('/api/audiencelist').then((resp) => {
          console.log(resp)
          this.items = resp.data;
        })
        this.$Notice.success({
          title: '消息提示',
          desc: '已经按照热度排序'
        });
      },

      skip(a){
        this.$Modal.confirm({
              render: (h) => {
              return h('Input', {
                props: {
                  id:'passinput',
                  autofocus: true,
                  placeholder: 'Please enter the password of this room'
                },
                on: {
                  input: (val) => {
//                this.value = val;
                this.currentpassword=val;
//                if(val==="123")
//                  this.$router.push({path: 'living',query:{ id: a.vid}});
              }
            }
          })
        },
        onOk: () => {
            if(this.currentpassword=== a.password)
                this.$router.push({path: 'living',query:{ id: a.vid}});
            else
              this.$Notice.error({
                      title: '消息提示',
                      desc: '您输入的密码错误，请仔细检查 '
                    });
              }
            });

      },
			getList() {
				axios.get('/api/list').then((resp) => {
					console.log(resp)
					this.items = resp.data;
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


  .addbutton{
    margin:10px;

  }
  .addtext{
    test-align:left;
    font-size: 20px;
    font-style:normal;
    font-family:"Times New Roman", Times, serif;
  }
  .btns{
    float:left;
  }
  .layout-footer-center{
    text-align: center;
    font-size:20px;
  }
  .listclass{
    padding-top: 3%;
    padding-left: 5%;
    padding-right: 5%;
    padding-bottom: 3%;


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
  .card {
    padding: 3%;
    margin: 6%;
  }
  .thumbnail {
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
</style>
