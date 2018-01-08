<template>
    <div class="app-car-evaluation-rating">

      <div class="card card-padding">
        <div class="card-body ">

        <div class="row animated bounceInLeft">
            <img src="https://www.colourbox.com/preview/19951874-car-engine-flat-icon.jpg" width="96px" height="96px"/>
            <label> <h4> Motor </h4> </label>
            <star-rating :increment='0.5' rating='evaluation.motor' v-model="evaluation.motor"> </star-rating>
        </div>
        <hr>
        <div class="row animated bounceInLeft">
            <img src="http://www.pvhc.net/img220/rhyvxyzlqtlteegyxywx.jpg" width="96px" height="96px"/>
            <label> <h4> Gas Consume </h4> </label>
            <star-rating :increment='0.5' rating='evaluation.gas' v-model="evaluation.gas"> </star-rating>
        </div>

        <hr>
        <div class="row animated bounceInLeft">
            <img src="https://image.flaticon.com/icons/svg/215/215841.svg" width="96px" height="96px"/>
            <label> <h4> Apperance </h4> </label>
            <star-rating :increment='0.5' rating='evaluation.apparence' v-model="evaluation.apparence"> </star-rating>
        </div>

        <hr>
        <div class="row animated bounceInLeft">
            <img src="https://teal.net/wp-content/uploads/2016/08/Flat-Icons-18-27.png" width="96px" height="96px"/>
            <label> <h4> Brand Support </h4> </label>
            <star-rating :increment='0.5' rating='evaluation.support' v-model="evaluation.support"> </star-rating>
        </div>

        </div>
      </div>

    </div>
</template>

<script>
export default {
  name: "app-car-evaluation-rating",

  props: ["evaluation"],

  data() {
    return {};
  },

  methods: {}
};
</script>

<style scoped>
.card-padding {
  padding: 15px;
}
</style>
