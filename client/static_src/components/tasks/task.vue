<template>
<card
  :index="index"
  @modal="$emit('modal')"
  @delete="deleteTask(task)">
  <template slot="card-body">
    <div class="card-title h5 font-weight-bold mb-4">
      {{ task.name }}
    </div>
    <div v-if="task.hourly_rate" class="card-subtitle h6">
      <icon :icon="['fas', 'hand-holding-usd']" class="mr-1 text-muted"/>
      ${{ task.hourly_rate }}/hr
    </div>
  </template>
</card>
</template>


<script>
import {mapActions} from 'vuex';

import Card from '../cards/card.vue';


export default {
  components: {
    Card,
  },
  props: {
    task: {
      type: Object,
      default: () => {
        return {
          id: null,
        }
      },
    },
    index: {
      type: Number,
      default: null,
    },
  },
  methods: {
    ...mapActions({
      deleteTask: 'tasks/deleteTask',
    }),
  },
};
</script>
