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

import {TABLE_COLUMNS as columns} from "@/components/table";
import {ApiService} from "@/utils/axios";

export default {
  name: "TheTable",
  computed: {
    source() {
      return this.data;
    }
  },
  props: {
    endpoint: String,
    args: Object,
  },
  data() {
    return {
      data: [],
      columns,
    }
  },
  mounted() {
    ApiService.get(this.endpoint, {params: this.args})
      .then((result) => {
          let arr = [];
          for(const [key, value] of Object.entries((result.data))) {
            arr.push({key: key, value: value})
          }
          this.data = arr;
      })
  }
}
</script>

<style scoped>

</style>