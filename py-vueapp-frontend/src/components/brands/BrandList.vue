<template>
    <div class="app-brandlist">
        <div class="col-md-12">

            <app-brand-grid-component :brands='brands.data' />

            <hr />
            <div class="row">
                <router-link :to="{name: 'app-brandsave'}" class="btn btn-primary">
                    New Brand
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import BrandGridComponent from './BrandGridComponent'

export default {
    name: 'app-brandlist',
    components: {
        'app-brand-grid-component': BrandGridComponent
    },

    data() {
        return {
            brands: []
        }
    },

    created() {
        this.getBrands();
    },

    methods: {
        getBrands() {
            fetch('http://127.0.0.1:5000/py-vue/api/brands')
                .then(res => {
                    res.json()
                        .then(res => {
                            this.brands = res
                        })
                })
        }
    }

}
</script>

<style>

</style>
