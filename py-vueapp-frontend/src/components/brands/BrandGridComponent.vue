<template>
    <div class="app-brand-grid-component">
        <table class="table">
            <thead class="thead-dark">
                <tr>
                    <th>Brand Name</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="brand in brands" v-bind:key="brand._id">

                    <td><img src="https://image.flaticon.com/icons/png/512/364/364602.png" width="24px" height="24px"> {{brand.name}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'app-brand-grid-component',
    props: ['brands'],

    data() {
        return {

        }
    }
}
</script>

<style>

</style>
