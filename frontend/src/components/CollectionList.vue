<template>
  <div>
<!--    <h1>Collections</h1>-->
    <ul>
      <li v-for="collection in collections" :key="collection.id">
        {{ collection.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      collections: []
    };
  },
  created() {
    this.fetchCollections();
  },
  methods: {
    fetchCollections() {
      axios.get('/api/collections/')
        .then(response => {
          this.collections = response.data;
        })
        .catch(error => {
          console.error("There was an error fetching the collections: ", error);
        });
    }
  }
};
</script>