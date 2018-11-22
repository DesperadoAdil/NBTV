<template>
  <div id="teacherLiving" class="tealivingmain">
    <div  class="cardtea">
      <!-- -----------侧边栏----------------- -->
      <Menu name="sidemenu" style="width: 100%">

        <!-- 资源 -->
        <Submenu name="post" class="menuitentea">
          <template slot="title" ><Icon type="ios-paper" />
            资源
          </template>
          <MenuItem @click.native="showPdfList()">PDF课件</MenuItem>
          <MenuItem @click.native="showMultiList()">选择题</MenuItem>
          <MenuItem @click.native="showCodeList()">代码题</MenuItem>
        </Submenu>
        <!-- 资源 -->

        <!-- 添加 -->
        <Submenu name="add" class="menuitentea">
          <template slot="title" ><Icon type="ios-paper" />
            添加
          </template>
          <MenuItem @click.native="modal_pdf = true">PDF课件</MenuItem>
          <MenuItem @click.native="create_multi()">选择题</MenuItem>
          <MenuItem @click.native="create_code()">代码题</MenuItem>
        </Submenu>
        <!-- 添加 -->

        <!-- 使用 -->
        <Submenu name="cancel" class="menuitentea">
          <template slot="title"><Icon type="ios-people" />
            使用
          </template>
          <MenuItem @click.native="closetext()">取消使用</MenuItem>
        </Submenu>
        <!-- 使用 -->

        <!-- 学生 -->
        <Submenu name="student" class="menuitentea"  >
          <template slot="title"><Icon type="ios-stats" />
            学生
          </template>
          <MenuItem @click.native="getstudents">学生列表</MenuItem>
          <MenuItem @click.native="addStudentByExcel">xlsx文档添加</MenuItem>
          <MenuItem @click.native="addStudent()">用户名添加</MenuItem>
          <MenuItem @click.native="getShutUpList()">解除禁言</MenuItem>
        </Submenu>
        <!-- 学生 -->
      </Menu>
      <!-- -----------侧边栏----------------- -->

      <!-- 底部按钮：开播、关播、关麦 -->
      <Button class="btnopen" type="primary"  v-bind:icon="openclose"  @click="teaopenclose()">
        <span class="menuitentea">{{this.opentext}}</span>
      </Button>
      <Button type="primary" shape="circle" v-bind:icon="jinmai" @click="tojinmai"></Button>
      <Button type="primary" shape="circle" v-bind:icon="jinshipin" @click="tojinshipin()"></Button>
    </div>

    <!-------------Modal of the menus----------------->
    <!--PDFlist-->
    <Modal
      v-model="modal_pdflist" width="900"
    >
      <div>
        <Split class="teacher-live-split" style="height: 430px" v-model="split_pdf">
          <div slot="left"  class="teacher-live-split-pane">
            <p>全部PDF课件</p>
            <br>
            <Table height="345" border :columns="pdfAll" :data="pdfAllList"></Table>
            <p>点击添加：将课件添加至教室资源</p>
            <p>点击删除：从全部课件中删除课件</p>
          </div>
          <div slot="right"  class="teacher-live-split-pane">
            <p>本教室资源</p>
            <br>
            <Table height="345" border :columns="pdfThis" :data="pdfThisList"></Table>
            <p>点击使用：在当前教室中使用课件</p>
            <p>点击删除：从当前教室中删除课件</p>
          </div>
        </Split>
      </div>
      <div slot="footer">
        <Row>
          将已有资源添加至当前教室中，之后点击使用以发布教学资源
          <Button type="text" size="large" @click="modal_pdflist = false">关闭</Button>
        </Row>
      </div>
    </Modal>

    <!--multi_list-->
    <Modal v-model="modal_multilist" width="900">
      <div>
        <Split class="teacher-live-split" style="height: 430px" v-model="split_multi">
          <div slot="left"  class="teacher-live-split-pane">
            <p>全部选择题</p>
            <br>
            <Table height="345" border :columns="multiAll" :data="multiAllList"></Table>
            <p>点击添加：将题目添加至教室资源; 点击编辑：在全部课件中编辑题目</p>
            <p>点击删除：从全部课件中删除题目</p>
          </div>
          <div slot="right"  class="teacher-live-split-pane">
            <p>本教室资源</p>
            <br>
            <Table height="345" border :columns="multiThis" :data="multiThisList"></Table>
            <p>点击使用：在当前教室中使用题目; 点击查看：查看当前题目答题情况</p>
            <p>点击删除：从当前教室中删除题目</p>
          </div>
        </Split>
      </div>
      <div slot="footer">
        <Row>
          将已有资源添加至当前教室中，之后点击使用以发布教学资源
          <Button type="text" size="large" @click="modal_multilist = false">关闭</Button>
        </Row>
      </div>
    </Modal>

    <!--code_list-->
    <Modal v-model="modal_codelist" width="900">
      <div>
        <Split class="teacher-live-split" style="height: 430px" v-model="split_code">
          <div slot="left"  class="teacher-live-split-pane">
            <p>全部代码题</p>
            <br>
            <Table height="345" border :columns="codeAll" :data="codeAllList"></Table>
            <p>点击添加：将题目添加至教室资源; 点击编辑：在全部课件中编辑题目</p>
            <p>点击删除：从全部课件中删除题目</p>
          </div>
          <div slot="right"  class="teacher-live-split-pane">
            <p>本教室资源</p>
            <br>
            <Table height="345" border :columns="codeThis" :data="codeThisList"></Table>
            <p>点击使用：在当前教室中使用题目; 点击查看：查看当前题目答题情况</p>
            <p>点击删除：从当前教室中删除题目</p>
          </div>
        </Split>
      </div>
      <div slot="footer">
        <Row>
          将已有资源添加至当前教室中，之后点击使用以发布教学资源
          <Button type="text" size="large" @click="modal_codelist = false">关闭</Button>
        </Row>
      </div>
    </Modal>

    <!--上传-->
    <Modal v-model="modal_pdf">
      <p slot="header">
        <span>上传课件</span>
      </p>
      <Form>
        <FormItem>
          <a href="javascript:;">
            <input type="file" name="pdfinput" id="pdfinput" value="pdf upload">
          </a>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="addPDF()">submit</Button>
        </FormItem>
      </Form>
      <div slot="footer">
        <Button type="text" size="large" @click="modal_pdf = false">取消</Button>
      </div>
    </Modal>

    <!--设置选择题-->
    <Modal   v-model="modal_multi"    @on-ok="addMulti()"    @on-cancel="modal_multi = false">
      <p slot="header">
        <span>设置选择题</span>
      </p>
      <Form ref="multi" model="sub_multi" label-width="80" style="width: 300px">
        <FormItem label="题目描述">
          <Input type="textarea" v-model="sub_multi.statement" placeholder="输入你的选择题描述"></Input>
        </FormItem>
        <!-- 以下为选项的动态添加删除  -->
        <FormItem
          v-for="(item, index) in multi_options"
          v-if="item.status"
          :key="index">
          <Row>
            <Col span="18">
              <Input type="text" placeholder="输入选项" v-model="multi_options[index].value"></Input>
            </Col>
            <Col span="4" offset="1">
              <Button @click="multi_delChoice(index)">删除</Button>
            </Col>
          </Row>
        </FormItem>
        <FormItem>
          <Row>
            <Col span="12">
              <Button type="dashed" long @click="multi_addChoice()" icon="md-add">添加选项</Button>
            </Col>
          </Row>
        </FormItem>
        <!-- 答案设置  -->
        <FormItem label="答案">
          <Input v-model="sub_multi.answer" placeholder="A/B/C/D/.."></Input>
        </FormItem>
      </Form>
    </Modal>

    <!--设置编程题-->
    <Modal   v-model="modal_code"    @on-ok="addCode()"    @on-cancel="modal_code = false">
      <p slot="header">
        <span>设置编程题</span>
      </p>
      <Form label-position="top">
        <FormItem label="题目描述">
          <Input v-model="sub_code.statement"
                 type="textarea" rows="4"
                 placeholder="输入你的题目描述">
          </Input>
        </FormItem>
        <FormItem label="代码语言">
          <Select v-model="cmOption.mode">
            <Option value="python">python</Option>
            <Option value="text/x-c++src">cpp</Option>
          </Select>
        </FormItem>
        <FormItem label="示例代码">
          <template>
            <codemirror
              v-model="sub_code.example"
              :options="cmOption">
            </codemirror>
          </template>
            <!--<textarea-->
             <!--id="textarea1" name="textarea1">-->
            <!--</textarea>-->
        </FormItem>
      </Form>
    </Modal>

    <!--上传学生名单-->
    <Modal v-model="modal_student_xlsx">
      <p slot="header" style="font-size: 20px">
        <span>上传学生名单</span>
      </p>
      <Form>
        <Poptip word-wrap width="200" trigger="hover" title="提示" content="格式要求：xlsx文件的单元格填写一个完整的用户名，否则无效。添加失败可以再次添加或者用户名添加">
          <FormItem>
            <a href="javascript:;">
              <input type="file" name="xlsxinput" id="xlsxinput" value="上传Excel文件">
            </a>
          </FormItem>
        </Poptip>
        <FormItem>
          <Button @click="subxlsx()">提交</Button>
        </FormItem>
        <FormItem>
          <div v-for="student in studentitems" :key="student">
            {{ student }}
          </div>
        </FormItem>
      </Form>
      <div slot="footer">
        <Button type="text" size="large" @click="modal_student_xlsx = false">取消</Button>
      </div>
    </Modal>

    <!--view multi-->
    <Modal v-model="modal_viewmulti" width="900">
      <div>
        <Split class="teacher-live-split" style="height: 430px" v-model="split_multicheck">
          <div slot="left"  class="teacher-live-split-pane">
            <div style="position:relative; height:400px; overflow:auto">
            <Form ref="multi" model="sub_multi" label-width="80" style="width: 300px">
              <FormItem label="题目描述">
                {{sub_multi.statement}}
              </FormItem>
              <FormItem
                v-for="(item, index) in sub_multi.optionList"
                :key="index">
                {{String.fromCharCode(65+index)+" : "+item}}
              </FormItem>
              <FormItem label="答案">
                {{sub_multi.answer}}
              </FormItem>
            </Form>
            </div>
          </div>
          <div slot="right"  class="teacher-live-split-pane">
            <Table height="420" stripe :columns="multiAnswer" :data="multiAnswerList"></Table>
          </div>
        </Split>
      </div>
      <div slot="footer">
        <Button type="text" size="large" @click="modal_viewmulti = false">关闭</Button>
      </div>
    </Modal>

    <!--view code-->
    <Modal
      v-model="modal_viewcode"
      @on-ok="modal_viewcode = false"
      @on-cancel="modal_viewcode = false"
      width="900"
    >
      <Card>
        <Split class="teacher-live-split" style="height: 430px" v-model="split_codecheck">
          <div slot="left"  class="teacher-live-split-pane">
            <div style="position:relative; height:400px; overflow:auto">
              <Form label-position="top">
                <FormItem label="题目描述">
                  {{sub_code.statement}}
                </FormItem>
                <FormItem label="代码语言">
                  {{sub_code.language}}
                </FormItem>
                <FormItem label="示例代码">
                  <pre v-highlightjs="sub_code.example" height="100"><code class="cpp"></code></pre>
                </FormItem>
              </Form>
            </div>
          </div>
          <div slot="right"  class="teacher-live-split-pane">
            <div style="position:relative; height:400px; overflow:auto">
              <Form :label-width="40">
                <FormItem
                  v-for="(item, index) in codeAnswerList"
                  :key="index"
                  :label="item.student"
                  >
                  <pre v-highlightjs="item.answer" height="100"><code class="p"></code></pre>
                </FormItem>
              </Form>
            </div>
          </div>
        </Split>
      </Card>
    </Modal>

    <!--Edit 选择题--TODO: SUBMIT MULTI CHANGE-->
    <Modal   v-model="modal_editmulti"    @on-ok="submitMultiChange()"    @on-cancel="modal_editmulti = false">
      <p slot="header" style="font-size: 20px">
        <span>修改选择题</span>
      </p>
      <Form ref="multi" model="sub_multi" label-width="80" style="width: 300px">
        <FormItem label="题目描述">
          <Input type="textarea" v-model="sub_multi.statement" placeholder="输入你的题目描述"></Input>
        </FormItem>
        <!-- 以下为选项的动态添加删除  -->
        <FormItem
          v-for="(item, index) in multi_options"
          v-if="item.status"
          :key="index">
          <Row>
            <Col span="18">
              <Input type="text" placeholder="Enter Your Choice" v-model="multi_options[index].value"></Input>
            </Col>
            <Col span="4" offset="1">
              <Button @click="multi_delChoice(index)">删除</Button>
            </Col>
          </Row>
        </FormItem>
        <FormItem>
          <Row>
            <Col span="12">
              <Button type="dashed" long @click="multi_addChoice()" icon="md-add">添加选项</Button>
            </Col>
          </Row>
        </FormItem>
        <!-- 答案设置  -->
        <FormItem label="题目答案">
          <Input v-model="sub_multi.answer" placeholder="A/B/C/D/.."></Input>
        </FormItem>
      </Form>
    </Modal>

    <!--Edit 编程题--TODO: SUBMIT CODE CHANGE-->
    <Modal   v-model="modal_editcode"    @on-ok="submitCodeChange()"    @on-cancel="modal_editcode = false">
      <p slot="header" style="font-size: 20px">
        <span>设置编程题</span>
      </p>
      <Form label-position="top">
        <FormItem label="题目描述">
          <Input v-model="sub_code.statement"
                 type="textarea" rows="4"
                 placeholder="输入你的题目描述">
          </Input>
        </FormItem>
        <FormItem label="代码语言">
          <Select v-model="cmOption.mode">
            <Option value="python">python</Option>
            <Option value="text/x-c++src">cpp</Option>
          </Select>
        </FormItem>
        <FormItem label="示例代码">
          <template>
            <codemirror
              v-model="sub_code.example"
              :options="cmOption">
            </codemirror>
          </template>
        </FormItem>
      </Form>
    </Modal>

    <Modal v-model="modalStudentList" @on-ok="modalStudentList = false">
      <p slot="header">
        <span>学生名单</span>
      </p>
      <div v-for="student in studentitems" :key="student">
        {{ student }}
      </div>
    </Modal>

    <Modal v-model="shutUpModal" @on-ok="shutUpModal = false">
      <p slot="header">
        <span>禁言名单</span>
      </p>
      <div v-for="student in shutuplist" :key="student">
        {{ student }}
        <Button type="success" @click="noShutUp(student)">解禁</Button>
      </div>
    </Modal>

    <!---------main living 部分------------->
    <div  id="mainlivingcard" v-bind:class="classmain0 ? 'cardtealiving00' : 'cardtealittleliving00'" >
      <div class="topveido">
        <!--<h3>教室信息显示部分（待修改）</h3>-->
      </div>
      <object >
        <embed id="rtmp-streamer1" src="/static/swfdir/RtmpStreamer.swf" bgcolor="#999999" quality="high"
               width="100%" :style="{height:videohei}"  allowScriptAccess="sameDomain" type="application/x-shockwave-flash"  allowfullscreen="true"></embed>
      </object>
      <div class="bottomve`ido">
        <!--<h3>礼物等其他显示部分（待修改）</h3>-->
      </div>
    </div>

    <!---------main pdf 部分------------->
    <div id="mainpdfcard" class="cardtealivingpdf" :style="{display:mainpdfcarddisplay?'block':'none'}">
      <iframe id="displayPdfIframe" name="displayPdfIframe" class="pdfframe" :src="displayPdfurl"/>
    </div>

    <div  id="maincodecard" class="cardtealivingcdode11"  :style="{display:maincodecarddispaly?'block':'none'}">

      <Form label-position="left">
        <FormItem label="问题描述：" >
          <p style="word-break:break-all;float:left;text-align: left">{{curcode.statement}}</p>
        </FormItem>
        <FormItem label="编程语言：">
          <p style="word-break:break-all;float:left;text-align: left">{{curcode.language}}</p>
        </FormItem>
          <FormItem label="输入答案：">

              <!--输入框的代码高亮-->
              <codemirror
                id="codemirr"
                :value="curcode.example"
                :options="cmOption"
                class="codecode"
                >
              </codemirror>

          </FormItem>
        </Form>

    </div>
    <!--curmulti:{-->
    <!--uniqueId: '',-->
    <!--statement: 'Among the following people, who is the most gay one?',-->
    <!--optionList: ['ADIL', 'XCJ', 'HYX', 'ZHQ ♂ ZSH'],-->
    <!--answer: 'A'-->
    <!--},-->
    <!---------main 选择题 部分 在主界面显示选择题------------->

    <!--zsh-->
     <div id="mainselectcard" class="cardtealivingselect" :style="{display:mainselectcarddisplay?'block':'none'}">
    <!--zsh-->
      <Form>
        <FormItem label="题目">
          <p style="word-break:break-all;float:left;text-align: left">{{curmulti.statement}}</p>
        </FormItem>
        <FormItem v-for="(item, index) in curmulti.optionList"  :key="index"  style=" font-size: 15px">
          <p style="word-break:break-all;float:left;text-align: left">{{String.fromCharCode(65+index)+" : "+item}}</p>
          </FormItem>

        <FormItem>
          <p style="word-break:break-all;float:left;text-align: left">本题目答案：{{curmulti.answer}}</p>
        </FormItem>
      </Form>
    </div>

    <!--=========这是赵汉卿负责的聊天室部分，请勿改动================-->
    <div id="chatingRoom" :style="{top:chatingtop,height:chatinghei}">
      <div class="talk-contents">
        <div class="talk-inner">
          <div class="talk-nav">
            <div class="talk-title">
              <Dropdown @click.native="CHAT.list(userInfo.username, cururl)" trigger="click">
                <a href="javascript:void(0)">
                  聊天对象
                  <Icon type="ios-arrow-down"></Icon>
                </a>
                <DropdownMenu slot="list">
                  <DropdownItem @click.native="CHAT.socket.emit('refresh', {'url':cururl})">刷新</DropdownItem>
                  <DropdownItem v-for="student in CHAT.studentlist" @click.native="talkTo(student)" :key="student.username">{{ student }}</DropdownItem>
                  <DropdownItem divided @click.native="talkTo('all')">all</DropdownItem>
                </DropdownMenu>
              </Dropdown>
              {{ username }}
            </div>
          </div>

          <div class="content" id="content-id">
            <div v-for="(msgObj, index) in CHAT.msgArr" :key="msgObj.msg">
              <div v-if="CHAT.msgArr[index].toUser === username && username !== userInfo.username">
                <div class="talk-space self-talk"
                     v-if="CHAT.msgArr[index].fromUser === userInfo.username">
                  <div class="talk-content">
                    <div class="talk-self-name">{{ msgObj.fromUser }}</div>
                    <div v-if="msgObj.msgType === 'text'" class="talk-word talk-word-self">{{ msgObj.msg }}</div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'audio'">
                      <audio :src="audioUrl(msgObj.msg)" controls></audio>
                    </div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'img'">
                      <img class="talk-image" :src="imageUrl(msgObj.msg)"/>
                    </div>
                    <div v-else></div>
                  </div>
                </div>

                <div class="talk-space user-talk" v-else>
                  <div class="talk-content">
                    <Poptip v-if="msgObj.fromUser !== '[系统]'" trigger="hover" content="content" placement="right-start">
                      <div class="talk-user-name">{{ msgObj.fromUser }}</div>
                      <div class="api" slot="content">
                        <Button type="warning" @click="shutUp(msgObj)">禁言</Button>
                        <Button type="error" @click="blackList(msgObj)">踢出</Button>
                      </div>
                    </Poptip>
                    <div v-else class="talk-user-name">{{ msgObj.fromUser }}</div>

                    <div v-if="msgObj.msgType === 'text'" class="talk-word talk-word-user">{{ msgObj.msg }}</div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'audio'">
                      <audio :src="audioUrl(msgObj.msg)" controls></audio>
                    </div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'img'">
                      <img class="talk-image" :src="imageUrl(msgObj.msg)"/>
                    </div>
                    <div v-else></div>
                  </div>
                </div>
              </div>

              <div v-else-if="CHAT.msgArr[index].toUser === userInfo.username && username !== userInfo.username">
                <div  class="talk-space user-talk">
                  <div class="talk-content">
                    <div v-if="username === 'all'">
                      <Poptip v-if="msgObj.fromUser !== '[系统]'" trigger="hover" content="content" placement="right-start">
                        <div class="talk-user-name">[私信]：{{ msgObj.fromUser }}</div>
                        <div class="api" slot="content">
                          <Button type="warning" @click="shutUp(msgObj)">禁言</Button>
                          <Button type="error" @click="blackList(msgObj)">踢出</Button>
                        </div>
                      </Poptip>
                      <div v-else class="talk-user-name">[私信]：{{ msgObj.fromUser }}</div>
                    </div>
                    <div v-else-if="CHAT.msgArr[index].fromUser === username">
                      <Poptip v-if="msgObj.fromUser !== '[系统]'" trigger="hover" content="content" placement="right-start">
                        <div class="talk-user-name">{{ msgObj.fromUser }}</div>
                        <div class="api" slot="content">
                          <Button type="warning" @click="shutUp(msgObj)">禁言</Button>
                          <Button type="error" @click="blackList(msgObj)">踢出</Button>
                        </div>
                      </Poptip>
                      <div v-else class="talk-user-name">{{ msgObj.fromUser }}</div>
                    </div>
                    <div v-if="msgObj.msgType === 'text'" class="talk-word talk-word-user">{{ msgObj.msg }}</div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'audio'">
                      <audio :src="audioUrl(msgObj.msg)" controls></audio>
                    </div>
                    <div v-else></div>
                    <div v-if="msgObj.msgType === 'img'">
                      <img class="talk-image" :src="imageUrl(msgObj.msg)"/>
                    </div>
                    <div v-else></div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="talker">
            <Input v-if="msgType === 'text'" class="talker-input" v-model="msg" type="textarea" :autosize="true" placeholder="Enter something..." @on-enter="submit"/>
            <div v-else-if="msgType === 'img'">点击发送上传图片</div>
            <button class="talker-send" type="success" @click="submit">发送</button>
            <button class="talker-send" v-on:mousedown="toggleRecorder" v-on:mouseup="submitRecord"><Icon type="ios-mic" size="20"/></button>
            <a href="javascript:;" class=" upf talker-send" @click="chooseImg">图片
              <input type="file" name="fileinput" id="fileinput"/>
            </a>
          </div>
        </div>
      </div>
    </div>
    <!--=========这是赵汉卿负责的聊天室部分，请勿改动================-->

  </div>
</template>

<script>
import axios from 'axios'
import {setSWFIsReady} from '../../static/js/livingrtmp.js'
import {RtmpStreamer} from '../../static/js/livingrtmp.js'
import CHAT from '../client'
import { convertTimeMMSS } from '../utils'
import Recorder from '../recorder'
import PrismEditor from 'vue-prism-editor'
import VueCodemirror from 'codemirror/lib/codemirror'
import 'codemirror/lib/codemirror.css' // css，必要

// language
import 'codemirror/mode/python/python.js'
import 'codemirror/mode/clike/clike.js'

// theme css
import 'codemirror/theme/base16-light.css'
// require active-line.js
import 'codemirror/addon/selection/active-line.js'
// closebrackets
import 'codemirror/addon/edit/closebrackets.js'
// keyMap
import 'codemirror/addon/edit/matchbrackets.js'
import 'codemirror/addon/comment/comment.js'
import 'codemirror/addon/dialog/dialog.js'
import 'codemirror/addon/dialog/dialog.css'
import 'codemirror/addon/search/searchcursor.js'
import 'codemirror/addon/search/search.js'
import 'codemirror/keymap/emacs.js'
import 'codemirror/theme/blackboard.css'
import 'codemirror/mode/javascript/javascript'
import 'codemirror/mode/clike/clike'
import 'codemirror/mode/go/go'
import 'codemirror/mode/htmlmixed/htmlmixed'
import 'codemirror/mode/http/http'
import 'codemirror/mode/php/php'
import 'codemirror/mode/python/python'
import 'codemirror/mode/http/http'
import 'codemirror/mode/sql/sql'
import 'codemirror/mode/vue/vue'
import 'codemirror/mode/xml/xml'

export default{
  name: 'load',
  props: {
    micFailed: { type: Function },
    startRecord: { type: Function },
    stopRecord: { type: Function }
  },
  data () {
    return {
      /**
       * 以下为聊天室使用，请勿改动
       */
      curpage: '1',
      chatingtop: 60 + 'px',
      chatinghei: 710 + 'px',
      msgTypeInfo: '语音',
      socket: null,
      msgType: 'text',
      talkType: 'broadcast',
      msg: '',
      CHAT,
      username: 'all',
      isUploading: false,
      recorder: new Recorder({
        afterStop: () => {
          this.audio = this.recorder.audio
          if (this.stopRecord) {
            this.stopRecord('stop record')
          }
        },
        attempts: this.attempts,
        time: this.time
      }),
      audio: {},
      selected: {},
      shutUpModal: false,
      shutuplist: [],
      /**
       * 以上为聊天室使用，请勿改动
       */

      // something to do with add student
      astu: '',
      // stream stuff
      jinmai: 'ios-mic',
      jinshipin: 'ios-eye',
      isjinmai: false,
      isjinshipin: false,
      videohei: 700 + 'px',
      classmain0: true,
      stream000: '',
      streamer: '',
      streamername: '7181857ac220181030221452650',

      // pdf, multiple and codes
      // pdf parameter
      split_pdf: 0.5,
      modal_pdflist: false,
      // framework to show pdf all
      pdfAll: [{title: '标题', key: 'title'},
        {
          title: '选项',
          key: 'action',
          fixed: 'right',
          width: 180,
          render: (h, params) => {
            return h('div', [
              /*
              h('Button', [
                h('Tooltip', {
                  props: {
                    // confirm: true,
                    content: '点击以添加该PDF至本教室的使用资源中',
                    placement: 'bottom'
                    // type: 'text',
                    // size: 'small'
                  },
                  style: {marginRight: '5px'},
                  on: {
                    click: () => { this.addPdfAll(params.index) }
                  }
                }, '添加')
              ]), */
              h('Button', {
                props: {type: 'text', size: 'small', title: '点击以添加该PDF至本教室的使用资源中'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.addPdfAll(params.index) }
                }
              }, 'Add'),
              h('Button', {
                props: {type: 'text', size: 'small', title: 'test'},
                on: {
                  click: () => { this.delPdfAll(params.index) }
                }
              }, '删除')])
          }
        }],
      pdfThis: [
        {title: '标题', key: 'title'},
        {
          title: '选项',
          key: 'action',
          fixed: 'right',
          width: 120,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.usePdf(params.index) }
                }
              }, '使用'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delPdfClass(params.index) }
                }
              }, '删除')])
          }
        }],
      pdfThisList: [],
      pdfAllList: [],
      // MULTI
      // MULTIPLE CHOICE PARAMETER
      split_multi: 0.5,
      split_multicheck: 0.5,
      modal_viewmulti: false,
      modal_editmulti: false,
      modal_multilist: false,
      // FRAMEWORK TO SHOW MULTI

      curmulti: {
        uniqueId: '',
        statement: '',
        optionList: [],
        answer: ''
      },
      multiAll: [{title: '题目', key: 'statement'},
        {
          title: '选项',
          key: 'action',
          fixed: 'right',
          width: 180,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.addMultiAll(params.index) }
                }
              }, '添加'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.editMultiAll(params.index) }
                }
              }, '编辑'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delMultiAll(params.index) }
                }
              }, '删除')])
          }
        }],
      multiThis: [{title: '题目', key: 'statement'},
        {
          title: '选项',
          key: 'action',
          fixed: 'right',
          width: 180,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.useMulti(params.index) }
                }
              }, '使用'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.viewMulti(params.index) }
                }
              }, '查看'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delMultiClass(params.index) }
                }
              }, '删除')])
          }
        }],
      // MULTI LIST
      multiAllList: [],
      multiThisList: [],
      // MULTI STUDENT ANSWER LIST
      multiAnswer: [{title: 'student', key: 'student'}, {title: 'answer', key: 'answer'}],
      multiAnswerList: [],
      codeAnswer: [{title: 'student', key: 'student'}, {title: 'answer', key: 'answer'}],
      codeAnswerList: [],
      // CODE
      // CODE PARAMETER
      split_code: 0.5,
      modal_codelist: false,
      split_codecheck: 0.5,
      modal_viewcode: false,
      modal_editcode: false,
      // FRAMEWORK TO SHOW CODE LIST
      codeAll: [
        {title: '题目', key: 'statement'},
        {
          title: '选项',
          key: 'action',
          fixed: 'right',
          width: 180,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.addCodeAll(params.index) }
                }
              }, '添加'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.editCodeAll(params.index) }
                }
              }, '编辑'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delCodeAll(params.index) }
                }
              }, '删除')])
          }
        }],
      codeThis: [{title: '题目', key: 'statement'},
        {
          title: '选项',
          key: 'action',
          fixed: 'right',
          width: 180,
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.useCode(params.index) }
                }
              }, '使用'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                style: {marginRight: '5px'},
                on: {
                  click: () => { this.viewCode(params.index) }
                }
              }, '查看'),
              h('Button', {
                props: {type: 'text', size: 'small'},
                on: {
                  click: () => { this.delCodeClass(params.index) }
                }
              }, '删除')])
          }
        }],
      // CODE LIST
      codeAllList: [],
      codeThisList: [],
      curcode: {
        uniqueId: '',
        statement: '',
        language: '',
        example: ''
      },
      // ADD PDF/MULTI/CODE MODALS
      // PDF
      modal_pdf: false,
      // MULTI
      modal_multi: false,
      multi_options: [
        {
          value: '',
          index: 1,
          status: 1
        }
      ], //
      multi_index: 1,
      sub_multi: {
        uniqueId: '',
        statement: '',
        optionList: [],
        answer: '',
        username: ''
      },
      // CODE
      modal_code: false,
      sub_code: {
        uniqueId: '',
        username: '',
        statement: '',
        language: '',
        example: ''
      },
      // CODE EDITOR
      cmOption: {
        //        smartIndent:true,
        //          showCursorWhenSelecting: true,
        autofocus: true,
        //      autoCloseBrackets: true,
        //      tabSize: 4,
        lineNumbers: true,
        //      line: true,
        mode: 'python',
        theme: 'blackboard',  // 选中的theme
        lineWrapping: true
      },
      // ADD STUDENT LIST
      modal_student_xlsx: false,
      // Shihang'S PARAMETER
      displayPdfurl: '',
      littlelivingcarddisplay: false,
      mainselectcarddisplay: false,
      mainpdfcarddisplay: false,
      maincodecarddispaly:false,
      mainlivingcarddisplay: true,

      // COMMON INFO
      userInfo: {
        username: '',
        password: '',
        mobile: '',
        status: '',
        job: ''
      },
      curuser: {
        username: '',
        job: '',
        url: '',
        item: ''
      },
      // STREAM PARAMETERS
      curpdfurl0:'',
      curstream: '',
      vid: '248980',
      cururl: '',
      curvideo: true,
      toopen: true,
      openclose: 'ios-videocam-outline',
      opentext: '开播',

      // SHIHANG'S STUFF
      curstu: 'zsh',
      // SEEM TO BE ABLE TO SHOW STUDENT CODE, SAVE FOR NOW
      curti: [
        {
          title: '4',
          type: 'code',
          ans: '#include<> \n using namespace std; int main(){ int c; cout<<c++<<endl; return 0}',
          standardans: ''
        }
      ],
      studentitems: ['zsh', 'adil', 'zhq', 'hyx', 'xcj'],
      modalStudentList: false
    }
  },
  mounted () {
    /**
     * 以下为聊天室使用，请勿改动
     */
    CHAT.message(this.userInfo.username)
    this.findIfShutUp()
    /**
     * 以上为聊天室使用，请勿改动
     */
  },
  created () {
    this.cururl = this.$route.params.url
    // // console.log(this.cururl)
    this.showUserInfo()
    window['updatepage'] = () => {
      this.updatepage()
    }

    /**
     * 以下为聊天室使用，请勿改动
     */
    this.chatingRoomInit()
    /**
     * 以上为聊天室使用，请勿改动
     */
  },
  computed: {
    isPause () {
      return this.recorder.isPause
    },
    isRecording () {
      return this.recorder.isRecording
    },
    message () {
      return this.uploadStatus === 'success' ? this.successfulUploadMsg : this.failedUploadMsg
    },
    recordedTime () {
      return convertTimeMMSS(this.recorder.duration)
    },
    volume () {
      return parseFloat(this.recorder.volume)
    }
  },
  components: {
    PrismEditor,
    VueCodemirror
  },
  methods: {
    updatepage () {
      // console.log('updatepage')
      this.curpage = document.getElementById('displayPdfIframe').contentWindow.document.getElementById('pageNumber').value
      // console.log(this.curpage)
      let idata = {pdfurl: '', page: ''}
      idata.pdfurl = this.curpdfurl0
      idata.page = this.curpage

      let date = new Date()
      let time = date.getHours() + ':' + date.getMinutes()
      let obj = {
        type: 'page',
        msgType: 'page',
        url: this.cururl,
        time: time,
        msg: idata,
        toUser: 'stu',
        fromUser: this.userInfo.username
      }
      CHAT.submit(obj)
    },
    // ADD METHODS
    // PDF
    addPDF () {
      // send pdf to backend
      let formData = new FormData()
      formData.append('username', this.userInfo['username'])
      formData.append('file', document.querySelector('input[id=pdfinput]').files[0])
      // // console.log(document.querySelector('input[id=pdfinput]').files[0])
      let options = {
        url: '/api/resource/add_pdf',
        data: formData,
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axios(options).then((resp) => {
        if (resp.data.status === 'success') {
          this.$Message.success('PDF uploaded successfully')
        }
      })
    },
    // MULTI
    multi_addChoice () {
      this.multi_index++
      this.multi_options.push({
        value: '',
        index: this.multi_index,
        status: 1
      })
    },
    multi_delChoice (i) {
      this.multi_options[i].status = 0
    },
    create_multi () {
      this.sub_multi.statement = ''
      this.sub_multi.optionList.splice(0, this.sub_multi.optionList.length)
      this.sub_multi.answer = ''
      this.modal_multi = true
    },
    addMulti () {
      // send sub_multi should be set by now
      this.sub_multi.username = this.userInfo.username
      // 将multi_option这个列表改成可发送的数组
      for (let i = 0; i < this.multi_index; i++) {
        if (this.multi_options[i].status === 1) {
          this.sub_multi.optionList.push(this.multi_options[i].value)
        }
      }
      // test
      // // console.log(this.sub_multi.statement)
      // // console.log(this.sub_multi.optionList)
      // post
      axios.post('/api/resource/add_multiple', this.sub_multi).then((resp) => {
        this.$Message.success(resp.data.status)
        // 如果成功
        if (resp.data.status === 'success') {
          // 不用维护选择题列表
          // console.log('Add Multiple Succeeded')
          // 如果失败
        } else {
          this.$Message.error('添加选择题失败')
        }
      })
    },
    // CODE
    create_code () {
      this.sub_code.statement = ''
      this.sub_code.example = ''
      this.sub_code.language = ''
      this.modal_code = true
    },
    addCode () {
      // sub_code should be set by now
      this.sub_code.username = this.userInfo.username
      if (this.cmOption.mode === 'python') {
        this.sub_code.language = 'python'
      } else if (this.cmOption.mode === 'text/x-c++src') {
        this.sub_code.language = 'cpp'
      }
      // test
      // console.log(this.sub_code.username)
      // console.log(this.sub_code.language)
      // console.log(this.sub_code.statement)
      // post
      axios.post('/api/resource/add_code', this.sub_code).then((resp) => {
        this.$Message.success(resp.data.status)
        // 如果成功
        if (resp.data.status === 'success') {
          // 不用维护列表
          // console.log('Add Code Succeeded')
          // 如果失败
        } else {
          this.$Message.error('添加代码题失败')
        }
      })
    },

    // EDIT METHODS

    // LIST METHODS
    // PDF
    // SHOW LIST
    showPdfList () {
      this.modal_pdflist = true
      // get the input
      let pdfListInput = {username: '', url: ''}
      pdfListInput.username = this.userInfo.username
      pdfListInput.url = this.cururl
      // post
      axios.post('/api/resource/getpdfs', pdfListInput).then((resp) => {
        // resp.data 即是那个列表
        this.pdfAllList = resp.data.pdfAllList

         this.pdfThisList = resp.data.pdfThisList
      })
    },
    // ADD PDF TO CLASS
    addPdfAll (index) {
      // iPdf shape as : {title: 'Slide01', url: 'hide/slide01'}
      let iPdf = this.pdfAllList[index]
      let input = {username: '', url: '', pdf: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.pdf = iPdf
      // check if added
      let added = false
      // console.log(iPdf.url)
      for (let i = 0; i < this.pdfThisList.length; i++) {
        // console.log(this.pdfThisList[i].url)
        if (iPdf.url === this.pdfThisList[i].url) {
          // console.log('succeed!')
          added = true
        }
      }
      // post
      if (added) {
        // if it exists in current list
        this.$Message.success('Already Added')
      } else {
        axios.post('/api/resource/pdf_addclass', input).then((resp) => {
          if (resp.data.status === 'success') {
            let pdfInput = {username: '', url: ''}
            pdfInput.username = this.userInfo.username
            pdfInput.url = this.cururl
            axios.post('/api/resource/getpdfs', pdfInput).then((resp) => {
              if (resp.data.pdfAllList !== null) {
                this.pdfAllList = resp.data.pdfAllList
                this.pdfThisList = resp.data.pdfThisList
              } else {
                this.$Message.error('wrong')
              }
            })
          } else {
            this.$Message.error('error in post')
          }
        })
      }
    },
    // DEL PDF FROM TEACHER
    delPdfAll (index) {
      let iPdf = this.pdfAllList[index]
      // input
      let delPdfAllInput = {username: '', url: '', pdf: {}}
      delPdfAllInput.username = this.userInfo.username
      delPdfAllInput.url = this.cururl
      delPdfAllInput.pdf = iPdf
      // post
      axios.post('/api/resource/delete_pdf', delPdfAllInput).then((resp) => {
        if (resp.data.status === 'success') {
          this.$Message.success('deleted from teacher\'s resource')
          let pdfInput = {username: '', url: ''}
          pdfInput.username = this.userInfo.username
          pdfInput.url = this.cururl
          axios.post('/api/resource/getpdfs', pdfInput).then((resp) => {
            if (resp.data.pdfAllList !== null) {
              this.pdfAllList = resp.data.pdfAllList
             this.pdfThisList = resp.data.pdfThisList
            } else {
              this.$Message.error('wrong')
            }
          })
        } else {
          this.$Message.error('error in post')
        }
      })
    },
    // USE IT
    usePdf (index) {
      let ipdf = this.pdfThisList[index]
      // console.log(ipdf)
      this.$Modal.confirm({
        title: '提示',
        content: '是否展示' + ipdf.title,
        onOk: () => {
          // console.log('onOK')
        this.curpdfurl0=ipdf.url
          this.chatingtop = 340 + 'px'
          this.chatinghei = 430 + 'px'
          this.videohei = 250 + 'px'
  this.maincodecarddispaly=false
          this.mainselectcarddisplay = false
          this.mainpdfcarddisplay = true
          this.classmain0 = false
          // console.log(this.classmain0)
          // console.log(document.getElementById('rtmp-streamer1').class)
          // this.liaotianshiheight = 350 + 'px'
          this.displayPdfurl = '/static/pdfjs/web/viewer.html?file=' + ipdf.url
          this.curvideo = false
          this.modal_pdflist = false
          // console.log('1321312')
          let date = new Date()
          let time = date.getHours() + ':' + date.getMinutes()
          let obj = {
            type: 'pdf',
            msgType: 'pdf',
            url: this.cururl,
            time: time,
            msg: ipdf.url,
            toUser: 'stu',
            fromUser: this.userInfo.username
          }
          CHAT.submit(obj)
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    },
    // DEL PDF FROM CLASS
    delPdfClass (index) {
      let iPdf = this.pdfThisList[index]
      // get input
      let input = {username: '', url: '', pdf: {}}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.pdf = iPdf
      // post
      axios.post('/api/resource/pdf_delclass', input).then((resp) => {
        if (resp.data.status === 'success') {
          this.$Message.success('deleted from class resource')
          let pdfInput = {username: '', url: ''}
          pdfInput.username = this.userInfo.username
          pdfInput.url = this.cururl
          axios.post('/api/resource/getpdfs', pdfInput).then((resp) => {
            if (resp.data.status === 'success') {
              this.pdfAllList = resp.data.pdfAllList
              this.pdfThisList = resp.data.pdfThisList
            } else {
              this.$Message.error('wrong')
            }
          })
        } else {
          this.$Message.error('error in post')
        }
      })
    },

    // MULTI
    // SHOW LIST
    showMultiList () {
      this.modal_multilist = true
      // get input
      let input = {username: '', url: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      // post
      axios.post('/api/resource/getmultiples', input).then((resp) => {
        // resp.data 即是那个列表
        this.multiAllList = resp.data.multiAllList
        this.multiThisList = resp.data.multiThisList
        // console.log(this.multiAllList)
        // console.log(this.multiThisList)
      })
    },
    // EDIT MULTI
    editMultiAll (index) {
      const iMulti = this.multiAllList[index]
      // give value here
      this.sub_multi.statement = iMulti.statement
      this.sub_multi.uniqueId = iMulti.uniqueId
      this.sub_multi.answer = iMulti.answer
      // multi options
      this.multi_options = []
      // debug
      // console.log(iMulti)
      // console.log(iMulti.optionList)
      // multi_options: [{value: '',index: 1,status: 1}],
      for (let i = 0; i < iMulti.optionList.length; i++) {
        let k = {value: '', index: i + 1, status: 1}
        k.value = iMulti.optionList[i]
        this.multi_options.push(k)
      }
      // get multi_options
      this.modal_editmulti = true
    },
    // MULTI
    submitMultiChange () {
      // send sub_multi should be set by now
      this.sub_multi.username = this.userInfo.username
      // 将multi_option这个列表改成可发送的数组
      for (let i = 0; i < this.multi_index; i++) {
        if (this.multi_options[i].status === 1) {
          this.sub_multi.optionList.push(this.multi_options[i].value)
        }
      }
      // test
      // // console.log(this.sub_multi.statement)
      // // console.log(this.sub_multi.optionList)
      // post
      axios.post('/api/resource/add_multiple', this.sub_multi).then((resp) => {
        this.$Message.success(resp.data.status)
        // 如果成功
        if (resp.data.status === 'success') {
          // 维护选择题列表
          let input = {username: '', url: ''}
          input.username = this.userInfo.username
          input.url = this.cururl
          // post
          axios.post('/api/resource/getmultiples', input).then((resp) => {
            // resp.data 即是那个列表
            this.multiAllList = resp.data.multiAllList
            this.multiThisList = resp.data.multiThisList
          })
          // 如果失败
        } else {
          this.$Message.error('Edit failed')
        }
      })
    },
    // ADD MULTI TO CLASS
    addMultiAll (index) {
      let iMulti = this.multiAllList[index]
      let input = {username: '', url: '', uniqueId: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.uniqueId = iMulti.uniqueId
      // check if added
      let added = false
      // console.log(iMulti.uniqueId)
      for (let i = 0; i < this.multiThisList.length; i++) {
        // console.log(this.multiThisList[i].uniqueId)
        if (iMulti.uniqueId === this.multiThisList[i].uniqueId) {
          // console.log('succeed!')
          added = true
        }
      }
      // post
      if (added) {
        this.$Message.error('Already Added')
      } else {
        axios.post('/api/resource/multi_addclass', input).then((resp) => {
          if (resp.data.status === 'success') {
            let multiInput = {username: '', url: ''}
            multiInput.username = this.userInfo.username
            multiInput.url = this.cururl
            // console.log('succeeded in post add class')
            // post
            axios.post('/api/resource/getmultiples', multiInput).then((resp) => {
              // resp.data 即是那个列表
              this.multiAllList = resp.data.multiAllList
              this.multiThisList = resp.data.multiThisList
              // console.log('response data get, although do not know what')
            })
          } else {
            this.$Message.error('something wrong')
          }
        })
      }
    },
    // DEL PDF FROM TEACHER
    delMultiAll (index) {
      let iMulti = this.multiAllList[index]
      // input
      let input = {username: '', url: '', uniqueId: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.uniqueId = iMulti.uniqueId
      // post
      axios.post('/api/resource/delete_multiple', input).then((resp) => {
        if (resp.data.status === 'success') {
          let multiInput = {username: '', url: ''}
          multiInput.username = this.userInfo.username
          multiInput.url = this.cururl
          // post
          axios.post('/api/resource/getmultiples', multiInput).then((resp) => {
            // resp.data 即是那个列表
            this.multiAllList = resp.data.multiAllList
            this.multiThisList = resp.data.multiThisList
          })
        } else {
          this.$Message.error('something wrong')
        }
      })
    },
    // USE IT
    useMulti (index) {
      let iselect = this.multiThisList[index]
      // console.log(iselect)
      this.$Modal.confirm({
        title: '提示',
        content: '是否展示: \n ' + iselect.statement,
        onOk: () => {
          // console.log("sdasd")
          this.chatingtop = 340 + 'px'
          this.chatinghei = 430 + 'px'
          this.chatingtop = 340 + 'px'
          this.chatinghei = 430 + 'px'
          this.mainselectcarddisplay = true
          this.mainpdfcarddisplay = false
          this.classmain0 = false
  this.maincodecarddispaly=false
          this.curvideo = false
          this.curmulti=iselect
          this.curmulti = iselect
          this.curtitle = iselect.statement
          this.curanswer = iselect.answer
          this.modal_multilist = false
          let date = new Date()
          let time = date.getHours() + ':' + date.getMinutes()
          let obj = {
            type: 'select',
            msgType: 'select',
            url: this.cururl,
            time: time,
            msg: iselect,
            toUser: 'stu',
            fromUser: this.userInfo.username
          }
          CHAT.submit(obj)
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    },
    // VIEW
    viewMulti (index) {
      let iMulti = this.multiThisList[index]
      // input
      let input = {username: '', url: '', uniqueId: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.uniqueId = iMulti.uniqueId
      // post
      axios.post('/api/resource/multi_viewclass', input).then((resp) => {
        this.multiAnswerList = resp.data.multiAnswerList
      })
      this.sub_multi.optionList = iMulti.optionList
      this.sub_multi.statement = iMulti.statement
      this.sub_multi.answer = iMulti.answer
      this.sub_multi.uniqueId = iMulti.uniqueId
      // console.log(this.sub_multi.optionList)
      this.modal_viewmulti = true
    },
    // DEL MULTI FROM CLASS
    delMultiClass (index) {
      let iMulti = this.multiThisList[index]
      // input
      let input = {username: '', url: '', uniqueId: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.uniqueId = iMulti.uniqueId
      // post
      axios.post('/api/resource/multi_delclass', input).then((resp) => {
        if (resp.data.status === 'success') {
          let multiInput = {username: '', url: ''}
          multiInput.username = this.userInfo.username
          multiInput.url = this.cururl
          // post
          axios.post('/api/resource/getmultiples', multiInput).then((resp) => {
            // resp.data 即是那个列表
            this.multiAllList = resp.data.multiAllList
            this.multiThisList = resp.data.multiThisList
          })
        } else {
          this.$Message.error('something wrong')
        }
      })
    },

    // CODE
    // SHOW LIST
    showCodeList () {
      this.modal_codelist = true
      // get input
      let input = {username: '', url: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      // post
      axios.post('/api/resource/getcodes', input).then((resp) => {
        // resp.data 即是那个列表
        this.codeAllList = resp.data.codeAllList
        this.codeThisList = resp.data.codeThisList
      })
    },
    // EDIT CODE ASSIGNMENT
    editCodeAll (index) {
      let iCode = this.codeAllList[index]
      this.sub_code.language = iCode.language
      this.sub_code.example = iCode.example
      this.sub_code.statement = iCode.statement
      this.sub_code.uniqueId = iCode.uniqueId
      this.sub_code.username = this.userInfo.username
      this.modal_editcode = true
    },
    // CODE
    submitCodeChange () {
      // sub_code should be set by now
      this.sub_code.username = this.userInfo.username
      if (this.cmOption.mode === 'python') {
        this.sub_code.language = 'python'
      } else if (this.cmOption.mode === 'text/x-c++src') {
        this.sub_code.language = 'cpp'
      }
      // test
      // console.log(this.sub_code.username)
      // console.log(this.sub_code.language)
      // console.log(this.sub_code.statement)
      // post
      axios.post('/api/resource/update_code', this.sub_code).then((resp) => {
        this.$Message.success(resp.data.status)
        // 如果成功
        if (resp.data.status === 'success') {
          // console.log('Edit Code Succeeded')
          // 如果失败
        } else {
          this.$Message.error('添加代码题失败')
        }
      })
    },
    // ADD CODE TO CLASS
    addCodeAll (index) {
      let iCode = this.codeAllList[index]
      let input = {username: '', url: '', uniqueId: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.uniqueId = iCode.uniqueId
      // check if added
      let added = false
      // console.log(iCode.uniqueId)
      for (let i = 0; i < this.codeThisList.length; i++) {
        // console.log(this.codeThisList[i].uniqueId)
        if (iCode.uniqueId === this.codeThisList[i].uniqueId) {
          // console.log('succeed!')
          added = true
        }
      }
      // post
      if (added) {
        this.$Message.error('Already Added')
      } else {
        axios.post('/api/resource/code_addclass', input).then((resp) => {
          if (resp.data.status === 'success') {
            let codeInput = {username: '', url: ''}
            codeInput.username = this.userInfo.username
            codeInput.url = this.cururl
            // post
            axios.post('/api/resource/getcodes', codeInput).then((resp) => {
              // resp.data 即是那个列表
              this.codeAllList = resp.data.codeAllList
              this.codeThisList = resp.data.codeThisList
            })
          } else {
            this.$Message.error('something wrong')
          }
        })
      }
    },
    // DEL CODE FROM TEACHER
    delCodeAll (index) {
      let iCode = this.codeAllList[index]
      // input
      let input = {username: '', url: '', uniqueId: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.uniqueId = iCode.uniqueId
      // post
      axios.post('/api/resource/delete_code', input).then((resp) => {
        if (resp.data.status === 'success') {
          let codeInput = {username: '', url: ''}
          codeInput.username = this.userInfo.username
          codeInput.url = this.cururl
          // post
          axios.post('/api/resource/getcodes', codeInput).then((resp) => {
            // resp.data 即是那个列表
            this.codeAllList = resp.data.codeAllList
            this.codeThisList = resp.data.codeThisList
          })
        } else {
          this.$Message.error('something wrong')
        }
      })
    },
    // USE IT
    useCode (index) {
      let iCode = this.codeThisList[index]
      //  {
      //    uniqueId: '',
      //      statement: 'B-Tree',
      //    language: 'cpp',
      //    example: 'cout << "hello world" << endl;'
      //  }
      // console.log(iCode)
      this.$Modal.confirm({
        title: '提示',
        content: '是否展示' + iCode.statement,
        onOk: () => {
          // console.log('onOK')
        this.curcode=iCode


  document.getElementById("codemirr").focus();

          this.modal_codelist = false
          this.chatingtop = 340 + 'px'
          this.chatinghei = 430 + 'px'
          this.videohei = 250 + 'px'
          this.mainselectcarddisplay = false
          this.mainpdfcarddisplay = false
          this.classmain0 = false
          this.maincodecarddispaly=true
          // console.log(this.classmain0)
          // console.log(document.getElementById('rtmp-streamer1').class)
          this.modal_pdflist = false
          // console.log('1321312')
          let date = new Date()
          let time = date.getHours() + ':' + date.getMinutes()
          let obj = {
            type: 'code',
            msgType: 'code',
            url: this.cururl,
            time: time,
            msg: iCode,
            toUser: 'stu',
            fromUser: this.userInfo.username
          }
          CHAT.submit(obj)
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    // to be implemented
    },

    // VIEW
    viewCode (index) {
      let iCode = this.codeThisList[index]
      // input
      let input = {username: '', url: '', uniqueId: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.uniqueId = iCode.uniqueId
      this.sub_code.statement = iCode.statement
      this.sub_code.language = iCode.language
      this.sub_code.example = iCode.example
      // debug
      // console.log(input)
      this.sub_code.statement = iCode.statement
      this.sub_code.language = iCode.language
      this.sub_code.example = iCode.example
      // post
      axios.post('/api/resource/code_viewclass', input).then((resp) => {
        this.codeAnswerList = resp.data.codeAnswerList
      })
      this.modal_viewcode = true
    },
    // DEL CODE FROM CLASS
    delCodeClass (index) {
      let iCode = this.codeThisList[index]
      // input
      let input = {username: '', url: '', uniqueId: ''}
      input.username = this.userInfo.username
      input.url = this.cururl
      input.uniqueId = iCode.uniqueId
      // post
      axios.post('/api/resource/code_delclass', input).then((resp) => {
        if (resp.data.status === 'success') {
          let codeInput = {username: '', url: ''}
          codeInput.username = this.userInfo.username
          codeInput.url = this.cururl
          // post
          axios.post('/api/resource/getcodes', codeInput).then((resp) => {
            // resp.data 即是那个列表
            this.codeAllList = resp.data.codeAllList
            this.codeThisList = resp.data.codeThisList
          })
        } else {
          this.$Message.error('something wrong')
        }
      })
    },

    // Yuxuan's Methods Stops Here

    /**
     * 以下为聊天室使用，请勿改动
     */
    chatingRoomInit () {
      this.socket = CHAT.init(this.userInfo.username, this.cururl)
      document.getElementById('fileinput').addEventListener('change', this.chooseImg(), false);
    },
    submit () {
      var date = new Date()
      var time = date.getHours() + ':' + date.getMinutes()
      var obj = {}
      if (this.msgType === 'text') {
        if (this.msg === '') return
        obj = {
          type: this.talkType,
          msgType: 'text',
          url: this.cururl,
          time: time,
          msg: this.msg,
          toUser: this.username,
          fromUser: this.userInfo.username
        }
        this.msg = ''
        CHAT.submit(obj)
      } else if (this.msgType === 'audio') {
        obj = {
          type: this.talkType,
          msgType: 'audio',
          url: this.cururl,
          time: time,
          msg: this.audio,
          toUser: this.username,
          fromUser: this.userInfo.username
        }
        // console.log(obj)
        CHAT.submit(obj)
      } else if (this.msgType === 'img') {
        var blob = new Blob([document.querySelector('input[type=file]').files[0]], { type: 'image/png' })
        obj = {
          type: this.talkType,
          msgType: 'img',
          url: this.cururl,
          time: time,
          msg: blob,
          toUser: this.username,
          fromUser: this.userInfo.username
        }
        // console.log(obj)
        CHAT.submit(obj)
        this.msgType = 'text'
      }
    },
    submitRecord () {
      // console.log('mouse up')
      this.stopRecorder()
      var date = new Date()
      var time = date.getHours() + ':' + date.getMinutes()
      var obj = {
        type: this.talkType,
        msgType: 'audio',
        url: this.cururl,
        time: time,
        msg: this.audio,
        toUser: this.username,
        fromUser: this.userInfo.username
      }
      // console.log(obj)
      CHAT.submit(obj)
    },
    chooseImg () {
      this.msgType = 'img'
    },
    changeMsgType () {
      if (this.msgType === 'text') {
        this.msgTypeInfo = '语音'
        this.msgType = 'audio'
      } else if (this.msgType === 'audio') {
        this.msgTypeInfo = '文字'
        this.msgType = 'text'
      }
    },
    toggleRecorder () {
      // console.log('mouse down')
      if (!this.isRecording || (this.isRecording && this.isPause)) {
        this.recorder.start()
        if (this.startRecord) {
          this.startRecord('start record')
        }
      } else {
        this.recorder.pause()
        if (this.startRecord) {
          this.startRecord('pause record')
        }
      }
    },
    stopRecorder () {
      if (!this.isRecording) {
        return
      }
      this.recorder.stop()
    },
    audioUrl (obj) {
      var url = window.URL.createObjectURL(new Blob([obj.blob], { type: 'audio/wav' }))
      return url
    },
    imageUrl (obj) {
      var url = window.URL.createObjectURL(new Blob([obj], { type: 'image/png' }))
      return url
    },
    talkTo (p) {
      if (p === this.userInfo.username) return
      this.username = p
      if (p !== 'all') {
        this.msg = ''
        this.talkType = 'whisper'
      } else {
        this.msg = ''
        this.talkType = 'broadcast'
      }
    },
    shutUp (m) {
      var obj = {
        url: this.cururl,
        toUser: m.fromUser,
        fromUser: this.userInfo.username
      }
      // console.log(m)
      CHAT.shutUp(obj)
    },
    blackList (m) {
      var obj = {
        url: this.cururl,
        toUser: m.fromUser,
        fromUser: this.userInfo.username
      }
      // console.log(m)
      CHAT.blackList(obj)
    },
    findIfShutUp () {
      axios.post('/api/classroom/shutuplist', {'url': this.cururl}).then((resp) => {
        // console.log(resp.data)
        this.shutuplist = resp.data
      })
    },
    getShutUpList () {
      this.shutUpModal = true
      this.findIfShutUp()
    },
    noShutUp (student) {
      CHAT.youCanTalk(student, this.cururl)
      var index = this.shutuplist.indexOf(student)
      this.shutuplist.splice(index, 1)
    },
    /**
     * 以上为聊天室使用，请勿改动
     */
    subxlsx () {
      // console.log('upload xlsx')
      this.getstudents()
      /* const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      data['item'] = document.querySelector('input[type=file]').files[0]
      // console.log(data['item']) */
      let formData = new FormData()
      formData.append('url', this.cururl)
      formData.append('item', document.querySelector('input[id="xlsxinput"]').files[0])
      let options = {
        url: '/api/classroom/xlsxaddstudents',
        data: formData,
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      // console.log(formData.url)
      axios(options).then((resp) => {
        if (resp.data !== undefined) {
          this.$Message.success('added succeeded')
          this.getstudents()
        }
      })
    },
    addStudentByExcel () {
      this.modal_student_xlsx = true
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      axios.post('/api/classroom/getstudents', data).then((resp) => {
        this.studentitems = resp.data
      })
    },
    addStudent () {
      // console.log('add student via username')
      this.$Modal.confirm({
        render: (h) => {
          return h('Input', {
            props: {
              id: 'passinput',
              autofocus: true,
              placeholder: 'Please enter the username of this student'
            },
            on: {
              input: (val) => {
                this.astu = val
              }
            }
          })
        },
        onOk: () => {
          const data = this.curuser
          data['username'] = this.userInfo['username']
          data['job'] = this.userInfo['job']
          data['url'] = this.cururl
          data['item'] = this.astu
          axios.post('/api/classroom/aaddstudents', data).then((resp) => {
            if (resp.data.status === 'success') {
              this.$Message.success('成功添加学生')
            }
          })
        }
      })
    },
    exportData (type) {
      if (type === 1) {
        this.$refs.table.exportCsv({
          filename: this.curstu + '数据统计'
        })
      }
    },
    getstudents () {
      this.modalStudentList = true
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      axios.post('/api/classroom/getstudents', data).then((resp) => {
        this.studentitems = resp.data
      })
    },
    // 用于显示学生的代码
    showstudentti (item) {
      this.curstu = item
      const data = this.curuser
      data['username'] = this.userInfo['username']
      data['job'] = this.userInfo['job']
      data['url'] = this.cururl
      data['item'] = this.curstu
      axios.post('/api/classroom/getstudentsti', data).then((resp) => {
        this.curti = resp.data
      })
    },
    closetext () {
      this.$Modal.confirm({
        title: '提示',
        content: '确认退出教学资源',
        onOk: () => {
        // console.log("close")
          this.maincodecarddispaly=false
          this.mainselectcarddisplay = false
          this.mainpdfcarddisplay = false
          this.classmain0 = true
          this.videohei = 700 + 'px'
          this.chatingtop = 60 + 'px'
          this.chatinghei = 710 + 'px'
          this.curvideo = true
          const data = this.curuser
          data['username'] = this.userInfo['username']
          data['job'] = this.userInfo['job']
          data['url'] = this.cururl
          axios.post('/api/classroom/closepdfsec', data).then((resp) => {

          })

          var date = new Date()
          var time = date.getHours() + ':' + date.getMinutes()
          var obj = {
            type: 'close',
            msgType: 'close',
            url: this.cururl,
            time: time,
            msg: 'close',
            toUser: 'stu',
            fromUser: this.userInfo.username
          }
          CHAT.submit(obj)
        },
        onCancel: () => {
          this.$Message.info('Clicked cancel')
        }
      })
    },
    showUserInfo () {
      this.userInfo['username'] = this.$cookies.get('user').username
      this.userInfo['status'] = this.$cookies.get('user').status
      this.userInfo['password'] = this.$cookies.get('user').password
      this.userInfo['mobile'] = this.$cookies.get('user').mobile
      this.userInfo['job'] = this.$cookies.get('user').job
    },
    teaopenclose () {
      if (this.toopen) {
        this.$Modal.confirm({
          title: '提示',
          content: '是否确认开播',
          onOk: () => {
            this.toopen = false
            this.opentext = '关播'
            this.openclose = 'ios-power'
            this.getstudents()
            const data = this.curuser
            data['username'] = this.userInfo['username']
            data['job'] = this.userInfo['job']
            data['url'] = this.cururl
            axios.post('/api/classroom/openliving', data).then((resp) => {
              this.streamername = resp.data.streamername
              // console.log(resp.data.streamername)
              // console.log(this.streamername)
              // console.log(this.streamername)
              setSWFIsReady()
              this.streamer000 = document.getElementById('rtmp-streamer1')
              this.streamer000.setScreenPosition(-100, 0)
              this.streamer000.setScreenSize(700, 380)
              this.streamer000.publish('rtmp://push2.videocc.net/recordfe', this.streamername)
            })
          },
          onCancel: () => {
          }
        })
      } else {
        this.$Modal.confirm({
          title: '提示',
          content: '是否确认关播',
          onOk: () => {
            this.toopen = true
            this.opentext = '开播'
            this.openclose = 'ios-videocam-outline'
            window.location.reload()
            const data = this.curuser
            data['username'] = this.userInfo['username']
            data['job'] = this.userInfo['job']
            data['url'] = this.cururl
            axios.post('/api/classroom/closeliving', data).then((resp) => {
            })
          },
          onCancel: () => {

          }
        })
      }
    },
    tojinmai () {
      if (this.isjinmai) {
        this.jinmai = 'ios-mic'
        this.isjinmai = false
        this.streamer000.disconnect()
        this.streamer000.setScreenPosition(-1000, 0)
        this.streamer000.setScreenSize(700, 380)
        this.streamer000.setMicRate(10000000000)
        this.streamer000.publish('rtmp://push2.videocc.net/recordfe', this.streamername)
      } else {
        this.jinmai = 'ios-mic-off'
        this.isjinmai = true
        this.streamer000.disconnect()
        this.streamer000.setScreenPosition(-1000, 0)
        this.streamer000.setScreenSize(700, 380)
        this.streamer000.setMicRate(0)
        this.streamer000.publish('rtmp://push2.videocc.net/recordfe', this.streamername)
      }
    },
    tojinshipin () {
      if (this.isjinshipin) {
        this.jinshipin = 'ios-eye'
        this.isjinshipin = false
        this.streamer000.disconnect()
        this.streamer000.setScreenPosition(-1000, 0)
        this.streamer000.setScreenSize(700, 380)
        this.streamer000.setCamFrameInterval(15)
        this.streamer000.publish('rtmp://push2.videocc.net/recordfe', this.streamername)
      } else {
        this.jinshipin = 'ios-eye-off'
        this.isjinshipin = true
        this.streamer000.disconnect()
        this.streamer000.setScreenPosition(-1000, 0)
        this.streamer000.setScreenSize(700, 380)
        this.streamer000.setCamFrameInterval(1000000000)
        this.streamer000.publish('rtmp://push2.videocc.net/recordfe', this.streamername)
      }
    }

  }
}

</script>
<style>
  #teacherLiving {
    padding: 0 5%;
  }
  /* 赵汉卿负责的聊天室部分，请勿修改 */
  #chatingRoom {
    position:absolute;
    left: 79%;
    width: 21%;

  }
  .talk-contents {
    height: 100%;
    margin-left: 10px;
  }
  .talk-nav {
    background-color: #eee;
    margin-left: 10px;
    text-align: center;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    line-height: 30px;
  }
  .talk-title {
    position: relative;
    padding: 10px 0;
    margin: 0 19px;
    border-bottom: 1px solid #d6d6d6;
    background-color: #eee;
  }
  .content {
    background-color: #eee;
    position: absolute;
    bottom: 50px;
    padding: 0 19px;
    margin-left: 10px;
    top: 51px;
    right: 0;
    left: 0;
    overflow: scroll;
  }
  .talker {
    margin-left: 10px;
    padding-right: 19px;
    border-top: 1px solid #d6d6d6;
    position: absolute;
    right: 0;
    bottom: 0;
    left: 0;
  }

  .talk-space {
    width: 100%;
    margin-bottom: 16px;
  }
  .talk-word {
    display: inline-block;
    position: relative;
    background: -webkit-linear-gradient(left top, rgba(246, 94, 84, 1), rgba(218, 43, 101, 1)); /* Safari 5.1 - 6.0 */
    color: #fff;
    max-width: 60%;
    min-height: 25px;
    line-height: 25px;
    margin: 0 1%;
    padding: 4px 12px 2px 11px;
    border-radius: 5px;
    font-size: 12px;
    word-break: break-all;
  }
  .talk-word-user {
    border-bottom-right-radius: 0;
    margin-right: 10px;
    text-align: left;
  }
  .talk-word-self {
    background: rgba(243, 243, 243, 1) none;
    color: rgba(0, 0, 0, 1);
    border-bottom-left-radius: 0;
    margin-left: 10px;
    text-align: right;
  }
  .self-talk {
    margin-top: 10px;
  }
  .talk-content {
    text-align: right;
    position: relative;
  }
  .user-talk {
    margin-top: 10px;
  }
  .talk-content {
    text-align: left;
    position: relative;
    margin-left: 0px;
  }
  .talk-image {
    width: 100px;
  }
  .talker-send {
    display: inline-block;
    margin-bottom: 0;
    font-weight: 400;
    text-align: center;
    touch-action: manipulation;
    cursor: pointer;
    background-image: none;
    border: 1px solid transparent;
    white-space: nowrap;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    padding: 5px 15px 6px;
    font-size: 12px;
    border-radius: 4px;
    transition: color .2s linear,background-color .2s linear,border .2s linear,box-shadow .2s linear;
    vertical-align: middle;
    line-height: 1.5;
    outline: 0;
    color: #fff;
    background-color: #19be6b;
    border-color: #19be6b;
    -webkit-appearance: button;
  }
  /* 赵汉卿负责的聊天室部分，请勿修改 */
  .tealivingmain{
    width: 100%;
  }
  .cardtea{
    position:absolute;
    left: 0;
    top:60px;
    width: 18%;
  }
  .cardtealiving00{
    position:absolute;
    left: 19%;
    width: 59%;
    top:60px;
  }
  .cardtealittleliving00{
    position:absolute;
    left: 79%;
    width: 21%;
    top:60px;
  }

  .menuitentea{
    font-size: 18px;
  }
  .btnopen{
    padding-:5%;
    margin:5%;
  }

  .cardtealivingpdf{
    position:absolute;
    left: 19%;
    width: 59%;
    top:60px;
    display: none;
  }
  .pdfframe{
    width:100% ;
    height:600px;
  }
  .topveido{
    height: auto;
    float: left;
  }
  .bottomveido{
    height: auto;
    text-align: center;
  }
  .cardtealivingselect{
    position:absolute;
    left: 19%;
    width: 59%;
    height: 800px;
    top:60px;
    display: none;
  }

  .selecttitle00{
    padding-top: 3%;
    position:relative;
    left:40px;
    float:left;
    font-size: 15px;
  }
  .radiotea{
    float:left;
    position:relative;
    top:300px;

  }
  .anstea00{
    float:left;
    position:relative;
    top:500px;
    left:-50px;
    font-size: 15px;
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
  .teacher-live-split{
    height: 430px;
    border: 1px solid #dcdee2;
  }
  .teacher-live-split-pane{
    padding: 10px;
  }
  .cardtealivingcdode11{
    position:absolute;
    left: 19%;
    width: 59%;
    top:60px;
    display: none;
  }
  p{
    word-wrap: break-word;
    word-break: break-all;
    overflow: hidden;
  }
  .codecode{
    text-align: left;

  }
</style>
