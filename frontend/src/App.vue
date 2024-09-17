<template>
  <div id="app">
    <DrawerMenu :menuItems="features" @select="selectFeature" />
    <router-view />
  </div>
</template>

<script>
import DrawerMenu from './components/DrawerMenu.vue';

export default {
  name: 'App',
  components: {
    DrawerMenu
  },
  data() {
    return {
      features: [
        '主页 Home', 
        '停用词 Stop Words', 
        '分词 Word Segmentation', 
        '搜索 Search', 
        '拼音 Jyutping Romanization',
        '文本解析 Parsing Cantonese',
        '语音识别 Speech Recognition'
      ]
    }
  },
  methods: {
    selectFeature(feature) {
      // 当一个特性被选中时，使用router来导航
      this.$router.push({ name: feature });
    }
  }
}
</script>

<style>
.flex-col {
  display: flex;
  flex-direction: column;
}
</style>