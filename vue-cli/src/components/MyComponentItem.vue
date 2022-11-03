<template>
    <div>
        <h3>하위커포넌트래용</h3>
        <p> {{staticProps}} </p>
        <p> {{myProps}} </p>
        <button @click="childToParent">클릭!</button>
    </div>
  
</template>


<script>


export default {
    name : 'MyComponentItem',
    props : {
        staticProps : String,
        myProps : String,
    },
    methods: {
        childToParent: function(){
            this.$emit('child-to-parent',"나는 자식이 보낸 데이터다")
        }
    }

}
</script>

<style>

</style>