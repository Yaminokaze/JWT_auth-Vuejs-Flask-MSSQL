<template>
  <div>
    <h1>Welcome</h1>
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
      }
    };
  },
  methods: {

  
created: function () {
      this.$http.get("http://localhost:5000/home").then(
        function(response) {
          this.credentials = response;
        }/*,
        function(error) {
          console.log(error);
        }*/
      );
    }
}};
</script>
