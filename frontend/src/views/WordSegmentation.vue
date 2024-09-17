<template>
  <div class="flex-col">
    <div>
      <p>
        按照惯例，粤语书写不使用词界限符（如英文中的空格）。然而，在许多自然语言处理任务中，常常需要处理已分词的粤语数据。
        <br />By convention, Cantonese is not written with word boundaries (like spaces in English). However, in many
        natural
        language processing tasks, it is often necessary to work with a segmented form of Cantonese data.
      </p>
      <p>
        目前，底层的词语分割模型是一个简单的最长字符串匹配算法。
        <br />Currently, the underlying word segmentation model is a simple longest string matching algorithm.
      </p>
    </div>

    <textarea v-model="inputText" placeholder="Enter text for segmentation..."></textarea>
    <button @click="segmentText">Segment Text</button>
    <div v-if="segmentedWords.length > 0">
      <h2>Segmented Words:</h2>
      <text v-for="word in segmentedWords" :key="word">
        \{{ word }}&nbsp;
      </text>
    </div>
  </div>
</template>
    
<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: 'WordSegmentation',

  setup() {
    const inputText = ref('');
    const segmentedWords = ref([]);

    const segmentText = () => {
      if (inputText.value.trim() === '') {
        alert('Please enter some text to segment.');
        return;
      }

      axios.post('http://localhost:8090/segment', { text: inputText.value })
        .then(response => {
          segmentedWords.value = response.data;
        })
        .catch(error => {
          console.error('Error in WordSegmentation.vue:', error);
        });
    };

    return {
      inputText,
      segmentedWords,
      segmentText
    };
  }
}
</script>

<style scoped>
textarea {
  width: 80%;
  min-height: 150px;
  margin-bottom: 1em;
  padding: 0.5em;
}

button {
  padding: 0.5em 1em;
  width: 200px;
  cursor: pointer;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin: 0.5em 0;
}
</style>