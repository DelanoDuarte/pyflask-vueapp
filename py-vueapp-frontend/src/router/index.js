import Vue from 'vue'
import Router from 'vue-router'

import HelloWorld from '@/components/HelloWorld'
import Home from '@/home/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/vuehome',
      name: 'HelloWorld',
      component: HelloWorld,
      alias: 'vueHome'
    },

    {
      path: '/',
      name: 'Home',
      component: Home,
      alias: 'customHome'
    }
  ]
})
