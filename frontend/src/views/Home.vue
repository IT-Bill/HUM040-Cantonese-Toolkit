<template>
  <div class="home-container">
    <h1>欢迎来到粤语工具箱</h1>
    <p>Welcome to the Cantonese Toolkit.</p>
    <p>这个工具箱提供了一系列用于处理和分析粤语文本和语音的工具。
      <br>This toolkit offers a range of tools for processing and analyzing Cantonese text and speech.
    </p>
    <ol class="tool-list">
      <li>
        <strong>停用词</strong> - 用于识别和移除文本中常见的、意义不大的词汇，以便于分析核心内容。
        <br><strong>Stop Words</strong> - Identifies and removes common words with little meaning from the text to
        facilitate core content analysis.
      </li>
      <li>
        <strong>分词</strong> - 将粤语连续文本分割成有意义的单词或短语。
        <br><strong>Word Segmentation</strong> - Splits continuous Cantonese text into meaningful words or phrases.
      </li>
      <li>
        <strong>搜索</strong> - 提供搜索粤语文本的功能，可以根据关键词、发音或词性等进行查找。
        <br><strong>Search</strong> - Allows you to search Cantonese text by keywords, pronunciation, part of speech, and
        more.
      </li>
      <li>
        <strong>粤拼转换</strong> - 将粤语文字转换成粤拼罗马字母，帮助理解发音。
        <br><strong>Jyutping Romanization</strong> - Converts Cantonese characters into Jyutping romanization to help
        understand pronunciation.
      </li>
      <li>
        <strong>文本解析</strong> - 解析粤语句子的结构，提供语法分析。
        <br><strong>Parsing Cantonese</strong> - Parses the structure of Cantonese sentences, providing grammatical
        analysis.
      </li>
      <li>
        <strong>语音识别</strong> - 把粤语语音转换成文字，方便文本处理和分析。
        <br><strong>Speech Recognition</strong> - Converts Cantonese speech into text for convenient text processing and
        analysis.
      </li>
    </ol>

    <p>基于 <a href="https://github.com/jacksonllee/pycantonese" target="_blank" rel="noopener noreferrer">pycantonese 库</a>
      和 <a href="https://cloud.tencent.com/product/asr" target="_blank" rel="noopener noreferrer">腾讯云语音识别</a>。
      <br>These features are based on the <a href="https://github.com/jacksonllee/pycantonese" target="_blank"
        rel="noopener noreferrer">pycantonese library</a> and
      <a href="https://cloud.tencent.com/product/asr" target="_blank" rel="noopener noreferrer">Tencent Cloud Speech
        Recognition</a>.
    </p>
    <p>Author: ITBill</p>
  </div>
</template>

<script>
export default {
  name: 'Home'
  // 其他逻辑
}
</script>

<style scoped>
.home-container {
  padding: 0px 20px;
}

.tool-list {
  list-style-type: none;
  padding: 0;
}

.tool-list li {
  margin-bottom: 15px;
}

.tool-list strong {
  color: #333;
  font-weight: bold;
}</style>
