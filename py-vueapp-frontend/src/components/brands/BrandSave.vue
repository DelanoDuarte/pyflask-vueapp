<template>
    <div class="app-brandsave">

        <div class="col-md-12">

            <div align='center'>
                <img src="https://cdn4.iconfinder.com/data/icons/transport-flat-icons-vol-1/256/39-128.png" width="128px" height="128px">
                <br />
                <h2>New Car </h2>
            </div>

            <hr/>

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
                    <button type="submit" class="btn btn-success">Save </button>
                </div>
            </form>
        </div>

    </div>
</template>

<script>
export default {
    name: 'app-brandsave',

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
