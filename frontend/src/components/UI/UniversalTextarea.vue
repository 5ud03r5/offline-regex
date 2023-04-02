<template>
    <span id="cnt" contenteditable="true" :placeholder="placeholder" @input="updateText" autocorrect="off"
        autocomplete="off"
        class="bg-gray-900 min-h-[633px]  max-h-[633px] overflow-y-scroll break-all placeholder:break-all text-[20px] input text-gray-100 rounded-md transition-all outline-3 outline-purple-900 focus:bg-slate-800 resize-none px-2 py-4 m-2 ">

    </span>
</template>
<script setup>
import { ref, watchEffect, onMounted } from 'vue';
const emits = defineEmits(['update:text'])
const props = defineProps({
    value: String
})
onMounted(() => document.getElementById('cnt').innerHTML = props.value)

const placeholder = ref('Here goes your raw text...')
const updateText = (e) => {
    emits('update:text', e.target.innerHTML)
    if (e.target.innerHTML.length > 0) {
        placeholder.value = ''
    } else {
        placeholder.value = 'Here goes your raw text...'
    }
}
watchEffect(() => {

    if (props.value.length > 0) {
        placeholder.value = ''
    } else {
        placeholder.value = 'Here goes your raw text...'
    }
})

</script>
<style scoped>
.input {
    box-shadow: 0 1px 5px 0 rgba(85, 255, 255, 0.162), 0 1px 20px 0 rgba(217, 0, 255, 0.101)
}

.input::before {
    content: attr(placeholder);
    position: absolute;
    font-style: italic;
    color: rgb(209 213 219);
}
</style>