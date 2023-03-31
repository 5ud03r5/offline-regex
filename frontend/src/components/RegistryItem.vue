<template>
    <div class="flex relative flex-col w-1/3 px-4 py-2 min-h-[150px] m-2 space-y-2 rounded-md shadow-xl bg-slate-600">
        <div class="flex items-center">
            <label class="text-[25px] font-bold text-gray-300">{{ name }}</label>
            <div
                class="px-2 py-1 ml-auto font-bold text-gray-200 transition-all rounded-md hover:bg-gray-800 hover:text-gray-300 bg-slate-900 hover:cursor-pointer">
                Try it</div>
        </div>

        <span class="p-4 italic text-gray-400 rounded-md bg-slate-700">{{ regex }}</span>
        <div class="absolute flex space-x-2 right-2 bottom-1">
            <UniversalTag v-for="tag in tags" :key="tag.id" :tag="tag.name" class="ml-auto"></UniversalTag>
        </div>

    </div>
</template>

<script setup>
import UniversalTag from './UI/UniversalTag.vue';
const props = defineProps({
    created: String,
    name: String,
    regex: String,
    tags: Array
})

</script>
<style scoped>
.tryit:hover {
    box-shadow: 0 1px 10px 0 rgb(255, 57, 255), 0 1px 5px 0 rgb(0, 108, 108);
    color: rgb(255, 193, 255)
}
</style>