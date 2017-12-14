<template>
    <div class="app-cars-list">
        <div class="col-md-12">

            <div align='center'>
                <img src="https://cdn4.iconfinder.com/data/icons/transport-flat-icons-vol-1/256/39-128.png" width="128px" height="128px">
                <br />
                <h2>Car List </h2>
            </div>

            <hr>
            <CarGridComponent :cars='cars' />

            <hr />
            <div class="row">
                <router-link :to="{name: ''}" class="btn btn-primary">
                    New Car
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import CarGridComponent from './CarGridComponent'

export default {
    name: 'app-cars-list',
    components: {
        'CarGridComponent': CarGridComponent
    },

    data() {
        return {
            cars: []
        }
    },

    created() {
        this.getCarsJson();
    },

    methods: {

        getCarsJson() {
            fetch('http://127.0.0.1:5000/py-vue/api/cars')
                .then(res => res.json()
                    .then(res => {
                        this.cars = res.cars
                    }))
        }
    }
}
</script>

<style>

</style>
