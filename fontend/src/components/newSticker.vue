<template>
  <div :class="[sticker,sticker+n]">
    <div id="tape"></div>
    <div :class="[notehead,notehead+n]">
      <span class="delete" v-on:click="deleteSticker">&times;</span>
      </div>
     <textarea :class="[note,note+n]" v-model="message"></textarea>
    <div :class="[noteinfo,noteinfo+n]">
    <div class="note-user">{{ username }}</div>
    <div class="note-time">{{ newDate }}</div>
    <div class="savebtn" v-on:click="save">✓</div>
    </div>
  </div>
</template>
<script>
import { getCookie } from '../cookie'
import { getTime } from '../getTime'
export default {
  name: "newSticker",
  data() {
    return {
      newDate:"",
      username:"",
      sticker: "sticker",
      note: "note",
      notehead: "notehead",
      noteinfo: "noteinfo",
      n: "",
      message:''
    };
  },
  methods: {
    deleteSticker() {
      this.$emit("delete")
    },
    randomColor() {
      this.n = parseInt(Math.random() * 6)
    },
    save(){
      if(getCookie('username')){
      let params = new URLSearchParams()
      params.append('username', getCookie('username'))
      params.append('message', this.message)
      params.append('newdate',this.newDate)
      this.axios.post("http://127.0.0.1:5000/store", params).then(res => {
          if (res.data== "saved"){
            alert("保存了一条留言(/≧▽≦)/")
          }else if(this.message==''){
            alert("请输入留言┑(￣Д ￣)┍")
          }else{
            alert("出现了故障┑(￣Д ￣)┍请稍后再试～")
          }
      });
     }else{
       alert("请先登陆！(๑⁼̴̀д⁼̴́๑)")
     }
    }
  },
  mounted() {
    this.newDate = getTime()
    this.randomColor()
    if(getCookie('username')){
      this.username=getCookie('username')
    }
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.sticker {
  float: left;
  position: relative;
  width: 160px;
  margin: 20px;
  margin-top: 30px;
  -webkit-box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.2);
  -moz-box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.2);
  -ms-box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.2);
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.2);
  break-inside: avoid;
  -moz-colum-break-inside: avoid;
  -webkit-column-break-inside: avoid;
  -ms-column-break-inside: avoid;
}
#tape {
  width: 74px;
  height: 30px;
  background: rgba(0, 0, 0, 0.1);
  position: absolute;
  top:-16px;
  left: 38px;
  border-left: 2px dotted rgba(0, 0, 0, 0.06);
  border-right: 2px dotted rgba(0, 0, 0, 0.06);
  -webkit-box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.2);
  -moz-box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.2);
  box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.2);
}
#tape:hover{
  cursor: pointer;
}
.note {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  font-size:16px;
  height: 170px;
  width:140px;
  max-height:180px;
  max-width:140px;
  resize: none;
  box-sizing: border-box;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
  -webkit-user-modify: read-write-plaintext-only;
  border-style:none;
  background:transparent;
  outline: 0;
  margin: 10px;
  margin-top:22px;
}

.notehead {
  display: flex;
  align-items: center;
  width: 160px;
  height: 20px;
}

.delete {
  position: absolute;
  right: 4px;
  color: rgb(194, 192, 192);
  font-size: 20px;
  cursor: pointer;
}
.delete:hover {
  color: #fff;
}
.noteinfo {
  width: 150px;
}
.note-user,
.note-time {
  color: #fff;
  font-size: 16px;
  margin-top:4px;
  margin-left: 4px;
}
.savebtn{
  color:#fff;
  cursor: pointer;
  width: 20px;
  height: 20px;
  background: transparent;
  text-align: center;
  font-size: 20px;
  border-radius: 50%;
  border:1px #fff solid;
  line-height: 22px;
  position: absolute;
  right:10px;
  bottom:10px;
}
.sticker0,
.note0,
.noteinfo0 {
  background: #f36c60;
}
.notehead0 {
  background: #e84e40;
}
.sticker1,
.note1,
.noteinfo1 {
  background: #9575cd;
}
.notehead1 {
  background: #7e57c2;
}
.sticker2,
.note2,
.noteinfo2 {
  background: #aed581;
}
.notehead2 {
  background: #9ccc65;
}
.sticker3,
.note3,
.noteinfo3 {
  background: #ffb74d;
}
.notehead3 {
  background: #ffa726;
}
.sticker4,
.note4,
.noteinfo4 {
  background: #a1887f;
}
.notehead4 {
  background: #8d6e63;
}
.sticker5,
.note5,
.noteinfo5 {
  background: #90a4ae;
}
.notehead5 {
  background: #78909c;
}
</style>
