// The authHeader is used to make authenticated HTTP requests to the server api using JWT authentication.
import { router } from "../../router";
import  Vue from 'vue';
import { apiService } from '../api/api_service';
export function authHeader() {
    // return authorization header with jwt token
    let user = JSON.parse(localStorage.getItem('user'));
    // console.log(user.token);
    if (isValidJwt()) {
        return 'Bearer: ' + user.token; // send encoded jwt token
    }
    else {
        apiService.signOut();
        Vue.prototype.$buefy.dialog.alert({
            title: 'Hết thời gian sử dụng',
            message: 'Hãy đăng nhập vào hệ thống để sử dụng tiếp!',
            type: 'is-danger',
            hasIcon: true,
            icon: 'times-circle',
            iconPack: 'fa',
            ariaRole: 'alertdialog',
            ariaModal: true,
            onConfirm: () => {
              router.push('/register');
            },
          });
    }
}

// What you’re essentially getting is a component that’s entirely decoupled from the DOM or the rest of your app
// The isValid(jwt) function is used to determine if a user if authenticated based off the information in the JWT.
// JWT (JSON Web Token) is an encoded JSON object of the form "[HEADER].[PAYLOAD].[SIGNATURE]".
export function isValidJwt() {
  const jwt = localStorage.getItem('user');
  if (!jwt || jwt.split('.').length < 3) {
    return false
  }
  const data = JSON.parse(atob(jwt.split('.')[1]));
  const exp = new Date(data.exp * 1000); // JS deals with dates in milliseconds since epoch
  const now = new Date();
  return now <= exp;
}

export function getToken() {
    return JSON.parse(localStorage.getItem('user'));
}

