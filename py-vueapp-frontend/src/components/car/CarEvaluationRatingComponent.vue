<template>
    <div class="app-car-evaluation-rating">
        <div class="row">
            <img src="https://www.colourbox.com/preview/19951874-car-engine-flat-icon.jpg" width="128px" height="128px"/>
            <label> <h4> Motor </h4> </label>
            <star-rating :increment='0.5' rating='evaluation.motor' v-model="evaluation.motor"> </star-rating>
        </div>
        <br />
        <div class="row">
            <img src="http://www.pvhc.net/img220/rhyvxyzlqtlteegyxywx.jpg" width="128px" height="128px"/>
            <label> <h4> Gas Consume </h4> </label>
            <star-rating :increment='0.5' rating='evaluation.gas' v-model="evaluation.gas"> </star-rating>
        </div>

        <br />
        <div class="row">
            <img src="https://image.flaticon.com/icons/svg/215/215841.svg" width="128px" height="128px"/>
            <label> <h4> Apperance </h4> </label>
            <star-rating :increment='0.5' rating='evaluation.apparence' v-model="evaluation.apparence"> </star-rating>
        </div>

        <br />
        <div class="row">
            <img src="https://teal.net/wp-content/uploads/2016/08/Flat-Icons-18-27.png" width="128px" height="128px"/>
            <label> <h4> Brand Support </h4> </label>
            <star-rating :increment='0.5' rating='evaluation.support' v-model="evaluation.support"> </star-rating>
        </div>

        <hr>

         <div class="row">
            <div class="col-md-12 text-center">
                <button type="button" v-on:click="evaluateCar" class="btn btn-primary">Evaluate This Car </button>
                <router-link :to="{name:'app-brandlist'}" class="btn btn-warning">Cancel</router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: "app-car-evaluation-rating",

  data() {
    return {
      evaluation: {
        motor: 0,
        gas: 0,
        apparence: 0,
        support: 0
      }
    };
  },

  methods: {
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

</style>
