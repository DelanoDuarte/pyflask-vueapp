<template>
    <div class="home">
        <div class="col-md-12">

            <h1 class="text-center"> Home </h1>

            <hr>

            <!--<canvas id="simpleChart" width="800" height="800"></canvas>-->
            <div class="row">
                <div class="col-sm-4">
                    <div class="card">
                        <div class="card-body">
                            <h4 class="card-title">Special title treatment</h4>
                            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                            <a href="#" class="btn btn-primary">Go somewhere</a>
                        </div>

                    </div>
                </div>
                <div class="col-sm-4">
                    <div class="card">
                        <div class="card-body">
                            <h4 class="card-title">Special title treatment</h4>
                            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                            <a href="#" class="btn btn-primary">Go somewhere</a>
                        </div>
                    </div>
                </div>
                <div class="col-sm-4">
                    <div class="card">
                        <div class="card-body">
                            <h4 class="card-title">Special title treatment</h4>
                            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                            <a href="#" class="btn btn-primary">Go somewhere</a>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import NamesList from './NamesList'
import Chart from 'chart.js'

export default {
    name: 'home',

    data() {
        return {

        }
    },

    created() {

    },

    mounted() {
        this.mountChart();
    },

    methods: {

        mountChart() {
            let chart = window.document.getElementById('simpleChart');

            var myLineChart = new Chart(chart, {
                type: 'line',
                data: [{
                    x: 10,
                    y: 20
                }, {
                    x: 15,
                    y: 10
                }],
                options: {
                }
            });
        }
    }
}
</script>

<style scoped>

</style>
