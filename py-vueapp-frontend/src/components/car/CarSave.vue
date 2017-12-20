<template>
    <div class="app-car-save">
        <div align='center'>
            <img src="https://cdn4.iconfinder.com/data/icons/transport-flat-icons-vol-1/256/39-128.png" width="128px" height="128px">
            <br />
            <h2>{{title}} </h2>
        </div>

        <hr>
        <CarFormComponent :car='car' />
    </div>
</template>

<script>
import CarFormComponent from './CarFormComponent'

export default {
    name: 'app-car-save',
    components: {
        'CarFormComponent': CarFormComponent
    },

    data() {
        return {
            title: 'New Car',
            car: {
                model: '',
                brand: '',
                price: '',
                year: undefined
            }
        }
    },

    created() {
        this.checkEdit();
    },

    methods: {

        checkEdit() {
            let params = this.$route.params
            if (params.id) {
                this.title = 'Edit Car'
                this.getCarById();
            }
        },

        getCarById() {
            fetch(`http://127.0.0.1:5000/py-vue/api/cars/${this.$route.params.id}`)
                .then(res => res.json()
                    .then(res => {
                        this.car = res;
                    }))
        },

    }

}
</script>

<style scoped>

</style>
