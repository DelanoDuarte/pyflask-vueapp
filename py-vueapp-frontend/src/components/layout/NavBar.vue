<template>
    <div class="custom-navbar">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="#">App</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
                <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                    <li class="nav-item active">
                        <router-link to="/" class="nav-link">
                            Home
                            <span class="sr-only">(current)</span>
                        </router-link>

                    </li>

                    <li class="nav-item">
                        <router-link :to="{name: 'app-brandlist'}" class="nav-link">
                            Brands
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link :to="{name: 'app-cars-list'}" class="nav-link">
                            Car
                        </router-link>
                    </li>
                    <li class="nav-item">
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    name: 'custom-navbar'

}
</script>

<style>

</style>
