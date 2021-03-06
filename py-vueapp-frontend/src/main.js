// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import ModalComponent from './components/modal-component/ModalComponent'
import VueFlash from 'vue-flash'

import StarRating from 'vue-star-rating'


import Message from './components/message/Message'

Vue.config.productionTip = false

Vue.component('flash', VueFlash)
Vue.component('star-rating', StarRating)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {
    App
  }
})

// new Vue({
//   el: '#app-message',
//   template: '<Message/>',
//   components: { Message }
// })