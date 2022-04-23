
<template>
    <div>
        <h5 id="logout"><a href="/" class="nav-link">Logout</a></h5>
        <div class="btn-container">
            <div class="route-btn"><a href="/car" class="nav-link" >Add Car</a></div>
            <div class="route-btn"><a href="/Explore" class="nav-link">Explore</a></div>
            <div class="route-btn"><a href="/profile" class="nav-link">Profile</a></div>
        </div>
    </div>
</template>

<style>
    .btn-container{
        display: grid;
        grid-template-columns: 350px 350px 350px;
        padding: 350px;
      
    }
    
    .route-btn{
        border: 2px solid rgba(255, 255, 255, 0.445);
        background-color:rgba(255, 255, 255, 0.445);
        padding: 14px 28px;
        font-size: 20px;
        cursor: pointer;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        font-family:Tahoma;
        font-weight: bold;
       
        
    }

    .route-btn:hover{
         top: -10px;
         position: relative;
         font-size: 25px;
    }
    body{
        height: 100%;
    }

    #logout{
        text-align:right;
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        right: 30px;
        position: relative;
    }

    .nav-link{
         color: rgba(15, 13, 13, 0.904);
    }

</style>

<script>
 export default {
  name: "bkg-img",
  created: function () {
    document.body.style.backgroundImage = "url(/src/assets/homepage.jpg)";
    document.body.style.backgroundRepeat = "no-repeat";
    document.body.style.backgroundSize = "cover";
   
  }
 };
</script>