<template>
    <div class="NameList">
        <table class="table">
            <thead class="thead-dark">
                <tr>
                    <th>Name</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in items" v-bind:key="item">
                    <td>{{item.name}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'NameList',

    props: ['items'],
    data() {
        return {
        }
    }
}
</script>

<style>

</style>
