import Vue from 'vue';
import Vuex from 'vuex';
import { apiService } from '../components/api/api_service.js';
import { router } from '../router/index.js';
import createPersistedState from "vuex-persistedstate";
Vue.use(Vuex);

const userData = localStorage.getItem('user');
const userState = userData ? { status: { signedIn: true}, userData } : { status: {}, userData: null};

export const store = new Vuex.Store ({
  state: {
    userStatus: userState,
    ID: '',
    fullname: '',
    isNotExist: false,
  },
  plugins: [createPersistedState()],
  mutations: {
        signInSuccess(state, user) {
            state.userStatus = { signedIn: true };
            state.isNotExist = false;
        },
        getUserData(state, data) {
            state.ID = data.ID;
            state.fullname = data.Fullname;
        },
        signInFailure(state) {
            state.isNotExist = true;
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
              if (response.type === 'Admin') {
                context.commit('signInSuccess', response.token);
                //console.log(user.token);
                router.push('/admin');
              }
              else if (response.type === 'Student'){
                context.commit('signInSuccess', response.token);
                router.push('/student');
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

  },
});
