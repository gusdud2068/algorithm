<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComponent/>
    <HelloWorld msg-title="이게 뭔데"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
//1.불러오기
//import MyComponent from './components/MyComponent.vue'
import MyComponent from '@/components/MyComponent';


export default {
  name: 'App',
  components: {
    HelloWorld,
    //2. 등록하기
    MyComponent,
    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
