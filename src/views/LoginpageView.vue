
<script>
 export default {
  created: function () {
    document.body.style.backgroundImage = "url(/src/assets/login.gif)";
    document.body.style.backgroundRepeat = "no-repeat";
    document.body.style.backgroundSize = "cover";
   
  }
 };
</script>

<template>
 <div>
    <ul>
      <li class="right"><a href="/" class="nav-link">Back</a></li>
      <li class="right"><a href="/register" class="nav-link">Register</a></li>
   </ul>
    <h2>Account Login</h2>
    <div class="regform-container">
      <form>
        <div class="grid-container">
            <div class="grid-item">
              <label for="user">Username</label><br>
              <input type="text" id="form-con" name="user"><br><br>
              <button class="btn">Login</button>
            </div>
            <div  class="grid-item">
              <label for="pass">Password</label><br>
              <input type="password" id="form-con" name="pass"><br>
              
            </div>
         </div>
        </form>
    </div>
</div>  
</template>

<style>
  .btn{
        border: 2px solid black;
        padding: 14px 28px;
        font-size: 14px;
        cursor: pointer;
        font-family:Tahoma;
        font-weight: bold;
        position: relative;
        border-radius: 12px;
        background-color:beige;
        }

</style>