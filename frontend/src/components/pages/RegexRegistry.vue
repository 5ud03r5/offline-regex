<template>
    <div class="">
        <div class="flex justify-center">
            <UniversalInput @update:value="newValue => search = newValue" class="py-2 text-center text-[19px] bg-gray-700"
                :placeholder="'Search in registry...'">
            </UniversalInput>
        </div>
        <div v-if="tags" class="flex flex-wrap justify-center">
            <UniversalTag v-for="tag in tags" v-include="{ filter: filter, tag: tag }" :key="tag.id" :tag="tag.name"
                @click="setFilter(tag)">
            </UniversalTag>
        </div>
        <div class="flex flex-wrap justify-center mt-10">

            <RegistryItem v-if="filteredRegex" v-for="item in filteredRegex" :key="item.id" :name="item.name"
                :created="item.created" :tags="item.tags" :regex="item.regex" :id="item.id" @getRegex="getRegex">
            </RegistryItem>
        </div>
    </div>
</template>

<script setup>
import { ref, watchEffect, watch } from 'vue';
import RegistryItem from '../RegistryItem.vue';
import UniversalInput from '../UI/UniversalInput.vue';
import UniversalTag from '../UI/UniversalTag.vue';
import { storeToRefs } from 'pinia';
import { useRegexStore } from '../../store/store'
import { useRouter, useRoute } from 'vue-router'
const data = ref(null)
const tags = ref(null)
const regexApi = ref('regex/')
const filter = ref([])
const search = ref('')
const filteredRegex = ref(null)
const store = useRegexStore()
const { dataRegex } = storeToRefs(store)
const router = useRouter()
const getRegex = async (id) => {
    const response = await fetch(import.meta.env.VITE_API + 'regex/' + id)
    if (!response.ok) {
        throw Error('Cannot pull repository from API')
    }
    dataRegex.value = await response.json()
    router.push('/')

}

const getData = async (filter) => {
    if (filter.value.length > 0) {
        regexApi.value = 'regex/?tags=' + filter.value.map(tag => { return tag.id })
    } else {
        regexApi.value = 'regex/'
    }
    const response = await fetch(import.meta.env.VITE_API + regexApi.value)
    if (!response.ok) {
        throw Error('Cannot pull repository from API')
    }
    data.value = await response.json()
    filteredRegex.value = data.value
}
const getTags = async () => {
    const response = await fetch(import.meta.env.VITE_API + 'tags/')
    if (!response.ok) {
        throw Error('Cannot pull tags from API')
    }
    tags.value = await response.json()
}
const setFilter = (item) => {
    if (filter.value.includes(item)) {
        const index = filter.value.indexOf(item)
        filter.value.splice(index, 1)
    } else {
        filter.value.push(item)
    }

}

watch(search, () => {
    if (search.value.length > 0) {
        filteredRegex.value = data.value.filter(item => item.name.toLowerCase().includes(search.value.toLocaleLowerCase()))
    } else {
        filteredRegex.value = data.value
    }

})

watchEffect(() => getData(filter))
watchEffect(getTags)
</script>
