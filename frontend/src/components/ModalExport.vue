


<template>
    <div>
        <div @click="$emit('hideModal')" class="absolute bg-gray-900/60 z-[500] w-full h-full top-0">
        </div>
        <div
            class="fixed  z-[1000] rounded-md shadow-xl bg-slate-800 w-[800px] h-max inset-x-1/2 translate-x-[-50%] top-40">
            <UniversalButton @click="$emit('hideModal')" class="absolute right-0 p-1 ml-auto ">
                <IconsClose />
            </UniversalButton>
            <div class="w-full py-3 text-center bg-gray-400 rounded-t-md">
                <label class="text-[24px] text-gray-900 font-semibold ">Export matches</label>
            </div>
            <div class="flex p-2 space-x-2 ">
                <div class="flex flex-col w-2/5 space-y-2 text-white">
                    <div @click="setFormat('Plain')" :class="format === 'Plain' ? 'bg-gray-500' : 'bg-gray-700'"
                        class="transition-all w-full p-2 text-[20px]  rounded-md hover:bg-gray-500 hover:cursor-pointer">
                        Text
                    </div>
                    <div @click="setFormat('JSON')" :class="format === 'JSON' ? 'bg-gray-500' : 'bg-gray-700'"
                        class="transition-all w-full p-2 text-[20px]  rounded-md hover:bg-gray-500 hover:cursor-pointer">
                        JSON</div>
                    <div @click="setFormat('CSV')" :class="format === 'CSV' ? 'bg-gray-500' : 'bg-gray-700'"
                        class="transition-all w-full p-2 text-[20px]  rounded-md hover:bg-gray-500 hover:cursor-pointer">
                        CSV</div>

                </div>
                <div class="w-3/5 p-2 text-white bg-gray-700 rounded-md max-h-[250px] min-h-[250px] overflow-auto"
                    id="text">
                    <div v-if="format === 'Plain'" v-for="group, gname, index in match.groups">
                        {{ index + 1 }} {{ group }} {{ gname }}
                    </div>
                    <div v-if="format === 'CSV'">
                        id,Group,Match
                        <div v-for="group, gname, index in match.groups">
                            {{ index + 1 }},{{ group }},{{ gname }}
                        </div>
                    </div>
                    <div v-if="format === 'JSON'">
                        [
                        <div class="flex flex-col" v-for="group, gname, index in match.groups">
                            <span class="ml-3">{</span>
                            <span class="ml-5">"id": {{ index + 1 }},</span>
                            <span class="ml-5">"group": "{{ group }}",</span>
                            <span class="ml-5">"match": "{{ gname }}"</span>
                            <span class="ml-3">},</span>
                        </div>
                        ]
                    </div>


                </div>
            </div>
            <UniversalButton class="p-2 ml-auto" @click="copyToClipboard">Copy to clipboard
                <IconsClipboard height="24" width="24" class="ml-2">
                </IconsClipboard>
            </UniversalButton>
        </div>
    </div>
</template>

<script setup>
import UniversalButton from './UI/UniversalButton.vue';
import IconsClipboard from './icons/IconsClipboard.vue'
import { ref } from 'vue';
import IconsClose from './icons/IconsClose.vue';
import { useRegexStore } from '../store/store';
import { storeToRefs } from 'pinia';
const store = useRegexStore()
const { match } = storeToRefs(store)
const format = ref('Plain')

const emit = defineEmits(['submitForm', 'hideModal'])
const copyToClipboard = () => {
    navigator.clipboard.writeText(document.getElementById('text').innerText)
}
const setFormat = (option) => {
    if (format.value === option) {
        format.value = ''
    } else {
        format.value = option
    }

}


</script>

<style scoped></style>