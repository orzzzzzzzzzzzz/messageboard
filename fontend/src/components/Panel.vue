<template>
<div id="emmmm">
<div class="options">
  <div class="login-btn" v-on:click="showlogin" v-if="loginbtn">Login</div>
  <div class="hello" v-if="showhello">hello {{ username }}!</div>
  <div class="logout-btn" v-on:click="logout" v-if="logoutbtn">Logout</div>
  <div class="register-btn" v-on:click="showregister" v-if="registerbtn">Register</div>
  </div>
  <transition name="expand1">
    <div class="panel login-panel" v-if="loginpanel">
      Username:<input type="text" name="username" v-model="username"/>
      Password :<input type="password" name="password" v-model="password" @keyup.enter="login"/>
      <div class="remind" v-show="showremind">{{ remind }}</div>
      <button  value="Cancel" v-on:click="hidelogin">Cancel</button>
      <button  type="submit" value="Submit" v-on:click="login">Submit</button>
      <div class="empty"></div>
    </div>
  </transition>
  <transition name="expand2">
    <div class="panel register-panel" v-if="registerpanel">
      Your Username:<input type="text" name="username" v-model="newUsername" />
      Password :<input type="password" name="password" v-model="newPassword1" />
      Confirm Your Password :<input type="password" name="password" v-model="newPassword2" @keyup.enter="register"/>
      <div class="remind" v-show="showremind">{{ remind }}</div>
      <button  value="Cancel" v-on:click="hideregister">Cancel</button>
      <button type="submit" value="Submit" v-on:click="register">Submit</button>
      <div class="empty"></div>
    </div>
  </transition>
  </div>
</template>
<script>
import { setCookie,getCookie,delCookie } from '../cookie'
export default {
  name: "Panel",
  data() {
    return {
      loginpanel: false,
      registerpanel: false,
      loginbtn: true,
      logoutbtn: false,
      registerbtn: true,
      showhello: false,
      showremind: false,
      username: "",
      password: "",
      newUsername: "",
      newPassword1: "",
      newPassword2:"",
      remind: ""
    };
  },
  methods: {
    showlogin() {
      this.username = ""
      this.password = ""
      this.$emit("layer")
      this.registerpanel = false
      this.loginpanel = true
    },
    showregister() {
      this.newUsername = ""
      this.newPassword1 = ""
      this.newPassword2=""
      this.$emit("layer")
      this.loginpanel = false
      this.registerpanel = true
    },
    hidelogin() {
      this.loginpanel = false
      this.remind = ""
      this.showremind = false
      this.$emit("layer")
    },
    hideregister() {
      this.registerpanel = false
      this.remind = ""
      this.showremind = false
      this.$emit("layer")
    },
    login() {
      this.remind = ""
      this.showremind = false
      if (this.username == "" || this.password == "") {
        this.remind = "用户名或密码不能为空!"
        this.showremind = true
      } else {
        let params =new URLSearchParams();
        params.append('username',this.username)
        params.append('password',this.password)
        this.axios.post("http://127.0.0.1:5000/login", params).then(res => {
          if (res.data == -1) {
            this.remind = "该用户不存在!"
            this.showremind = true
          } else if (res.data == 0) {
            this.remind = "密码输入错误!"
            this.showremind = true
          } else {
            setCookie("username", this.username, 1000 * 60);
            alert("登陆成功!ㄟ(≧◇≦)ㄏ")
            this.hidelogin()
            this.loginbtn = false
            this.registerbtn = false
            this.showhello = true
            this.logoutbtn = true
            this.$emit("showAddBtn")
          }
        });
      }
    },
    register() {
      this.remind = ""
      this.showremind = false
      if (this.newUsername == "" || this.newPassword == "") {
        this.remind = "用户名或密码不能为空!"
        this.showremind = true
      }else if(this.newPassword1!=this.newPassword2){
        this.remind="两次输入的密码不一致!"
        this.showremind=true
      }else{
        let params = new URLSearchParams();  
        params.append('username', this.newUsername);  
        params.append('password', this.newPassword1);
        this.axios.post("http://127.0.0.1:5000/register", params).then(res => {
          if (res.data == "200!") {
            alert("注册成功!┗|｀O′|┛ 嗷~~")
            this.hideregister()
            this.username = ""
            this.password = ""
            setTimeout(function(){
            	this.registerbtn = false
            	this.loginbtn = true
              this.showremind = false
              this.showlogin()
            }.bind(this),1000)
          }else if(res.data == "emmm"){
              this.remind="该用户名已被占用...嘤嘤嘤"
              this.showremind=true
          }else {
            alert("出现了故障┑(￣Д ￣)┍请稍后再试～")
            this.hideregister()
          }
        });
      }
    },
    logout() {
      delCookie("username")
      this.loginbtn=true
      this.registerbtn=true
      this.showhello=false
      this.logoutbtn=false
      this.$emit("showAddBtn")
      this.$emit("showSaveBtn")
    }
  },
  mounted() {
    if (getCookie("username")) {
      this.loginbtn = false
      this.registerbtn = false
      this.username = getCookie("username")
      this.showhello = true
      this.logoutbtn = true
    }
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.expand1-enter-active,
.expand1-leave-active {
  transition: all 0.5s;
  height: 140px;
  background: rgba(95, 132, 170, 0.7);
  overflow: hidden;
}
.expand1-enter,
.expand1-leave-to {
  height: 0;
  opacity: 0;
}
.expand2-enter-active,
.expand2-leave-active {
  transition: all 0.5s;
  height: 190px;
  background: rgba(95, 132, 170, 0.7);
  overflow: hidden;
}
.expand2-enter,
.expand2-leave-to {
  height: 0;
  opacity: 0;
}
.panel {
  background: rgba(95, 132, 170, 0.7);
  width: 190px;
  -webkit-box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.2);
  -moz-box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.2);
  -ms-box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.2);
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.2);
  margin-top: -50px;
  position: absolute;
  left: 50%;
  margin-left: -95px;
  z-index: 2;
}
.remind {
  font-size: 14px;
  margin-left: 20px;
  color: rgba(223, 5, 5, 0.8);
}
input,
button {
  background: transparent;
  outline: none;
  border: #2c3e50 1px solid;
  color: #2c3e50;
  margin: 4px;
  margin-left: 20px;
}
input {
  display: block;
}
button {
  width: 42px;
  margin-left: 20px;
  margin-top: 10px;
  display: inline-block;
}
button:hover {
  cursor: pointer;
  color: #405e7c;
}
.empty {
  height: 8px;
}
.login-btn,
.logout-btn,
.register-btn,
.hello {
  font-weight: 500;
  font-size: 20px;
  display: inline;
  margin: 10px;
}
.hello{
  font-size:22px;
  
}
.login-btn:hover {
  color: #5f84aa;
  cursor: pointer;
}
.logout-btn:hover {
  color: #5f84aa;
  cursor: pointer;
}
.register-btn:hover {
  color: #5f84aa;
  cursor: pointer;
}
.options {
  position: absolute;
  top: 25px;
  right: 20px;
}
</style>
