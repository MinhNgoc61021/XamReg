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
    currentSemesterID: '', // dùng cái này thì khi sinh viên vào nó ko phải nhập lại Kỳ thi lần 2 nữa, chỉ có khi nào đăng xuất rồi sau mới phải đánh lại
    register_loading: false,
  },
  plugins: [createPersistedState()],
  mutations: {
        Exist(state, user) {
            state.userStatus = { signedIn: true };
            state.isNotExist = false;
        },
        getUserData(state, data) {
            state.ID = data.ID;
            state.fullname = data.Fullname;
        },
        notExist(state) {
            state.isNotExist = true;
        },
        signOut(state) {
            state.userStatus = {};
            state.ID = '';
            state.fullname = '';
            state.currentSemesterID = '';
        },
        setCurrentSemesterID(state, CurrentSemesterID) {
            state.currentSemesterID = CurrentSemesterID;
        },
        loadingFalse(state) {
            state.register_loading = false;
        },
        loadingTrue(state) {
            state.register_loading = true;
        }
  },
  actions: {
      SignIn: (context, { username, password }) => {
        context.commit('loadingTrue');
        apiService.signIn(username, password)
          .then(
            (response) => {
              if (response.type === 'Admin') {
                context.commit('Exist', response.token);
                context.commit('loadingFalse');
                router.push('/admin');
              }
              else if (response.type === 'Student'){
                context.commit('Exist', response.token);
                context.commit('loadingFalse');
                router.push('/student');
              }
              else if (response.status === 'fail') {
                context.commit('notExist');
                setTimeout(function () {
                  context.commit('Exist');
                }, 2000);
                context.commit('loadingFalse');
              }
            })
      },
      SignOut: (context) => {
        context.commit('signOut');
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
      SetCurrentSemesterID: (context, semID) => { // hàm này gọi bên shift_register
        context.commit('setCurrentSemesterID', semID);
      },

  },
  getters: {
  },
});
