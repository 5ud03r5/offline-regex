<template>
    <button
        class="bg-gray-900 flex items-center text-[20px] text-gray-200 rounded-md m-2 hover:bg-slate-800 outline-none hover:outline hover:outline-3 hover:outline-purple-300">
        <slot></slot>
    </button>
</template>

<script setup>


</script>

<style scoped>
button {
    box-shadow: 0 1px 5px 0 rgba(85, 255, 255, 0.162), 0 1px 20px 0 rgba(217, 0, 255, 0.101)
}
</style>