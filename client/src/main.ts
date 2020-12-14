import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'ant-design-vue/dist/antd.css';

import axios from 'axios';
import VuexAxios from 'vue-axios';
import Antd from 'ant-design-vue';


Vue.use(VuexAxios, axios);
Vue.use(Antd);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
