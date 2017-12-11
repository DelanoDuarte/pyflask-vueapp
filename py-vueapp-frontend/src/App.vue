<template>
  <div id="app">
    <custom-navbar>
    </custom-navbar>

    <div class="custombody">
      <div class="container">
        <router-view/>
      </div>
    </div>

  </div>
</template>

<script>
import NavBar from '@/components/layout/NavBar'

export default {
  name: 'app',
  components: {
    'custom-navbar': NavBar
  }
}
</script>

<style>
#app {
  /*font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;*/
}

.custombody {
  margin-top: 60px;
}
</style>
