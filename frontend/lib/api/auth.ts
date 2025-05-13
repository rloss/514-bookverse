import axios from 'axios';

export const login = async (providerToken: string) => {
  return axios.post('/api/v1/auth/social-login', { token: providerToken });
};
