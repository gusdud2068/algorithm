import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    moviesList : [],
    adding:null
  },
  getters: {
  },
  mutations: {
    ADD(state,content){
      return this.state.adding=content
    },
  },
  actions: {
  },
  modules: {
  }
})
