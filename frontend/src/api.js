import axios from 'axios';

export function getReps(stateID) {
  return axios.get('http://' + process.env.REACT_APP_LOCAL_HOST_IP_ADDR + '/getReps',{
    params: {
      stateID: stateID
    }
  });
};
