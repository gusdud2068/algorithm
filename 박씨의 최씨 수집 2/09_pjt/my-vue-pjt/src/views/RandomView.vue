<template>
  <div class="randombox">
    <div class="card" style="height:800px">
      <button class="btn btn-success" @click="btn" style="margin-bottom:5px">PICK</button>
      <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
    name: 'RandomView',
    data(){
      return{
        movie:null,
      }
    },
    computed: {
        // movie() {
        //     // console.log(this.$store.state.movieList)
        //     this.movies=this.$store.state.moviesList
        //     return this.movies
        // }
    },
    methods:{
      btn(){
        const movielist=this.movies=this.$store.state.moviesList
        const moviepick=_.sample(movielist,1)
        this.movie=moviepick
      }
    },
    created(){
      this.btn()
    }
}
</script>

<style>
.randombox{
  display: flex;
  justify-content: center;
  margin: 10px;
}
</style>