import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import StopWords from '../views/StopWords.vue'
import WordSegmentation from '../views/WordSegmentation.vue'
import SearchCorpus from '../views/SearchCorpus.vue'
import JyutpingRomanization from '../views/JyutpingRomanization.vue'
import ParsingCantonese from '../views/ParsingCantonese.vue'
import SpeechRecognition from '../views/SpeechRecognition.vue'

const routes = [
  {
    path: '/',
    name: '主页 Home',
    component: Home
  },
  {
    path: '/stop-words',
    name: '停用词 Stop Words',
    component: StopWords
  },
  {
    path: '/word-segmentation',
    name: '分词 Word Segmentation',
    component: WordSegmentation
  },
  {
    path: '/search',
    name: '搜索 Search',
    component: SearchCorpus
  },
  {
    path: '/jyutping-romanization',
    name: '拼音 Jyutping Romanization',
    component: JyutpingRomanization
  },
  {
    path: '/parsing-cantonese',
    name: '文本解析 Parsing Cantonese',
    component: ParsingCantonese
  },
  {
    path: '/speech-recognition',
    name: '语音识别 Speech Recognition',
    component: SpeechRecognition
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
