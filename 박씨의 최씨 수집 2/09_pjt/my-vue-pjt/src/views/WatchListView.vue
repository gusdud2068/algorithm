<template>
  <div class="mainbox">
    <div class="titlebox" style="width:90%; background-color:#e3f2fd; margin:30px">
      <h1>보고싶은 영화</h1>
      <div class="mainbox">
        <input type="text" v-model="wantmovie" placeholder="뭐보고 싶냐">
        <button @click="createmovie">Add</button>
      </div>
      <WatchListForm/>
    </div>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm'
export default {
    name: 'WatchListView',
    data(){
      return{
        wantmovie:null,
        wantlist:[]
      }
    },
    components:{
      WatchListForm,
    },
    methods:{
      createmovie(){
        const content=this.wantmovie
        this.wantlist.push(content)
        this.$store.commit('ADD',this.wantlist)
        this.wantmovie=null
      }
    }
}
</script>

<style>
.mainbox{
  display:flex; 
  justify-content: center;
  margin-bottom: 20px;
}
.titlebox{
  width:90%; 
  background-color:#e3f2fd; 
  margin:30px;
  border-radius: 20px;
  padding-top:20px
}
.margin{
  margin: auto;
}

</style>