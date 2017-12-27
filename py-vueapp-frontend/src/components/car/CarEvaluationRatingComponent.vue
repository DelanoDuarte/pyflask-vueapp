<template>
    <div class="app-car-evaluation-rating">
        <div class="row">
            <label>Rate this MTFK !!! </label>
            <star-rating :increment='0.5'> </star-rating>
        </div>
    </div>
</template>

<script>
export default {
    name: 'app-car-evaluation-rating',

    data() {
        return {
            evaluation: {
                motor: '',
                gas: '',
                apparence: '',
                support: ''
            }
        }
    },

    methods: {

        evaluateCar() {
            let data = JSON.stringify({ 'car': this.evaluation });
            fetch(`http://127.0.0.1:5000/py-vue/api/car-evaluation/${this.$route.params.id}`, {
                headers: { 'Content-Type': 'application/json' },
                method: 'POST',
                body: data,
            }).then(res => {
                res.json()
                    .then(res => {
                        console.log(res.data)
                        this.$router.push({ name: 'app-cars-list' })
                    })
            })
        },
    }
}
</script>

<style>

</style>
