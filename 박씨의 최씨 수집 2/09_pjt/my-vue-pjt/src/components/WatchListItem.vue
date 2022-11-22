<template>
  <div class="movielist" @click="btnClick" :class="{selected:btn}" >
    <h1>{{list}}</h1>
  </div>
</template>

<script>
export default {
    name: 'WatchListItem',
    props:{
      list:String
    },
    data(){
      return {
        btn:false,
      }
    },
    methods:{
      btnClick(){
        this.btn = !this.btn
      }
    }
}
</script>

<style>
.movielist{
  width: 100%;
  height: 70px;
  background-color: lightgray;
  padding: 15px;
  border: 1px solid white;
}
.selected{
  text-decoration: line-through;
  background-color: gray;
}
</style>