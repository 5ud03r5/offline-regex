<template>
    <div class="flex px-5">
        <div class="flex flex-col w-full">
            <div class="flex">
                <UniversalInput class="w-5/6" :value="regex" @update:value="newValue => regex = newValue"
                    :placeholder="'Here goes your regex...'">
                </UniversalInput>
                <UniversalButton class="px-4 " @click="modalOpened = true">
                    <IconsSave height="32" width="32"></IconsSave> <span class="px-3 text-[25px]">Save</span>
                </UniversalButton>
            </div>
            <UniversalTextarea @update:text="newValue => text = newValue" :value="text"></UniversalTextarea>
        </div>
        <div>
            <RegexVerify :match="match"></RegexVerify>
        </div>
        <Teleport to="body" v-if="modalOpened">
            <ModalForm @submitForm="submitForm" @hideModal="modalOpened = false"></ModalForm>
        </Teleport>
    </div>
</template>
<script setup>
import UniversalInput from '../UI/UniversalInput.vue';
import UniversalTextarea from '../UI/UniversalTextarea.vue'
import RegexVerify from '../RegexVerify.vue'
import { ref, watch } from 'vue';
import UniversalButton from '../UI/UniversalButton.vue';
import IconsSave from '../icons/IconsSave.vue';
import ModalForm from '../ModalForm.vue';
import { storeToRefs } from 'pinia';
import { useRegexStore } from '../../store/store';
const store = useRegexStore()
const { regex, text, match } = storeToRefs(store)
const modalOpened = ref(false)


const submitForm = async (value) => {
    if (regex.value.length > 0 && value['name'].length > 0) {
        await fetch(import.meta.env.VITE_API + 'regex/',
            {
                method: 'POST',
                body: JSON.stringify({
                    name: value['name'], regex: regex.value, text: text.value, tags: value['tags']
                }),
                headers: { 'Content-Type': 'application/json' }
            })
    }

    modalOpened.value = !modalOpened.value
}

</script>
