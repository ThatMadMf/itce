import Vue from 'vue';
import VueRouter, {RouteConfig} from 'vue-router';
import Home from '../../client/src/views/Home.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
    {
        path: '/calculate',
        name: 'calculate',
        component: () => import('../views/TheOrdinaryCalculation.vue'),
    },
    {
        path: '/calculate-max-sale',
        name: 'calculate-max-sale',
        component: () => import('../views/TheMaxSaleCalculation.vue'),
    },
    {
        path: '/calculate-zero-profitability',
        name: 'calculate-zero-profitability',
        component: () => import('../views/TheZeroProfitability.vue'),
    },
    {
      path: '/table',
      name: 'table',
      component: () => import('../views/TheTableView.vue'),
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
