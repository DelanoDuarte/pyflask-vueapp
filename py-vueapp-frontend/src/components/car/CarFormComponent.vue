<template>
    <div class="app-car-form-component">
        <form v-on:submit.prevent="savenNewCar">

            <div class="row">
                <div class="form-group col-md-8">
                    <label for="carModel">Car Model</label>
                    <input type="text" required class="form-control" v-model="car.model" id="carModel" placeholder="Lexus 2.0, Yellow Camaro 2.0">
                </div>
                <div class="form-group col-md-4">
                    <label for="carBrand">Brand</label>
                    <select v-model="car.brand" class="form-control" id="carBrand" required>
                        <option selected>Select </option>
                        <option v-for="brand in brands" v-bind:key="brand._id" :value="brand">{{brand.name}} </option>
                    </select>
                </div>
            </div>

            <div class="row">
                <div class="form-group col-md-3">
                    <label for="carPrice">Car Price</label>
                    <input type="number" required class="form-control" v-model="car.price" id="carPrice" placeholder="$ 15.564">
                </div>
            </div>

            <div class="row">
                <div class="form-group col-md-4">
                    <label for="carYear">Car Year</label>
                    <input type="number" min="1900" max="2099" step="1" required class="form-control" v-model="car.year" id="carYear" placeholder="2015">
                </div>
            </div>

            <div class="row">
                <div class="col-md-12 text-center">
                    <button type="submit" class="btn btn-success">Save </button>
                    <router-link :to="{name:'app-cars-list'}" class="btn btn-warning">Cancel</router-link>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import Message from './../message/Message'

export default {
    name: 'app-car-form-component',
    props: ['car'],
    components: {
        'Message': Message
    },

    data() {
        return {
            brands: [],
            showMessage: false
        }
    },

    created() {
        this.getBrands()
    },

    methods: {

        getBrands() {
            fetch('http://127.0.0.1:5000/py-vue/api/brands')
                .then(res => {
                    res.json()
                        .then(res => {
                            this.brands = res.data
                        })
                })
        },

        savenNewCar() {
            if (this.car.carId) {
                this.updateCar();
                return
            }
            this.saveCar()
        },

        saveCar() {
            let data = JSON.stringify({ 'car': this.car });
            fetch('http://127.0.0.1:5000/py-vue/api/cars', {
                headers: { 'Content-Type': 'application/json' },
                method: 'POST',
                body: data,
            }).then(res => {
                res.json()
                    .then(res => {
                        console.log(res.data)
                        this.$emit('saved')
                        //flash('New Car Sucessfuly Saved !', 'success')
                        this.$router.push({ name: 'app-cars-list' })
                    })
            })
        },

        updateCar() {
            let data = JSON.stringify({ 'car': this.car });
            fetch(`http://127.0.0.1:5000/py-vue/api/cars/${this.car.carId}`, {
                headers: { 'Content-Type': 'application/json' },
                method: 'PUT',
                body: data,
            }).then(res => {
                res.json()
                    .then(res => {
                        console.log(res.data)
                        this.$router.push({ name: 'app-cars-list' })
                    })
            })
        }

    }
}
</script>

<style>

</style>
