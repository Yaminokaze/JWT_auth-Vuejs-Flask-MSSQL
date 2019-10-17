<template>
  <div>
    <h1>Welcome</h1>
      <div class="alert alert-danger" v-if="error">
      <p>{{ error }}</p>
      </div>
    <h2>Username: {{credentials.username}}</h2>
    <h2>Email: {{credentials.email}}</h2>
    <h2>Country: {{credentials.country}}</h2>
    <h2>Birthday: {{credentials.birthdayDate}}</h2>
  </div>
</template>

<script>
export default {
  data() {
    return {
      credentials: {
        username: "",
        email: "",
        country: "",
        birthdayDate: ""
      },
      error:""
    };
  },
  methods: {

  
created: function () {
      this.$http.get("http://localhost:5000/home").then(
        response => {
          this.credentials = response;
        },
      error => {
        this.error = error.message;
      }
      );
    }
}};
</script>
