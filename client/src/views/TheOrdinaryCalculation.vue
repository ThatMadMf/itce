<template>
  <the-table
    endpoint="http://localhost:8000/calculate"
  />
</template>

<script>
import TheTable from "@/components/TheTable";
export default {
  name: 'TheOrdinaryCalculation',
  components: {
    TheTable,
  },
};
</script>

<style scoped>

</style>
