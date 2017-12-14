<template>
    <div class="app-brandsave">

        <div class="col-md-12">

            <div align='center'>
                <img src="https://cdn4.iconfinder.com/data/icons/transport-flat-icons-vol-1/256/39-128.png" width="128px" height="128px">
                <br />
                <h2>New Brand </h2>
            </div>

            <hr/>

            <BrandFormComponent :brand='brand' />

        </div>

    </div>
</template>

<script>
import BrandFormComponent from './BrandFormComponent'

export default {
    name: 'app-brandsave',
    components: {
        'BrandFormComponent': BrandFormComponent
    },

    data() {
        return {
            brand: {
                name: '',
                active: false
            }
        }
    },

    created() {

    },

    methods: {

    }

}
</script>

<style>

</style>
