<template>
  <div >
      <WatchListItem
      v-for="(list,index) in addwant"
    :key="index"
    :list="list"
      />
  </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem'
export default {
    name: 'WatchListForm',
    data(){
      return{
        wantlist:[],
      }
    },

    components:{
      WatchListItem
    },
    computed:{
      addwant(){
        return this.$store.state.adding
      }
    },
    methods:{
    }

}
</script>

<style>

</style>