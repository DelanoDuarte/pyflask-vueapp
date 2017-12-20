<template>
    <div class="app-cars-grid-component">
        <table class="table">
            <thead class="thead-dark">
                <tr>
                    <th>Car Model</th>
                    <th>Brand</th>
                    <th>Car Price</th>
                    <th>Car Year</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="car in cars" v-bind:key="car._id">
                    <td> {{car.model}}</td>
                    <td> {{car.brand.name}}</td>
                    <td> $ {{car.price}}</td>
                    <td> {{car.year}}</td>
                    <td>
                        <div class="text-center">
                            <router-link :to="{name:'app-cars-edit', params:{'id':car._id}}" class="btn btn-success">Edit</router-link>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>

    </div>
</template>

<script>
export default {
    name: 'app-cars-grid-component',
    props: ['cars'],

    data() {
        return {

        }
    }
}
</script>

<style>

</style>
