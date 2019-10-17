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
  </div>
</template>

<script>
export default {
  data() {
    return {

        username: "",
        email: "",
        country: "",
        birthdayDate: "",
        error:""
    };
  },
  methods: {
},
  
mounted: function() {
      this.$http.get("http://localhost:5000/home").then(
        response => {
          this.username = response.username;
          this.email = response.email;
          this.country = response.country;
          this.birthdayDate = response.birthdayDate
                console.log("test");  // eslint-disable-line

        },
      error => {
        this.error = error.message;
      }
      );
    }
};
</script>
