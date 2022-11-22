# my-vue-pjt
# 09_pjt

## 1. 최보영

axios 를 이용하여 영화데이터를 받아서 MovieView 에 영화들 데이터를 보내는 것을 작성하는 것이 어려웠습니다. 계속 axios 에서 데이터를 받아오지 못해서 다른 분들의 도움을 받아 해결할 수 있었습니다. 

axios 를 사용할 때는 method, url을 작성하고 url에 parameter 로 넣을 정보들을 params 객체로 작성해야 한다는 점을 이번 프로젝트를 통해서 다시 한 번 복습할 수 있었습니다.

```js
export default {
    name: 'App',

    methods: {
        moviesList() {
            const TDMB_API_KEY = '5e317b8996204a8dfdf09f7c83f13ee4'
            const TDMB_URL = `https://api.themoviedb.org/3/movie/top_rated`
            axios({
                method: 'get',
                url: TDMB_URL,
                params: {
                    api_key: TDMB_API_KEY,
                    language: 'ko-KR',
                    page: 1,
                }
            }).then((response) => {
                this.$store.state.moviesList = response.data.results
            }).catch((error) => {
                console.log(error)
            })
        }
    },
}
```

- 이번 프로젝트는 vue 를 이용해 API 로 받은 데이터를 컴포넌트에 작성하는 법을 실습할 수 있었습니다. 이번이 마지막 프로젝트인데, 아직도 부족한 점이 많은 것 같습니다. 다음에는 막히는 부분이 없도록 vue 에 대해 복습하겠습니다!

<hr>

## 2. 최형운

VUEX를 사용하는 것에 대해 헷갈리던 부분이 많았으나 실습을 통해 조금이나마 이해할수 있었습니다. 
특히 store를 통한 데이터의 이동을 생각하면서 할수 있게 되었습니다. 코드를 작성할때 마냥 따라 적는게 아닌 동작하는 과정을 생각하며 할수 있게 되었습니다.

app에서 라우터를 이용하여 페이지를 이동시키고 함수를 사용하여 데이터를 보내는 것이 살짝 어렵기도 하였습니다. 생각했을때 이렇게 하면 되겠다. 하는 방법이 작동을 안하는 것을 보고 좀더 공부를 해봐야 겠다고 생각하게 되었습니다.

<hr>

## 3. 박현영

vuex를 사용하여 기능들을 구현해 내는 것에 어려움이 있었습니다.
페이지간의 데이터 이동과 연결하는 데 변수명과 명령어를 써 내는 데 많이 헷갈렸고
팀원들의 도움이 없었더라면 제 시간내에 끝낼  수 없었을 것 같습니다.

특히 axios쪽에도 어려움이 있었는데
```js
<script>
import axios from 'axios'

export default {
  name: 'App',
  methods: {
        moviesList() {
            const TDMB_API_KEY = '5e317b8996204a8dfdf09f7c83f13ee4'
            const TDMB_URL = `https://api.themoviedb.org/3/movie/top_rated`
            axios({
                method: 'get',
                url: TDMB_URL,
                params: {
                  api_key: TDMB_API_KEY,
                  language: 'ko-KR',
                  page: 1,
                }
            }).then((response) => {
                // console.log(response)
                // console.log(response.data.results)
                this.$store.state.moviesList = response.data.results
                // console.log(this.$store.state.moviesList)
            }).catch((error) => {
                console.log(error)
            })
        },
    },
    // created() {
    //     this.moviesList()
    // }
}
</script>
```
이 부분에 대해 더 공부해서 다음에는 잘 사용할 수 있도록 노력하겠습니다. 

