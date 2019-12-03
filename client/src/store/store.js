import Vue from 'vue';
import Vuex from 'vuex';
import { apiService } from '../components/api/api_service.js';
import { router } from '../router/index.js';
Vue.use(Vuex);

const userData = localStorage.getItem('user');
const userState = userData ? { status: { signedIn: true}, userData } : { status: {}, userData: null};

export const store = new Vuex.Store ({
  state: {
    userStatus: userState,
    ID: '',
    fullname: '',
    userExistence: false,
  },
  mutations: {
        signInSuccess(state, user) {
            state.userStatus = { signedIn: true };
        },
        getUserData(state, data) {
            state.ID = data.ID;
            state.fullname = data.Fullname;
        },
        signInFailure(state) {
            state.userExistence = true;
        },
        signOut(state) {
          state.userStatus = {};
        },
  },
  actions: {
      SignIn: (context, { username, password }) => {
        apiService.signIn(username, password)
          .then(
            (response) => {
              console.log(response);
              if (response.type === 'Admin') {
                context.commit('signInSuccess', response.token);
                //console.log(user.token);
                router.push('/admin-page');
              }
              else if (response.type === 'Student'){
                context.commit('signInSuccess', response.token);
                router.push('/student-page');
              }
              else if (response.status === 'fail') {
                context.commit('signInFailure');
              }
            })
      },
      SignOut: () => {
        apiService.signOut();
        router.push('/register');
      },
      GetUserData: (context) => {
        apiService.getUserData()
          .then(
            (response) => {
              if (response.status === 200) {
                context.commit('getUserData', response.data);
              }},
          )
        },
  },
  getters: {

  }
});
