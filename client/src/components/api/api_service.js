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
  try {
    if (isValidJwt()) {
      const response = await axios({
        method: 'get',
        url: '/auth/get-user',
        headers: authHeader(),
      });
      let { data } = response;
      console.log(response.status);
      if (response.status === 200) {
        return data;
      }
      else if (response.status === 401) {
        localStorage.removeItem('user');
        await router.push('/register');
      }
    }
    else {
      alert('User is expired');
      localStorage.removeItem('user');
      await router.push('/register');
    }
  }
   catch (err) {
    return err.message;
   }

}

function signOut() {
  console.log('Signed Out');
  // remove user token from local storage
  localStorage.removeItem('user');
}
// }
//
// // check if the response from the api is Unauthorized
// // this handles if the JWT token expires or is no longer valid for any reason.
// // function handleResponse(response) {
// //     return response.then(text => {
// //         const data = text && JSON.parse(text);
// //         if (!response.ok) {
// //             if (response.status === 401) {
// //                 // auto logout if 401 response returned from api
// //                 signOut();
// //                 location.reload(true);
// //             }
// //
// //             const error = (data && data.message) || response.statusText;
// //             return Promise.reject(error);
// //         }
// //
// //         return data;
// //     });
// // }
