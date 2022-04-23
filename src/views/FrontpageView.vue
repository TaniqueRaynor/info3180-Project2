<script>
 export default {
  created: function () {
    document.body.style.backgroundImage = "url(/src/assets/frontpage.jpg)";
    document.body.style.backgroundRepeat = "no-repeat";
    document.body.style.backgroundSize = "60% 1000px";
   
  }
 };
</script>

<template>
        <div class="btn-con">
            <div class="login-btn"><a href="/Login" class="nav" >&nbsp;&nbsp;&nbsp;Login</a></div>
            <div class="reg-btn"><a href="/register" class="nav">Register</a></div>
        </div>
</template>

<style >
     .btn-con{
        display: grid;
        grid-template-columns: 170px 170px;
        padding: 350px;
      
    }
    
    .login-btn, .reg-btn{
        border: 2px solid black;
        padding: 14px 28px;
        font-size: 20px;
        cursor: pointer;
        font-family:Tahoma;
        font-weight: bold;
        position: relative;
        left: 980px;
        top:70px;
        border-radius: 12px;
        margin-left: 30px;
        margin-right: -10px;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;
        }

    .nav{
        color: aliceblue;
        text-decoration: none;
       

    }

    .login-btn{
        background-color: rgb(48, 117, 46);
    }

    .reg-btn{
        background-color: rgb(179, 2, 2);
    }
    
    .login-btn:hover{
        background-color: rgb(3, 172, 3)
    }

    .reg-btn:hover{
        background-color: red;
    }

</style>