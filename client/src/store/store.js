import Vue from 'vue';
import Vuex from 'vuex';
import { apiService } from '../components/api/api_service.js';
import { router } from '../router/index.js';
Vue.use(Vuex);

const userData = localStorage.getItem('user');
const userState = userData ? { status: { signedIn: true}, userData } : { status: {}, userData: null};

export const store = new Vuex.Store ({
  state: {
    user: userState,
    ID: '',
    username: '',
    fullname: '',
    dob: '',
    gender: '',
  },
  mutations: {
        signinSuccess(state, user) {
            state.status = { signedIn: true };
            state.user = user;
        },
        getUserData(state, data) {
            state.username = data.ID;
            state.fullname = data.Fullname;
            state.dob = data.Dob;
            state.gender = data.Gender;

        },
        signinFailure(state) {
            state.status = {};
            state.user = null;
        },
        signout(state) {
            state.status = {};
            state.user = null;
        }
  },
  actions: {
      SignIn: (context, {username, password}) => {
        apiService.signIn(username, password)
          .then(
            (user) => {
              if (user.type === 'admin') {
                context.commit('signinSuccess', user.token);
                //console.log(user.token);
                router.push('/admin-page');
              }
              else if (user.type === 'student'){
                context.commit('signinSuccess', user.token);
                router.push('/student-page');
              }
            },
            error => {
              context.commit('signinFailure', error);
            },
          )
      },
      SignOut: () => {
        apiService.signOut();
        router.push('/register');
      },
      GetUserData: (context) => {
        apiService.getUserData()
          .then((UserData) => {
            context.commit('getUserData', UserData)
          });
        },
  },
  getters: {

  }
});
