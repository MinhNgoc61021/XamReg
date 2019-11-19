import axios from 'axios';
import { authHeader, isValidJwt } from './jwt_handling.js';


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
      //const userPayload = getTokenData(response.data.token);
      //console.log(response.data);
      if (response.data.token) {
        // store user details and jwt in local storage to keep user signed in
        localStorage.setItem('user', JSON.stringify(response.data));
      }
      //console.log(response.data);
      return response.data;
    });
}


function getUserData() {
  if (isValidJwt()) {
    return axios({
      method: 'get',
      url: '/auth/get-user',
      headers: authHeader(),
    }).then((response => {
      return response.data;
    }));
  }
   else {
     return {'error': 'JWT invalid'};
  }

}

function signOut() {
  console.log('Signed Out');
  // remove user token from local storage
  localStorage.removeItem('user');
}

// check if the response from the api is Unauthorized
// this handles if the JWT token expires or is no longer valid for any reason.
function handleResponse(response) {
    return response.then(text => {
        const data = text && JSON.parse(text);
        if (!response.ok) {
            if (response.status === 401) {
                // auto logout if 401 response returned from api
                signOut();
                location.reload(true);
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    });
}
