<template>
    <input :placeholder="placeholder" :value="value" autocomplete="off" autocorrect="off"
        @input="$emit('update:value', $event.target.value)"
        class="bg-gray-900 text-gray-100 placeholder:text-gray-300 rounded-md placeholder:italic transition-all input outline-1 outline-purple-900 focus:bg-gray-800 px-2 py-4 m-2 text-[20px]" />
</template>

<script setup>

const props = defineProps({
    value: String,
    placeholder: String,
})
const emit = defineEmits(['update:value'])

</script>

<style scoped>
.input {
    box-shadow: 0 1px 5px 0 rgba(85, 255, 255, 0.162), 0 1px 20px 0 rgba(217, 0, 255, 0.101)
}
</style>