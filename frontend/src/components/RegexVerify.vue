<template>
    <div class="bg-slate-900  box w-[500px] rounded-md ml-3 p-4 mt-2  h-[710px]">
        <h2 class="pb-3 text-gray-300 text-[20px]">MATCH INFORMATION</h2>
        <hr>
        <div v-if="match" class="mt-6 text-gray-300">
            <label>Full match:</label>
            <div class="p-2 my-1 rounded-sm bg-slate-800">{{ match[0] }}</div>
            <label v-if="match.groups">Groups:</label>
            <div v-if="match.groups" class="flex flex-col flex-wrap p-2 my-1 rounded-sm bg-slate-800">
                <div v-for="group, gname, index in match.groups" class="flex m-1 space-x-1">
                    <div class="px-2 text-gray-700 bg-purple-400 rounded-sm">{{ gname }}</div>
                    <div>:</div>
                    <div class="px-2 text-gray-700 bg-gray-200 rounded-sm">{{ group }}</div>
                </div>
            </div>

        </div>
    </div>
</template>
<script setup>
const props = defineProps({ match: Array })

</script>

<style scoped>
.box {
    box-shadow: 0 1px 5px 0 rgba(85, 255, 255, 0.162), 0 1px 20px 0 rgba(217, 0, 255, 0.101)
}
</style>