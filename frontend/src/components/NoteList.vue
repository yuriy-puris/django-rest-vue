<template lang="pug">
  #note
    .card(v-for="note in notes")
        .card-header
          button.btn.btn-clear.float-right(@click="deleteNote(note)") Удалить
          .card-title {{ note.title }}
          .card-subtitle {{ note.created_at }}
        .card-body {{ note.body }}
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NoteList',
  computed: mapGetters(['notes']),
  data() {
    return {
      title: '',
      body: '',
      created_at: ''
    }
  },
  methods: {
    deleteNote (note) {
      this.$store.dispatch('deleteNote', note)
    }
  },
  beforeMount() {
    this.$store.dispatch('getNotes')
  }
}
</script>
