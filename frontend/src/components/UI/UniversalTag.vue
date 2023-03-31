<template>
    <div class="items-center m-1 text-gray-100 transition-all rounded-md w-max hover:cursor-pointer hover:text-purple-500">
        <span>#</span>{{ tag
        }}
    </div>
</template>

<script setup>
const props = defineProps({ tag: String })


</script>