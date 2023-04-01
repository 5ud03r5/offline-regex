import { defineStore } from "pinia";
import { ref, watch } from "vue";

export const useRegexStore = defineStore("regex", () => {
  const dataRegex = ref("");
  const regex = ref("");
  const text = ref("");
  const match = ref(null);

  watch(dataRegex, () => {
    regex.value = dataRegex.value.regex;
    text.value = dataRegex.value.text;
  });
  watch([text, regex], () => {
    if (regex.value.length > 0) {
      try {
        match.value = text.value.match(new RegExp(regex.value));
      } catch (e) {
        match.value = null;
      }
    } else {
      match.value = null;
    }
  });

  return {
    dataRegex,
    regex,
    text,
    match,
  };
});
