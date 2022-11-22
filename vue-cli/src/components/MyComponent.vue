<template>
    <div class = "border">
        <h1>싸피에서 살아남기이지롱</h1>
        <Mychild static-props="component에서 child로"/>
        <MyComponentItem 
        static-props = "mycomponent에서 보낸 데이터"
        :my-props="dynamicProps"
        @child-to-parent="parentGetEvent"
        />
 
    </div>
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem';

export default {
    name: 'MyComponent',
   
    components: {
        MyComponentItem,
    },
    data: function() {
        return {
            dynamicProps: '이건 동적인 데이터!',
        }
    },
    methods: {
        parentGetEvent: function (childData){
            console.log('용돈없지롱!!')
            console.log(childData)
            
        }
    }
}
</script>

<style>
 .border {
    border: solid 1px;
 }
</style>