<template lang="pug">
  section.container.grid-960
    .columns
      .column.col-2
      .column.col-8.col-md-12
        header.text-center
          h2 Create note
        create-note
        header.text-center
          h2 List of notes
        note-list
      .column.col-2
</template>

<script>
import CreateNote from './CreateNote'
import NoteList from './NoteList'

export default {
  name: 'Home',
  components: {
    NoteList,
    CreateNote
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
