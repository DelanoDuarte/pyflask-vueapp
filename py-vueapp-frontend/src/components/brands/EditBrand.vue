<template>
    <div class="app-brand-edit">
        <div class="col-md-12">

            <div align='center'>
                <img src="https://cdn4.iconfinder.com/data/icons/transport-flat-icons-vol-1/256/39-128.png" width="128px" height="128px">
                <br />
                <h2>Edit Brand </h2>
            </div>

            <hr/>

            <form v-on:submit.prevent="updateBrand">
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

                <hr>
                <div class="row">
                    <div class="col-sm-12 text-center">
                        <button type="submit" class="btn btn-success">Update </button>
                        <router-link :to="{name:'app-brandlist'}" class="btn btn-warning">Cancel</router-link>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    name: 'app-brand-edit',

    data() {
        return {
            brand: ''
        }
    },

    created() {
        this.getBrandById()
    },

    methods: {

        getBrandById() {
            fetch(`http://127.0.0.1:5000/py-vue/api/brands/${this.$route.params.id}`)
                .then(res => res.json()
                    .then(res => {
                        this.brand = res.brand;
                    }))
        },

        updateBrand() {
            let data = JSON.stringify({ 'brand': this.brand });
            fetch(`http://127.0.0.1:5000/py-vue/api/brands/${this.$route.params.id}`, {
                headers: { 'Content-Type': 'application/json' },
                method: 'PUT',
                body: data,
            }).then(res => res.json()
                .then(res => {
                    this.$router.push({ name: 'app-brandlist' })
                }))
        }

    }
}
</script>

<style>

</style>
