<template>
  <div class="col-sm-6 col-sm-offset-3">
    <h1>Welcome {{credentials.username}}!</h1>
     <h2> Email: {{credentials.email}} </h2>
     <h2> Country: {{credentials.country}} </h2>
     <h2> birthdayDate: {{credentials.birthdayDate}} </h2>
    </div>
  </div>
</template>

<script>
import auth from "@/auth/index";

export default {
  data() {
    return {
      credentials: {
        username: "",
        email: "",
        country: "",
        birthdayDate: "",
      },
    };
  },

  methods: {
    mounted() {
      this.$http
        .get('http://localhost:/5000/home', (data) => {
          this.credentials = data;
        }, { 
          headers: auth.getAuthHeader()
        })
      //  .error(err => {console.log(err)}
      }
  }

}
</script>
