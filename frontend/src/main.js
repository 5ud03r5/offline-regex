import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import "./assets/index.css";
import RegexRegistry from "./components/pages/RegexRegistry.vue";
import RegexTester from "./components/pages/RegexTester.vue";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: RegexTester },
    { path: "/registry", component: RegexRegistry },
  ],
});

const app = createApp(App);
app.use(router);
app.mount("#app");
