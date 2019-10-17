import router from "@/router/index";

const API_URL = "http://localhost:5000";
const LOGIN_URL = API_URL + "/login";
const SIGNUP_URL = API_URL + "/signup";

export default {
  user: {
    authenticated: false
  },

  login(context, creds, redirect) {
    context.$http.post(LOGIN_URL, creds).then(
      data => {
        localStorage.setItem("acces_token", data.acces_token);
        localStorage.setItem("refresh_token", data.refresh_token);

        this.user.authenticated = true;

        if (redirect) {
          router.go(redirect);
        }
      },
      error => {
        context.error = error;
      }
    );
  },

  signup(context, creds, redirect) {
    context.$http.post(SIGNUP_URL, creds).then(
      response => {
        localStorage.setItem("acces_token", response.access_token);
        localStorage.setItem("refresh_token", response.refresh_token);
        this.user.authenticated = true;

        if (redirect) {
          router.go(redirect);
        }
      },
      error => {
        context.error = error.message;
      }
    );
  },

  logout() {
    localStorage.removeItem("acces_token");
    localStorage.removeItem("refresh_token");
    this.user.authenticated = false;
  },

  checkAuth() {
    var jwt = localStorage.getItem("acces_token");
    if (jwt) {
      this.user.authenticated = true;
    } else {
      this.user.authenticated = false;
    }
  },

  getAuthHeader() {
    return {
      Authorization: "Bearer " + localStorage.getItem("id_token")
    };
  }
};
