<template>
  <div>
    <p>
      停用词是在自然语言处理中经常需要过滤掉的常见词汇，它们通常包括代词、冠词等功能性词汇。<br/>
      Stop words are common words that are often filtered out in natural language processing tasks, typically including
      function words such as pronouns and articles.
    </p>
    <table>
      <tr v-for="row in rows" :key="row[0]">
        <td v-for="word in row" :key="word">{{ word }}</td>
      </tr>
    </table>
  </div>
</template>
  
<script>
import axios from 'axios';
import { ref, computed } from 'vue';

export default {
  name: 'StopWords',

  setup() {
    const stopWords = ref([]);

    axios.get("http://localhost:8090/stop-words")
      .then(response => {
        stopWords.value = response.data;
      })
      .catch(error => {
        console.error('Error in StopWords.vue:', error);
      });

    const rows = computed(() => {
      const rows = [];
      let currentRow = [];
      stopWords.value.forEach((word, index) => {
        currentRow.push(word);
        if ((index + 1) % 10 === 0) {
          rows.push(currentRow);
          currentRow = [];
        }
      });
      if (currentRow.length > 0) {
        // 如果剩余的单词不足10个，仍然需要添加它们作为最后一行
        rows.push(currentRow);
      }
      return rows;
    });

    return {
      stopWords,
      rows
    };
  }
}
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}
</style>
