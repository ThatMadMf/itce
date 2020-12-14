<template>
  <div>
    <a-tabs default-active-key="1" @change="callback">
      <a-tab-pane key="1" tab="Посчитать">
        <the-ordinary-calculation/>
      </a-tab-pane>
      <a-tab-pane key="2" tab="Максимальная точка чены реализации" force-render>
        <the-max-sale-calculation/>
      </a-tab-pane>
      <a-tab-pane key="3" tab="Точка нулевой рентабельности">
        <the-zero-profitability/>
      </a-tab-pane>
    </a-tabs>
  </div>
</template>

<script>
import TheOrdinaryCalculation from '@/views/TheOrdinaryCalculation.vue';
import TheMaxSaleCalculation from '@/views/TheMaxSaleCalculation.vue';
import TheZeroProfitability from '@/views/TheZeroProfitability.vue';

export default {
  name: 'Switcher',
  components: {
    TheZeroProfitability,
    TheMaxSaleCalculation,
    TheOrdinaryCalculation,
  },
};

</script>

<style scoped>

</style>
