<template>
  <div class="drawer-menu">
    <button v-for="item in menuItems" :key="item" @click="selectFeature(item)">
      {{ item }}
    </button>
  </div>
</template>
  
<script>
export default {
  name: 'DrawerMenu',
  props: {
    menuItems: Array
  },
  methods: {
    selectFeature(item) {
      this.$emit('select', item);
    }
  }
}
</script>
  
<style scoped>
.drawer-menu button {
  background-color: #ffffff; /* 背景颜色 */
  color: #333333; /* 文字颜色 */
  border: 2px solid #dddddd; /* 边框颜色 */
  padding: 10px 20px; /* 内填充空间 */
  margin: 5px; /* 外边距 */
  /* text-transform: uppercase; 文字大写 */
  font-weight: bold; /* 字体加粗 */
  border-radius: 5px; /* 边框圆角 */
  outline: none; /* 移除焦点时的轮廓线 */
  cursor: pointer; /* 鼠标悬停时的指针样式 */
  transition: all 0.3s ease; /* 过渡动画 */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* 盒子阴影 */
}

.drawer-menu button:hover {
  background-color: #eeeeee; /* 按钮悬停背景颜色 */
  color: #555555; /* 按钮悬停文字颜色 */
  border-color: #cccccc; /* 按钮悬停边框颜色 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* 按钮悬停盒子阴影 */
}

.drawer-menu button:active {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2); /* 按钮按下时的盒子阴影 */
  transform: translateY(1px); /* 按钮按下时的微小移动 */
}
</style>

  