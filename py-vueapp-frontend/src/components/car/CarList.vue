<template>
    <div class="app-cars-list">
        <div class="col-md-12">

            <div align='center'>
                <img src="https://cdn4.iconfinder.com/data/icons/transport-flat-icons-vol-1/256/39-128.png" width="128px" height="128px">
                <br />
                <h2>Cars</h2>
            </div>
            <hr>
                
            <div class="row">
                <div class="col-sm-4">
                    <div class="card">
                        <div class="card-body">
                            <div align='center'>
                                <img src="https://image.flaticon.com/icons/png/512/196/196601.png" width="64px" height="64px">
                                <hr>
                                <h3>Chevrolet</h3>
                                <p>Most Evaluated Brand</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-sm-4">
                    <div class="card">
                        <div class="card-body">
                            <div align='center'>
                                <img src="http://healthyteambucket.s3-website-us-east-1.amazonaws.com/profile/1314.png" width="64px" height="64px">
                                <hr>
                                <h3>BMW - IX300</h3>
                                <p>Better Car Evaluation</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-sm-4">
                    <div class="card">
                        <div class="card-body">
                   
                        </div>
                    </div>
                </div>
            </div>

            <hr>
            <CarGridComponent :cars='cars' v-on:refreshCars="refreshCarGrid" />

            <hr />
            <div class="row">
                <router-link :to="{name: 'app-cars-save'}" class="btn btn-primary">
                    New Car
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import CarGridComponent from "./CarGridComponent";

export default {
  name: "app-cars-list",
  components: {
    CarGridComponent: CarGridComponent
  },

  data() {
    return {
      cars: []
    };
  },

  created() {
    this.getCarsJson();
  },

  methods: {
    getCarsJson() {
      fetch("http://127.0.0.1:5000/py-vue/api/cars").then(res =>
        res.json().then(res => {
          this.cars = res.cars;
        })
      );
    },

    refreshCarGrid() {
      this.getCarsJson();
    },

    showMessage() {}
  }
};
</script>

<style>

</style>
