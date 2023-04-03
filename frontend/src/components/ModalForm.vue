


<template>
    <div>
        <div @click="$emit('hideModal')" class="absolute bg-gray-900/60 z-[500] w-full h-full top-0">
        </div>
        <div
            class="fixed  z-[1000] rounded-md shadow-xl bg-slate-800 w-[550px] h-max inset-x-1/2 translate-x-[-50%] top-40">
            <UniversalButton @click="$emit('hideModal')" class="absolute right-0 p-1 ml-auto ">
                <IconsClose />
            </UniversalButton>
            <div class="w-full py-3 text-center bg-gray-400 rounded-t-md">
                <label class="text-[24px] text-gray-900 font-semibold ">Describe your regex</label>

            </div>
            <form class="flex flex-col p-3 space-y-3" @submit.prevent="submitForm">
                <UniversalInput @update:value="newValue => name = newValue" placeholder="Regex name..."
                    class="py-2 px-3 text-[16px]"></UniversalInput>
                <label class="text-center text-gray-300">It's a good idea to name your regex properly so you can easily find
                    it</label>
                <UniversalInput :placeholder="'Set your tags...'" @update:value="newValue => tags = newValue" />
                <label class="text-center text-gray-300">Use ', ' as a delimeter, for example: linux, windows,
                    python, tooling</label>

                <UniversalButton class="px-3 py-1 ml-auto">Add</UniversalButton>

            </form>
        </div>
    </div>
</template>

<script setup>
import UniversalButton from './UI/UniversalButton.vue';
import UniversalInput from './UI/UniversalInput.vue';
import { ref } from 'vue';
import IconsClose from './icons/IconsClose.vue';
const emit = defineEmits(['submitForm', 'hideModal'])
const name = ref('')
const tags = ref('')
const submitForm = () => {
    tags.value = tags.value.split(', ')
    emit('submitForm', { name: name.value, tags: tags.value })
}

</script>