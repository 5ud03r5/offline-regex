<template>
    <nav>
        <div class="bg-gray-900 fixed top-0 w-full nav z-[2000]">
            <div class="container text-[20px] mx-auto flex justify-end space-x-10 text-gray-100">
                <RouterLink to="/registry" class="p-5 hover:text-purple-600 transition-all">Registry</RouterLink>
                <RouterLink to="/" class="p-5 hover:text-purple-600 transition-all">Tester</RouterLink>
            </div>
        </div>
    </nav>
</template>
<style scoped>
.nav {
    box-shadow: 0 1px 10px 0 rgba(85, 255, 255, 0.474), 0 1px 15px 0 rgba(217, 0, 255, 0.6)
}

.router-link-active {
    color: rgb(165, 98, 228)
}
</style>