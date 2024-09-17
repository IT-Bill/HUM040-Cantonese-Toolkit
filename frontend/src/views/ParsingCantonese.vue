<template>
  <div class="flex-col">
    <div>
      <p>
        处理原始粤语文本，将其转换为适合语言学分析的结构化格式。
        <br>It is designed to process raw Cantonese text, converting it into a structured format suitable for linguistic
        analysis.
      </p>
    </div>

    <textarea v-model="inputText" placeholder="Enter Cantonese text for parsing..."></textarea>
    <button @click="parseText">Parse Text</button>

    <!-- 展示解析结果的表格 -->
    <div>
      <table>
        <thead>
          <tr>
            <th>词 Word</th>
            <th>拼音 Jyutping</th>
            <th>词性 POS</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in paginatedData" :key="i">
            <td>{{ item.word }}</td>
            <td>{{ item.jyutping }}</td>
            <td>{{ item.pos }}</td>
          </tr>
        </tbody>
      </table>

      <!-- 翻页控制 -->
      <button @click="previousPage" :disabled="currentPage <= 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage >= totalPages">Next</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, computed } from 'vue';

export default {
  name: 'ParsingCantonese',
  setup() {
    const inputText = ref('');
    const parsedData = ref([]);
    const currentPage = ref(1);
    const pageSize = 10;

    const parseText = () => {
      if (inputText.value.trim() === '') {
        alert('Please enter some Cantonese text to parse.');
        return;
      }

      axios.post('http://localhost:8090/parse', { text: inputText.value })
        .then(response => {
          parsedData.value = response.data;
          currentPage.value = 1; // 每次解析后重置为第一页
        })
        .catch(error => {
          console.error('Error in ParsingCantonese.vue:', error);
        });
    };

    const totalPages = computed(() => Math.ceil(parsedData.value.length / pageSize));
    const paginatedData = computed(() => {
      const start = (currentPage.value - 1) * pageSize;
      const end = start + pageSize;
      return parsedData.value.slice(start, end);
    });

    const previousPage = () => {
      if (currentPage.value > 1) currentPage.value -= 1;
    };

    const nextPage = () => {
      if (currentPage.value < totalPages.value) currentPage.value += 1;
    };

    return {
      inputText,
      parsedData,
      currentPage,
      totalPages,
      paginatedData,
      parseText,
      previousPage,
      nextPage
    };
  }
}
</script>

<style scoped>
/* 相同的样式可以从 JyutpingRomanization.vue 和 SearchCorpus.vue 继承 */
.flex-col {
  display: flex;
  flex-direction: column;
}

textarea {
  width: 80%;
  min-height: 150px;
  margin-bottom: 1em;
  padding: 0.5em;
}

button {
  padding: 10px 20px;
  margin-bottom: 20px;
  border: none;
  border-radius: 4px;
  background-color: #5cb85c;
  color: white;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
  width: 150px;
}

button:hover {
  background-color: #4cae4c;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

table {
  width: 100%;
  border-collapse: collapse;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
}

th,
td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f4f4f4;
  color: #333;
}

tbody tr:hover {
  background-color: #f9f9f9;
}
</style>
