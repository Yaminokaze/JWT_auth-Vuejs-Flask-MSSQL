<template>
  <div class="col-sm-4 col-sm-offset-4">
    <h2>Sign Up</h2>
    <div class="alert alert-danger" v-if="error">
      <p>{{ error }}</p>
    </div>
    <div class="form-group">
      <input
        type="text"
        class="form-control"
        placeholder="Enter your username"
        v-model="credentials.username"
      />
    </div>
    <div class="form-group">
      <input
        type="email"
        class="form-control"
        placeholder="Enter your email"
        v-model="credentials.email"
      />
    </div>
    <div class="form-group">
      <input
        type="password"
        class="form-control"
        placeholder="Enter your password"
        v-model="credentials.password"
      />
    </div>
    <div class="form-group">
      <select aria-placeholder="Tunisia" class="form-control"  v-model="credentials.country">
        <option value="" disabled hidden>Select Country</option>
        <option value="Tunisia">Tunisia</option>
        <option value="Brazil">Brazil</option>
      </select>
    </div>
    <div class="form-group">
      <input type="date" class="form-control" v-model="credentials.birthdayDate" />
    </div>
        <div class="form-group">
           <router-link to="/login">you already have an account? </router-link> 
    </div>
    <button class="btn btn-primary" @click="submit()">Access</button>
  </div>
</template>

<script>
import auth from '../auth/index';

export default {
  data() {
    return {
      credentials: {
        username: "",
        email: "",
        country: "",
        birthdayDate: "",
        password: ""
      },
      error: ""
    };
  },

  methods: {
    submit() {
      var credentials = {
        username: this.credentials.username,
        email: this.credentials.email,
        country: this.credentials.country,
        birthdayDate: this.credentials.birthdayDate,
        password: this.credentials.password
      };

      auth.signup(this, credentials, "/");
    }
  }
};
</script>