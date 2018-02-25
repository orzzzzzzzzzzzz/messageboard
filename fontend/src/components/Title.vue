<template>
  <div id="title">{{ title }}</div>
</template>

<script>
export default {
  name: "Title",
  data() {
    return {
      title: "Message Board"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#title{
  margin-left: 20px;
  margin-top:20px;
  font-weight: 500;
  font-size: 26px;
}
</style>
