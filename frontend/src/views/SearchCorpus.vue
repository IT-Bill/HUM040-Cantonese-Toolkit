<template>
  <div>
    <div>
      <p>语料库语言学工作中的一个常见任务是搜索感兴趣的特定元素。
        <br>can search for specific Jyutping elements, Chinese characters, part-of-speech tags, and any combinations of
        these.
      </p>
      <p>对于给定的语料库，它可以搜索特定的粤拼元素、汉字、词性标记以及这些的任意组合。
        <br>A common task in corpus-based linguistic work is to search for specific elements of interest.
      </p>

      <h2>粤拼参数 Jyutping Parameters:</h2>
      <ul>
        <li>声母 (onset) - 粤语中音节开头的辅音或辅音群。A consonant or consonant cluster that begins a syllable in Cantonese.</li>
        <li>韵核 (nucleus) - 粤语音节中的元音或音节性元素。The vowel or syllabic element in the middle of a syllable in Cantonese.</li>
        <li>声尾 (coda) - 粤语音节末尾的辅音。The final consonant or consonants at the end of a syllable in Cantonese.</li>
        <li>声调 (tone) - 粤语音节的声调走向。The pitch contour of a syllable in Cantonese.</li>
        <li>聲母 (initial) - 相当于声母，在粤语中指一个字的开始发音部分。Equivalent to the onset, referring to the initial sound of a word in
          Cantonese.</li>
        <li>韻母 (final) - 相当于韵核加声尾，在粤语中指一个字的中至尾的发音部分。Equivalent to nucleus plus coda, denoting the part of a syllable from
          the middle to the end in Cantonese.</li>
        <li>粤拼 (jyutping) - 一个完整的粤语音节的罗马拼写，即声母加韵核加声尾加声调。The complete romanization of a Cantonese syllable, i.e., onset
          plus nucleus plus coda plus tone.</li>
      </ul>

    </div>
    <!-- 输入区域 -->
    <div>
      <label for="nucleus-input">韵核 Nucleus: </label>
      <input id="nucleus-input" v-model="nucleus" placeholder="Example: aa" />
    </div>
    <div>
      <label for="tone-input">声调 Tone: </label>
      <input id="tone-input" v-model="tone" placeholder="Example: 2" />
    </div>
    <div>
      <label for="character-input">字符 Character: </label>
      <input id="character-input" v-model="character" placeholder="Example: 嘢" />
    </div>
    <div>
      <label for="pos-input">词性 Pos: </label>
      <input id="pos-input" v-model="pos" placeholder="Example: V" />
    </div>
    <button @click="searchCorpus">Search</button>

    <!-- 搜索结果表格 -->
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
</template>

<script>
import axios from 'axios';

export default {
  name: 'SearchCorpus',
  data() {
    return {
      nucleus: '',
      tone: '',
      character: '',
      pos: '',
      searchResults: [],
      currentPage: 1,
      pageSize: 10,
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.searchResults.length / this.pageSize);
    },
    paginatedData() {
      const start = (this.currentPage - 1) * this.pageSize;
      const end = start + this.pageSize;
      return this.searchResults.slice(start, end);
    },
  },
  methods: {
    searchCorpus() {
      // ... 发送请求的逻辑
      axios.post('http://localhost:8090/search', this.buildSearchParams())
        .then(response => {
          this.searchResults = response.data;
          this.currentPage = 1; // 每次搜索重置为第一页
        })
        .catch(error => {
          console.error('Search error:', error);
        });
    },
    buildSearchParams() {
      return {
        nucleus: this.nucleus,
        tone: this.tone,
        character: this.character,
        pos: this.pos
      };
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage += 1;
      }
    },
  },
};
</script>

<style scoped>
.flex-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

input {
  margin-bottom: 10px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  width: 300px;
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

