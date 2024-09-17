<template>
  <div class="flex-col">
    <div>
      <p>
        处理粤语语料库数据中最常见的任务之一涉及到粤拼罗马化的处理。
        <br>One of the most common tasks in handling Cantonese corpus data involves the processing
        of Jyutping romanization.
      </p>
      <p>
        常见的需求包括将粤语字符转换为粤拼罗马化。
        <br>A common need is to convert Cantonese characters to Jyutping romanization.
      </p>
    </div>

    <textarea v-model="inputText" placeholder="Enter text for romanization..."></textarea>
    <button @click="romanizeText">Romanize Text</button>
    <div v-if="romanizedWords.length > 0">
      <h2>Romanized Words:</h2>
      <div v-for="word in romanizedWords" :key="word">
        {{ word }}&nbsp;
      </div>
    </div>
  </div>
</template>
    
<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: 'JyutpingRomanization',

  setup() {
    const inputText = ref('');
    const romanizedWords = ref([]);

    const romanizeText = () => {
      if (inputText.value.trim() === '') {
        alert('Please enter some text to romanize.');
        return;
      }

      axios.post('http://localhost:8090/jyutping', { text: inputText.value })
        .then(response => {
          romanizedWords.value = response.data;
        })
        .catch(error => {
          console.error('Error in JyutpingRomanization.vue:', error);
        });
    };

    return {
      inputText,
      romanizedWords,
      romanizeText
    };
  }
}
</script>

<style scoped>
/* 你可以保持样式不变，或根据需要进行调整 */
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

</style>
