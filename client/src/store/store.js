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
    current_location: ['1'],
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
            state.userStatus = {};

        },
        signOut(state) {
          state.userStatus = {};
        },
        setCurrentLocation(state, index) {
          state.current_location.pop();
          state.current_location.push(index);
        }
  },
  actions: {
      SignIn: (context, { username, password }) => {
        apiService.signIn(username, password)
          .then(
            (user) => {
              if (user.type === 'Admin') {
                context.commit('signInSuccess', user.token);
                //console.log(user.token);
                router.push('/admin-page');
              }
              else if (user.type === 'Student'){
                context.commit('signInSuccess', user.token);
                router.push('/student-page');
              }
            },
            error => {
              context.commit('signInFailure', error);
            },
          )
      },
      SignOut: () => {
        apiService.signOut();
        router.push('/register');
      },
      GetUserData: (context) => {
        apiService.getUserData()
          .then(
            (UserData) => {
              context.commit('getUserData', UserData);
            },
            error => {
              context.commit('signOut', error);
            },
          )
        },
  },
  getters: {

  }
});
