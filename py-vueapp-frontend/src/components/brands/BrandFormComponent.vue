<template>
    <div class="app-brand-save-form">
        <form v-on:submit.prevent="saveNewBrand">
            <div class="row">
                <div class="form-group col-md-8">
                    <label for="brandName">Name</label>
                    <input type="text" required class="form-control" v-model="brand.name" id="brandName" placeholder="Ferrari, BMW , Chevrolet">
                </div>
            </div>

            <div class="row">
                <div class="form-group">
                    <label for="brandActive">Active Brand ?</label>
                    <input type="checkbox" class="form-control" id="brandActive" v-model="brand.active">
                </div>
            </div>

            <div class="row">
                <div class="col-md-12 text-center">
                    <button type="submit" class="btn btn-success">Save </button>
                    <router-link :to="{name:'app-brandlist'}" class="btn btn-warning">Cancel</router-link>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: 'app-brand-save-form',
    props: ['brand'],

    data() {
        return {

        }
    },

    created() {

    },

    methods: {
        saveNewBrand() {
            let data = JSON.stringify({ 'brand': this.brand });
            fetch('http://127.0.0.1:5000/py-vue/api/brands', {
                headers: { 'Content-Type': 'application/json' },
                method: 'POST',
                body: data,
            })
                .then(res => {
                    res.json()
                        .then(res => {
                            console.log(res.data)
                            this.$router.push({ name: 'app-brandlist' })
                        })
                })
        }
    }

}
</script>

<style>

</style>
