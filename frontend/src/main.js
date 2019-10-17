import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import auth from "./auth/index";
import VueResource from "vue-resource";
Vue.use(VueResource);

// Check the user's auth status when the app starts
auth.checkAuth();

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
