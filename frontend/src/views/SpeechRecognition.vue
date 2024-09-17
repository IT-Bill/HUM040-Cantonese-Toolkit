<template>
  <div>
    <p>
      可上传一段长度60s以内，大小3M以内的粤语音频文件。示例文件在voice_example文件夹。
      <br>Upload an audio file that is less than 60 seconds in length and under 3MB in size.
    </p>
    <p>
      示例文件在voice_example文件夹。
      <br>Examples are in voice_example folder.
    </p>


    <input type="file" @change="handleFileUpload" accept="audio/*">
    <button @click="submitAudio" :disabled="!selectedFile">Upload Audio</button>

    <!-- 展示语音识别结果 -->
    <div v-if="recognitionResult">
      <h3>音频长度 Audio Duration: </h3>
      <p>{{ recognitionResult.AudioDuration / 1000 }} s</p>
      <h3>识别结果 Recognition Result:</h3>
      <p>{{ recognitionResult.Result }}</p>
    </div>

  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  name: 'SpeechRecognition',
  data() {
    return {
      selectedFile: null,
      recognitionResult: null,  // 用于存储识别结果的数据属性
    };
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
    },
    submitAudio() {
      const formData = new FormData();
      formData.append('file', this.selectedFile);

      axios.post('http://localhost:8090/asr', formData)
        .then(response => {
          // 存储响应数据到 recognitionResult
          this.recognitionResult = response.data;
        })
        .catch(error => {
          console.error('Upload error:', error);
        });
    }
  }
}
</script>

<style scoped>
/* 添加您需要的任何样式 */
</style>
