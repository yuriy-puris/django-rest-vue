import Vue from 'vue'
import Vuex from 'vuex'
import { NOTES } from '../api/notes'

import {
  ADD_NOTE,
  REMOVE_NOTE,
  SET_NOTES
} from './mutations'

Vue.use(Vuex)

const state = {
  notes: []
}

const getters = {
  notes: state => state.notes
}

const mutations = {
  [ADD_NOTE] (state, note) {
    state.notes = [note, ...state.notes]
  },
  [REMOVE_NOTE] (state, { id }) {
    state.notes = state.notes.filter(note => {
      return note.id !== id
    })
  },
  [SET_NOTES] (state, { notes }) {
    state.notes = notes
  }
}

const actions = {
  createNote ({ commit }, noteData) {
    NOTES.create(noteData).then(note => {
      commit(ADD_NOTE, note)
    })
  },
  deleteNote ({ commit }, note) {
    NOTES.delete(note).then(response => {
      commit(REMOVE_NOTE, note)
    })
  },
  getNotes ({ commit }) {
    NOTES.read().then(notes => {
      commit(SET_NOTES, { notes })
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
