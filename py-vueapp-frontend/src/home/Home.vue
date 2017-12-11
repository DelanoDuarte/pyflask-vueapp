<template>
    <div class="home">
        <div class="col-md-12">

            <h2>Home </h2>
            <hr>

            <div class="row">
                <div class="form-group col-md-8">
                    <label>Name: </label>
                    <input class="form-control" v-model="name" required='true'>
                </div>
            </div>

            <div class="row">
                <button v-on:click='saveName' v-if="name !== undefined" class="btn btn-success btn-lg"> Add </button>
            </div>

            <hr>
            <NamesList :items="names"></NamesList>

        </div>
    </div>
</template>

<script>
import NamesList from './NamesList'

export default {
    name: 'home',
    components: {
        'NamesList': NamesList
    },

    data() {
        return {
            name: undefined,
            names: []
        }
    },

    created() {
        this.getName();
    },

    methods: {
        getName() {
            fetch('http://127.0.0.1:5000/py-vue/api/test')
                .then(res => {
                    res.json()
                        .then(res => {
                            this.names = res.data
                        })
                })
        },

        saveName() {
            let data = JSON.stringify({ 'name': this.name });
            fetch('http://127.0.0.1:5000/py-vue/api/test', {
                headers: { 'Content-Type': 'application/json' },
                method: 'POST',
                body: data,
            })
                .then(res => {
                    res.json()
                        .then(res => {
                            console.log(res.data)
                            this.getName();
                            this.name = undefined
                        })
                })
        }
    }

}
</script>

<style scoped>

</style>
