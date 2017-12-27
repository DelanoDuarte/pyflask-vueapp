import Vue from 'vue'
import Router from 'vue-router'

import HelloWorld from '@/components/HelloWorld'
import Home from '@/home/Home'

/** Brand Components*/
import BrandSave from '@/components/brands/BrandSave'
import BrandList from '@/components/brands/BrandList'
import EditBrand from '@/components/brands/EditBrand'

/** Car Components*/
import CarList from '@/components/car/CarList'
import CarSave from '@/components/car/CarSave'
import CarEvaluation from '@/components/car/CarEvaluation'


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
    },

    {
      path: '/cars',
      name: 'app-cars-list',
      component: CarList,
      alias: 'app-cars-list'
    },
    {
      path: '/cars/new',
      name: 'app-cars-save',
      component: CarSave,
      alias: 'app-cars-save'
    },
    {
      path: '/cars/:id',
      name: 'app-cars-edit',
      component: CarSave,
      alias: 'app-cars-edit'
    },
    {
      path: '/car/evaluate/:id',
      name: 'app-cars-evaluation',
      component: CarEvaluation,
      alias: 'app-cars-evaluation'
    }
  ]
})
