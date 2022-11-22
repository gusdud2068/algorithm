<template>
    <div>
        <MovieCard
            v-for="movie in moviesList" :key="movie.id"
            :movie="movie"
        />
    </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
    name: 'MovieView',

    // data() {
    //     return {
    //         moviesList : []
    //     }
    // },
    components: { MovieCard },
    computed: {
        moviesList() {
            // console.log(this.$store.state.movieList)
            return this.$store.state.moviesList
        }
    }
}
</script>

<style>
.flex {
    display: flex;
}
</style>