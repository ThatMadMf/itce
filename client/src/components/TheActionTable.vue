<template>
  <a-table
      :columns="columns"
      :data-source="source"
      size="middle"
      :pagination="{
        defaultPageSize: 20,
      }"
  >
  </a-table>
</template>

<script>
import {ACTION_TABLE_COLUMNS as columns} from "@/components/actionTable";
import {ApiService} from "@/utils/axios";

export default {
  name: 'TheActionTable',
  computed: {
    source() {
      console.log(this.data);
      return this.data;
    },
  },
  data() {
    return {
      data: [],
      columns,
    };
  },
  mounted() {
    ApiService.get('http://localhost:8000/table')
        .then((result) => {
          let data = result.data.map((e) => {
            e.vat = e.vat ? '1' : '';
            e.revsTax = e.revs_tax ? '1' : '';
            e.revenueTax = e.revenue_tax ? '1' : '';
            e.money = e.money ? '1' : '';

            const sum = e.money_change + e.vat_value + e.tax_value;
            if(sum > 0) {
              e.additions = sum;
            } else {
              e.subtractions = sum;
            }
            return e;
          })
          this.data = data;
        })
  }
}
</script>

<style scoped>

</style>