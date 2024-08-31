<template>
  <q-btn label="Выйти" @click="onLogout" color="negative" />
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useQuasar } from 'quasar';
import { logout } from 'src/api/auth';
import { useAuthStore } from 'src/stores/auth';

const router = useRouter();
const $q = useQuasar();
const authStore = useAuthStore();

const onLogout = async () => {
  try {
    await logout();
    authStore.clearUser();
    $q.notify({
      type: 'positive',
      message: 'Вы успешно вышли из системы'
    });
    router.push('/login');
  } catch (error) {
    console.error('Error during logout:', error);
    let errorMessage = 'Ошибка при выходе из системы';
    if (error instanceof Error) {
      errorMessage += `: ${error.message}`;
    }
    $q.notify({
      type: 'negative',
      message: errorMessage
    });
  }
};
</script>