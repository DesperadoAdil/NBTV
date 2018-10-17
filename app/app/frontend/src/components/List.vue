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
              <!--<div class="aspectration" data-ratio="16:9">-->
                  <img :src="item.thumbnail" class="thumbnail" @click="skip(item)">
              <!--</div>-->
              <p class="title">{{ item.title }} </p>
              <p class="teacher">授课老师：{{ item.teacher }} </p>
              <p class="audiencenum">当前人数：{{ item.audiencelist.length}}</p>
              <p class="audiencenum">开播时间：{{ item.createtime}}</p>
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
	  data :function() {
	    return {
        currentpassword:"",
        imgwitd:"100px",
				items: [
					{
						id: '1',
						teacher: 'zsh',
						title: 'math',
						thumbnail: require('../assets/logo.png'),
						password: '123',
						url: '',
						studentlist: '',
						teacherlist: '',
						audiencelist: [1,5,6,21,321,43],
						visible: '',
            vid:'242544',
            createtime:'2018-10-18 13:37:05'

					},
          {
            id: '2',
            teacher: 'zsh',
            title: 'math',
            thumbnail: require('../assets/logo.png'),
            password: '123',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: [1,5,6],
            visible: '',
            vid:'242544',
            createtime:'2018-10-19 13:37:06'
          },
          {
            id: '3',
            teacher: 'zsh',
            title: 'math',
            thumbnail:require( '../assets/logo.png'),
            password: '123',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: [1,5,6,12,2,2,2,2,2,2,2,2,2,2],
            visible: '',
            vid:'242544',
            createtime:'2018-10-20 13:37:15'
          },
          {
            id: '1',
            teacher: 'zsh',
            title: 'math',
            thumbnail: require('../assets/logo.png'),
            password: '123',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: [1,5,6,21,32,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            visible: '',
            vid:'242544',
            createtime:'2018-11-17 13:47:05'
          },
          {
            id: '2',
            teacher: 'zsh',
            title: 'math',
            thumbnail: require('../assets/logo.png'),
            password: '123',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: [1,5,6,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            visible: '',
            vid:'242544',
            createtime:'2018-10-07 13:37:05'
          },
          {
            id: '3',
            teacher: 'zsh',
            title: 'math',
            thumbnail:require( '../assets/logo.png'),
            password: '123',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: [1,5,6,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            visible: '',
            vid:'242544',
            createtime:'2018-11-17 13:37:05'
          },
          {
            id: '1',
            teacher: 'zsh',
            title: 'math',
            thumbnail:'should be some url',
            password: '123',
            url: '',
            studentlist: '',
            teacherlist: '',
            audiencelist: [1,5,6,3,3,3,3,3,3,3,3,3,3,3],
            visible: '',
            vid:'242544',
            createtime:'2018-4-17 13:37:05'
          },
				]

	    }
	  },
		created:function() {
			this.getList();
		},
		methods: {
      timelist:function(){

        var compare = function (obj1, obj2) {
          var val1 = obj1.createtime;
          var val2 = obj2.createtime;
          var datas1=val1.split(" ");
          var datas2=val2.split(" ");

          var date1 = datas1[0].split("-");
          var date2 = datas2[0].split("-");

          var time1 = datas1[1].split(":");
          var time2 = datas2[1].split(":");
          console.log(parseInt(date1[0]));
          if (parseInt(date1[0]) <parseInt(date2[0])) {
            return -1;
          } else if (parseInt(date1[0]) >parseInt(date2[0])) {
            return 1;
          } else {
            if (parseInt(date1[1]) <parseInt(date2[1])) {
              return -1;
            } else if (parseInt(date1[1]) >parseInt(date2[1])) {
              return 1;
            } else {
              if (parseInt(date1[2]) <parseInt(date2[2])) {
                return -1;
              } else if (parseInt(date1[2]) >parseInt(date2[2])) {
                return 1;
              } else {
                if (parseInt(time1[0]) <parseInt(time2[0])) {
                  return -1;
                } else if (parseInt(time1[0]) >parseInt(time2[0])) {
                  return 1;
                } else {
                  if (parseInt(time1[1]) <parseInt(time2[1])) {
                    return -1;
                  } else if (parseInt(time1[1]) >parseInt(time2[1])) {
                    return 1;
                  } else {
                    if (parseInt(time1[2]) <parseInt(time2[2])) {
                      return -1;
                    } else if (parseInt(time1[2]) >parseInt(time2[2])) {
                      return 1;
                    } else {
                      return 0;
                    }
                  }
                }
              }

            }
          }



          if (val1 < val2) {
            return -1;
          } else if (val1 > val2) {
            return 1;
          } else {
            return 0;
          }


        };
        this.items.sort(compare);
        this.$Notice.success({
          title: '消息提示',
          desc: '已经按照时间排序'
        });
      },
      audiencelist:function(){

        var compare = function (obj1, obj2) {
          var val1 = obj1.audiencelist.length;
          var val2 = obj2.audiencelist.length;
          if (val1 > val2) {
            return -1;
          } else if (val1 < val2) {
            return 1;
          } else {
            return 0;
          }
        };
        this.items.sort(compare);
        this.$Notice.success({
          title: '消息提示',
          desc: '已经按照热度排序'
        });
      },

      skip:function(a){
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
			getList:function() {
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
</style>
