<template>
    <div class="app-car-evaluation">
        <h2>Car Evaluation </h2>
        <hr>
        <div class="left-text">
            <h5>Evaluating {{car.model}} of the year {{car.year}}</h5>
        </div>
        <hr>
        <CarEvaluationRatingComponent />
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
      car: ""
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
    }
  }
};
</script>

<style scoped>
    .left-text{
        text-align: right
    }


</style>
