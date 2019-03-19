import { HTTP } from './common'

export const NOTES = {
  create(config) {
    return HTTP.post('/notes/', config).then(response => {
      return response.data
    })
  },
  read() {
    return HTTP.get('/notes/').then(response => {
      return response.data
    })
  },
  delete(note) {
    return HTTP.delete(`/notes/${note.id}/`)
  }
}

