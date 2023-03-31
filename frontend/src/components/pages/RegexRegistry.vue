<template>
    <div class="">
        <div class="flex justify-center">
            <UniversalInput class="py-2 text-center text-[19px] bg-gray-700" :placeholder="'Search in registry...'">
            </UniversalInput>
        </div>
        <div v-if="tags" class="flex flex-wrap justify-center">
            <UniversalTag v-for="tag in tags" :key="tag.id" :tag="tag.name"></UniversalTag>
        </div>
        <div class="flex flex-wrap justify-center mt-10">

            <RegistryItem v-if="data" v-for="item in data" :key="item.id" :name="item.name" :created="item.created"
                :tags="item.tags" :regex="item.regex"></RegistryItem>
        </div>
    </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue';
import RegistryItem from '../RegistryItem.vue';
import UniversalInput from '../UI/UniversalInput.vue';
import UniversalTag from '../UI/UniversalTag.vue';
const data = ref(null)
const tags = ref(null)
const getData = async () => {
    const response = await fetch(import.meta.env.VITE_API + 'regex/')
    if (!response.ok) {
        throw Error('Cannot pull repository from API')
    }
    data.value = await response.json()
}
const getTags = async () => {
    const response = await fetch(import.meta.env.VITE_API + 'tags/')
    if (!response.ok) {
        throw Error('Cannot pull tags from API')
    }
    tags.value = await response.json()

}
watchEffect(getData)
watchEffect(getTags)
</script>
