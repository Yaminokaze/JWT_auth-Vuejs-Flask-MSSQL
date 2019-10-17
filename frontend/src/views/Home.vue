<template>
  <div>
    <h1>Welcome</h1>
    <div class="alert alert-danger" v-if="error">
      <p>{{ error }}</p>
    </div>
    <h2>Username: {{ username }}</h2>
    <h2>Email: {{ email }}</h2>
    <h2>Country: {{ country }}</h2>
    <h2>Birthday: {{ birthdayDate }}</h2>
    <button class="btn btn-danger" @click="submit()">logout</button>
  </div>
</template>

<script>
export default {
  data() {
    return {

        username: "a",
        email: "",
        country: "",
        birthdayDate: "",
        error:""
    };
  },
  methods: {
},
  
mounted: function() {
      console.log("test");  // eslint-disable-line
      this.$http.get("http://localhost:5000/home").then(
        response => {
          this.username = response.username;
          this.email = response.email;
          this.country = response.country;
          this.birthdayDate = response.birthdayDate
        },
      error => {
        this.error = error.message;
      }
      );
    }
};
</script>
