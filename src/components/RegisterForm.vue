<script>
    export default {
    created(){
        this.getCsrfToken();

    },
    
    data(){
        return {
            csrf_token: ''
        }
    },
     created: function () {
        document.body.style.backgroundImage = "url(/src/assets/register.jpg)";
        document.body.style.backgroundRepeat = "no-repeat";
     },
    methods : {
        register(){

            let regForm = document.getElementById('regForm');
            let form_data = new FormData(regForm);

            fetch("/api/register", {
                method: 'POST',
                body: form_data,
                headers: {'X-CSRFToken': this.csrf_token}
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                
                if (data.status == 200){
                    
                }
                
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        }
    },
    
}

</script>

<template>
  <div>
    <ul>
      <li class="right"><a href="/" class="nav-link">Back</a></li>
      <li class="right"><a href="/Login" class="nav-link">Login</a></li>
   </ul>
  <div class="reg-container">
    <h2>Register</h2>
    <div class="regform-container">
      <form @submit.prevent="register" id="regForm" method="POST">
        <div class="grid-container">
            <div class="grid-item">
              <label for="user">Username</label><br>
              <input type="text" id="form-con" name="user"><br> 
            </div>
            <div  class="grid-item">
              <label for="pass">Password</label><br>
              <input type="password" id="form-con" name="pass"><br>
            </div>
            <div class="grid-item">
              <label for="name">Fullname</label><br>
              <input type="text" id="form-con" name="name" ><br>
            </div>
            <div class="grid-item">
              <label for="email">Email</label><br>
              <input type="text" id="form-con" name="email" placeholder="johndoe@gmail.com"><br>
            </div>
           <div class="grid-item">
              <label for="location">Location</label><br>
              <input type="text" id="form-con" name="location"><br>
          </div>
        </div>
         <br>
          <label for="Bio">Biography</label><br><br>
          <textarea id="bio" rows="5" cols="100"></textarea><br>
          <label for="photo">Upload Photo</label><br>
          <input type="file" id="file" name="file"/><br>
          <button type="submit" id="reg">Register</button>
    </form>
    </div>
  </div>
 </div>
</template>

<style>
 .regform-container{
    border: 2px inset rgb(231, 225, 225);
    padding-left: 50px;
    padding-top: 35px;
    padding-bottom: 50px;
    margin-right: 280px;
    margin-left: 300px;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
    border-radius: 10px;
    width:60%;
    position: relative;
        

  }

#bio{
      background-color: beige;
      border-radius: 20px;
  }

  #reg{
      padding: 10px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 4px 2px;
      cursor: pointer;
      background-color:rgba(128, 128, 128, 0.87);
      color:  #e7e7e7;
      border-radius: 7px;
      font-family: Tahoma;
      font-weight: bold;
  }

  h2{
      left: 300px;
      position: relative;
      color: #ffffff;
  }

  label{
    color: #e7e7e7;
  }

</style>