<template>
  <div id="audioTest">
    <br/>
    <br/>


      <div class="ar-content" :class="{'ar__blur': isUploading}">
        <div class="ar-recorder">
          <button @click="toggleRecorder()">录音</button>
          <button @click="stopRecorder">停止</button>
        </div>

        <div class="ar-recorder__duration">{{recordedTime}}</div>

        <div class="ar-records">
          <div
            class="ar-records__record"
            :class="{'ar-records__record--selected': record.id === selected.id}"
            :key="record.id"
            v-for="(record, idx) in recordList"
            @click="selected = record">
            <div
              class="ar__rm"
              v-if="record.id === selected.id"
              @click="removeRecord(idx)">&times;</div>
            <div class="ar__text">Record {{idx + 1}}</div>
            <div class="ar__text">{{record.duration}}</div>
          </div>
        </div>
      </div>

  </div>
</template>
<script>
import { convertTimeMMSS } from '../utils'
import Recorder from '../recorder'

export default{
  props: {
    micFailed: { type: Function },
    startRecord: { type: Function },
    stopRecord: { type: Function },

    failedUpload: { type: Function },
    headers: { type: Object },
    startUpload: { type: Function },
    successfulUpload: { type: Function },
    uploadUrl: { type: String },

    successfulUploadMsg: { type: String, default: 'Upload successful' },
    failedUploadMsg: { type: String, default: 'Upload fail' }
  },
  data () {
    return {
      isUploading: false,
      recorder: new Recorder({
        afterStop: () => {
          this.recordList = this.recorder.recordList()
          if (this.stopRecord) {
            this.stopRecord('stop record')
          }
        },
        attempts: this.attempts,
        time: this.time
      }),
      recordList: [],
      selected: {},
      uploadStatus: null,
      uploaderOptions: {}
    }
  },
  methods: {
    toggleRecorder () {
      if (!this.isRecording || (this.isRecording && this.isPause)) {
        console.log(this.recorder)
        console.log(1)
        this.recorder.start()
        if (this.startRecord) {
          this.startRecord('start record')
        }
      } else {
        console.log(this.recorder)
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
    removeRecord (idx) {
      this.recordList.splice(idx, 1)
      this.$set(this.selected, 'url', null)
      this.$eventBus.$emit('remove-record')
    }
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
  }
}
</script>
<style>

</style>
