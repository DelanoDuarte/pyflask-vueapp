<template>
    <div class="app-car-evaluation">
        <h2>Car Evaluation </h2>
        <hr>

        <div class="row">
          
              <div class="col-md-4">
                    <div class="card">
                        <img class="card-img-top" src="https://i.pinimg.com/736x/8f/61/67/8f61677067d8874a140738d7ad2ea56a--vehicle-accessories-car-lights.jpg">
                        <div class="card-block">
                            <h4 class="card-title">{{car.brand.name}} - {{car.model}}</h4>
                            <hr>
                            <div class="meta">
                                
                            </div>
                            <div class="card-text">

                                <div class="row">
                                  <div class="form-group col-sm-6">
                                    <label for="year"> <b>Year </b> </label>
                                    <input type="text" class="form-control" id="year" v-model="car.year" disabled>
                                  </div>

                                  <div class="form-group col-sm-6">
                                    <label for="year"><b>Price </b></label>
                                    <input type="text" class="form-control" id="year" v-model="car.price" disabled>
                                  </div>
                                </div>

                            </div>
                        </div>
                        <div class="card-footer">
                            <!-- <span class="float-right">Joined in 2013</span>
                            <span><i class=""></i>75 Friends</span> -->
                        </div>
                    </div>
              </div>
              
              <div class="col-md-8">
                <CarEvaluationRatingComponent :evaluation = 'evaluation'/>
              </div>
          
        </div>

        <hr>

        <div class="row">
            <div class="col-md-12 text-center">
                <button type="button" v-on:click="evaluateCar" class="btn btn-primary">Evaluate This Car </button>
                <router-link :to="{name:'app-cars-list'}" class="btn btn-warning">Cancel</router-link>
            </div>
        </div>
        
    </div>
</template>

<script>
import CarEvaluationRatingComponent from "./CarEvaluationRatingComponent";

export default {
  name: "app-car-evaluation",
  components: {
    CarEvaluationRatingComponent: CarEvaluationRatingComponent
  },

  data() {
    return {
      car: "",
      evaluation: {
        motor: 0,
        gas: 0,
        apparence: 0,
        support: 0
      }
    };
  },

  created() {
    this.loadCarById();
  },

  methods: {
    loadCarById() {
      fetch(
        `http://127.0.0.1:5000/py-vue/api/cars/${this.$route.params.id}`
      ).then(res =>
        res.json().then(res => {
          this.car = res;
        })
      );
    },

    evaluateCar() {
      let data = JSON.stringify({ "car-evaluation": this.evaluation });
      console.log(data);
      fetch(
        `http://127.0.0.1:5000/py-vue/api/car-evaluation/${this.$route.params
          .id}`,
        {
          headers: { "Content-Type": "application/json" },
          method: "POST",
          body: data
        }
      ).then(res => {
        res.json().then(res => {
          console.log(res.data);
          this.$router.push({ name: "app-cars-list" });
        });
      });
    }
  }
};
</script>

<style scoped>
.left-text {
  text-align: right;
}
.card {
  font-size: 1em;
  overflow: hidden;
  padding: 0;
  border: none;
  border-radius: 0.28571429rem;
  box-shadow: 0 1px 3px 0 #d4d4d5, 0 0 0 1px #d4d4d5;
}

.card-block {
  font-size: 1em;
  position: relative;
  margin: 0;
  padding: 1em;
  border: none;
  border-top: 1px solid rgba(34, 36, 38, 0.1);
  box-shadow: none;
}

.card-img-top {
  display: block;
  width: 100%;
  height: auto;
}

.card-title {
  font-size: 1.28571429em;
  font-weight: 700;
  line-height: 1.2857em;
}

.card-text {
  clear: both;
  margin-top: 0.5em;
  color: rgba(0, 0, 0, 0.68);
}

.card-footer {
  font-size: 1em;
  position: static;
  top: 0;
  left: 0;
  max-width: 100%;
  padding: 0.75em 1em;
  color: rgba(0, 0, 0, 0.4);
  border-top: 1px solid rgba(0, 0, 0, 0.05) !important;
  background: #fff;
}

.card-inverse .btn {
  border: 1px solid rgba(0, 0, 0, 0.05);
}
</style>
