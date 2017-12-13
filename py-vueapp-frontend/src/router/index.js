import Vue from 'vue'
import Router from 'vue-router'

import HelloWorld from '@/components/HelloWorld'
import Home from '@/home/Home'

/** Brand Components*/
import BrandSave from '@/components/brands/BrandSave'
import BrandList from '@/components/brands/BrandList'
import EditBrand from '@/components/brands/EditBrand'

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
    },

    {
      path: '/brands',
      name: 'app-brandlist',
      component: BrandList,
      alias: 'app-brandlist',
    },

    {
      path: '/brands/new',
      name: 'app-brandsave',
      component: BrandSave,
      alias: 'app-brandsave'
    },
    {
      path: '/brands/edit/:id',
      name: 'app-brand-edit',
      component: EditBrand,
      alias: 'app-brand-edit'
    }
  ]
})
