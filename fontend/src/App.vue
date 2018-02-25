<template>
  <div id="app">
    <div id="layer" v-if="isShow"></div>
    <Title/>
    <Panel v-on:layer="Layer" v-on:showAddBtn="showadd"/>
    <div id="waterfall">
    <old-sticker v-for="(item,index) in olditems" :key="item.uername" :username="item.username" :newdate="item.newdate" :message="item.message" v-on:delete="deleteOldSticker(index)"/>
    <new-sticker v-for="(item,index) in newitems" :key="item.key" v-on:delete="deletesticker(index)"/>
    </div>
    <Add v-if="addbtn" v-on:add="addnewsticker()"/>
  </div>
</template>

<script>
import Title from './components/Title'
import Add from './components/Add'
import oldSticker from './components/oldSticker'
import newSticker from './components/newSticker'
import Panel from './components/Panel'
import { getCookie } from './cookie'
export default {
  name: 'App',
  components: {
    Title,
    Panel,
    oldSticker,
    newSticker,
    Add
  },
  data() {
    return {
      newitems:[{key:0}],
      olditems:[],
      total:0,
      isShow:false,
      addbtn:false
    }
 },
  methods: {
    addnewsticker(){
      this.total+=1
      this.newitems.push({key:this.total})
    },
    deletesticker(i){
      this.newitems.splice(i,1)
    },
    Layer(){
      this.isShow=!this.isShow
    },
    showadd(){
      this.addbtn=!this.addbtn
    },
    deleteOldSticker(i){
      this.olditems.splice(i,1)
    }
  },
  mounted() {
    if (getCookie("username")) {
      this.addbtn=true
    }
    this.axios.get("http://127.0.0.1:5000/getMessage").then((res)=>{
      this.olditems = res.data
    });
  }
};

</script>
<style>
#layer{
  background: rgba(0,0,0,0.1);
  position: absolute;
  top: 0;
  bottom: 0;
  z-index: 1;
  width: 100%;
  height:100%;
}
body{
  background: url("assets/bg.jpg");
  background-size:cover;  
  background-attachment: fixed;
  overflow-x: hidden;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width: 100%;
  height:100%;
}
#waterfall{
  column-count:6;
  -moz-column-count:6;
  -webkit-column-count:6;
  -ms-column-count:6;
  column-width:180px;
  -moz-column-width:180px;
  -webkit-column-width:180px;
  -ms-column-width:180px;
}
</style>
