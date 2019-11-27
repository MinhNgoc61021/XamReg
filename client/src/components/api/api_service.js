import axios from 'axios';
import { authHeader, isValidJwt } from './jwt_handling.js';
import { router } from "../../router";


//This is where the client call the api server
export const apiService = {
  signIn, signOut, getUserData
};

function signIn(username, password) {
  const path = '/auth/register';
  return axios.post(path, {
    username, password
  })
    .then(response => {
      // Check if the response is a token
      if (response.data.token) {
        // store user details and jwt in local storage to keep user signed in
        localStorage.setItem('user', JSON.stringify(response.data));
      }
      //console.log(response.data);
      return response.data;
    });
}

async function getUserData() {
    if (isValidJwt()) {
      try {
        const response = await axios({
          method: 'get',
          url: '/auth/get-user',
          headers: { 'Authorization': authHeader() },
        });
        if (response.status === 200) {
          return response;
        }
      } catch (err) {
        return err;
      }
    }
    else {
      alert('User is expired');
      localStorage.removeItem('user');
      await router.push('/register');
    }
}


function signOut() {
  console.log('Signed Out');
  // remove user token from local storage
  localStorage.removeItem('user');
}
