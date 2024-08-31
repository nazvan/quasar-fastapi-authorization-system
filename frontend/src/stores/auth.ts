import { defineStore } from 'pinia';
import { getCurrentUser } from 'src/api/auth';

interface User {
  id: number;
  email: string;
  first_name: string;
  last_name: string;
  // добавьте другие поля пользователя по необходимости
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as User | null,
  }),
  getters: {
    isAuthenticated: (state) => !!state.user,
  },
  actions: {
    setUser(user: User) {
      this.user = user;
    },
    clearUser() {
      this.user = null;
    },
    async initializeAuth() {
      try {
        const user = await getCurrentUser();
        this.setUser(user);
      } catch (error) {
        console.error('Failed to initialize auth:', error);
        this.clearUser();
      }
    },
  },
});