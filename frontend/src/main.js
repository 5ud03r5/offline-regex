import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import "./assets/index.css";
import RegexRegistry from "./components/pages/RegexRegistry.vue";
import RegexTester from "./components/pages/RegexTester.vue";
import { createRouter, createWebHistory } from "vue-router";
import { createPinia } from "pinia";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: RegexTester },
    { path: "/registry", component: RegexRegistry },
  ],
});
const pinia = createPinia();

const app = createApp(App);
app.use(router);
app.use(pinia);
app.directive("include", (el, binding) => {
  if (binding.value.filter.includes(binding.value.tag)) {
    el.style.color = "purple";
  } else {
    el.style.color = "white";
  }
});
app.mount("#app");
