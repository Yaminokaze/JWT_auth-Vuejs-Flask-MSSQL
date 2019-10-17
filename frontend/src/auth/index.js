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
        localStorage.setItem("access_token", data.acces_token);
        localStorage.setItem("refresh_token", data.refresh_token);

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

  signup(context, creds, redirect) {
    context.$http.post(SIGNUP_URL, creds).then(
      response => {
        localStorage.setItem("access_token", response.access_token);
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
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    this.user.authenticated = false;
    router.go("/");
  },

  checkAuth() {
    var jwt = localStorage.getItem("access_token");
    if (jwt) {
      this.user.authenticated = true;
    } else {
      this.user.authenticated = false;
    }
  },

  getAuthHeader() {
    return {
      Authorization: "Bearer " + localStorage.getItem("access_token")
    };
  }
};
