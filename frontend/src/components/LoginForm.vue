<template>
  <q-form @submit="onSubmit" class="q-gutter-md">
    <q-input
      v-model="email"
      label="Email"
      type="email"
      :rules="[
        val => !!val || 'Обязательное поле',
        val => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(val) || 'Некорректный email'
      ]"
    />
    <q-input
      v-model="password"
      label="Пароль"
      type="password"
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-btn label="Войти" type="submit" color="primary"/>
  </q-form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useQuasar } from 'quasar';
import { useRouter } from 'vue-router';
import { login, getCurrentUser } from 'src/api/auth';
import { useAuthStore } from 'src/stores/auth';

const $q = useQuasar();
const router = useRouter();
const authStore = useAuthStore();

const email = ref('');
const password = ref('');

const onSubmit = async () => {
  try {
    await login(email.value, password.value);
    // Здесь мы не устанавливаем токен вручную, так как он должен быть установлен в куки на сервере
    const user = await getCurrentUser();
    authStore.setUser(user); // Убедитесь, что этот метод существует в authStore
    $q.notify({
      type: 'positive',
      message: `Вход выполнен успешно! Добро пожаловать, ${user.first_name}!`
    });
    router.push('/dashboard');
  } catch (error) {
    console.error('Error during login:', error);
    $q.notify({
      type: 'negative',
      message: 'Ошибка при входе. Пожалуйста, проверьте ваши учетные данные и попробуйте снова.'
    });
  }
};
</script>

<style scoped>
.q-form {
  max-width: 400px;
  margin: 0 auto;
}
</style>