<template>
    <div class="app-message">

        <div v-if="show">
            <div v-bind:class="{alert: alert-type}" role="alert">
                {{message}}
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'app-message',
    props: ['type', 'message', 'show'],

    data() {
        return {

        }
    }
}
</script>

<style>

</style>
