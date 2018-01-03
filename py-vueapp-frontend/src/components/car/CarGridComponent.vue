<template>
    <div class="app-cars-grid-component">
        <table class="table">
            <thead class="thead-dark">
                <tr>
                    <th>Car Model</th>
                    <th>Brand</th>
                    <th>Car Price</th>
                    <th>Car Year</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="car in cars" v-bind:key="car._id">
                    <td> {{car.model}}</td>
                    <td> {{car.brand.name}}</td>
                    <td> $ {{car.price}}</td>
                    <td> {{car.year}}</td>
                    <td>
                        <div class="text-center">
                            <router-link :to="{name:'app-cars-edit', params:{'id':car._id}}" class="btn btn-success">Edit</router-link>
                            <router-link :to="{name:'app-cars-evaluation', params:{'id':car._id}}" class="btn btn-primary"  v-if="!car.evaluated">Evaluate This Car</router-link>                            
                            <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#exampleModal" @click="showModal(car)">Delete </button>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Confirm Deletion</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        Delete this {{car.model}} ?
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
                        <button type="button" class="btn btn-danger" data-dismiss="modal" @click="deleteCar">Delete</button>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
export default {
  name: "app-cars-grid-component",
  props: ["cars"],

  data() {
    return {
      car: ""
    };
  },

  methods: {
    showModal(car) {
      this.car = car;
    },

    deleteCar() {
      fetch(`http://127.0.0.1:5000/py-vue/api/cars/${this.car._id}`, {
        method: "DELETE"
      }).then(res =>
        res.json().then(res => {
          console.log(res);
          this.$emit("refreshCars", () => {
            console.log("event emited for parent");
          });
        })
      );
    }
  }
};
</script>

<style>

</style>
