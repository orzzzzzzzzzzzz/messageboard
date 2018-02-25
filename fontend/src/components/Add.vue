<template>
 <div class="sticker-add-btn" v-on:click="addSticker">{{ add }}</div>
</template>

<script>
import { getCookie } from '../cookie'
export default {
  name: "Add",
  data() {
    return {
        add: "+"
    }
  },
  methods: {
    addSticker() {
      if(getCookie('username'))
      {
        this.$emit("add")
      }
      else{
        alert("请先登陆!")
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.sticker-add-btn:hover {
    background: #5f84aa;
}
.sticker-add-btn {
    width: 50px;
    height: 50px;
    background: #2c3e50;
    text-align: center;
    font-size: 40px;
    border-radius: 50%;
    padding: 0;
    color: #fff;
    position: fixed;
    right: 20px;
    bottom: 20px;
    font-weight: 700;
    -moz-box-shadow: 3px 3px 5px rgba(33,33,33,0.7);
    -webkit-box-shadow: 3px 3px 5px rgba(33,33,33,0.7);
    box-shadow: 3px 3px 5px rgba(33,33,33,0.7);
    cursor: pointer;
    line-height: 50px;
}
</style>
