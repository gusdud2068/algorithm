<template>
    <div class="card">
  <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">{{ movie.title }}</h5>
    <p class="card-text">{{ movie.overview }}</p>
  </div>
  </div>
</template>

<script>
export default {
name: 'MovieCard',
props: {
      movie: Object
    }
};
</script>

<style>
.card{
  float:left;
  height: 1000px;
  width: 30%;
  margin: 10px;
  padding: 0;
  overflow: hidden;
  border-radius: 20px;

}
.card-img-top{
  height: 700px;
}
</style>