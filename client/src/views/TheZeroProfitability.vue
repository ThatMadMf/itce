<template>
  <the-table
    endpoint="http://localhost:8000/calculate"
    :args="{'zero-profitability': true}"
  />
</template>

<script>
import TheTable from "@/components/TheTable";
export default {
  name: 'TheZeroProfitability',
  components: {TheTable},
};
</script>

<style scoped>

</style>
