<template>
  <div class="d-flex align-items-center justify-content-center">
    <router-view />
    <button class="btn btn-danger" @click="logout()" v-if="!user" >logout</button>
  </div>
</template>



<script>
import auth from './auth'

export default {
  data() {
    return {
      user: auth.user
    }
  },

  methods: {

    logout() {
      auth.logout()
    }
  }
}
</script>