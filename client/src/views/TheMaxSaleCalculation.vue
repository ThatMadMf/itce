<template>
  <the-table
    endpoint="http://localhost:8000/calculate"
    :args="{'max-sale': true}"
  />
</template>

<script>
import TheTable from "@/components/TheTable";
export default {
  name: 'TheMaxSaleCalculation',
  components: {TheTable},
};
</script>

<style scoped>

</style>
