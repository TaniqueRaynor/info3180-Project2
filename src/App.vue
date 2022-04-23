<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppFooter from "@/components/AppFooter.vue";

</script>

<template>

  <main>
    <RouterView />
     <AppFooter />
  </main>
  
 
</template>

<style>
body {
  padding-top: 75px;
  background-image: url("/src/assets/addcar.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

</style>
