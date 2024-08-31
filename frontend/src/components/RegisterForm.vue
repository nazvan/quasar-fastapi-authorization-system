<template>
  <q-form @submit="onSubmit" class="q-gutter-md">
    <q-input
      v-model="email"
      label="Email"
      type="email"
      :rules="[val => !!val || 'Обязательное поле', val => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(val) || 'Некорректный email']"
    />
    <q-input
      v-model="password"
      label="Пароль"
      type="password"
      :rules="[val => !!val || 'Обязательное поле', val => val.length >= 8 || 'Минимум 8 символов']"
    />
    <q-input
      v-model="phone_number"
      label="Номер телефона"
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-input
      v-model="first_name"
      label="Имя"
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-input
      v-model="last_name"
      label="Фамилия"
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-btn label="Зарегистрироваться" type="submit" color="primary"/>
  </q-form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useQuasar } from 'quasar';
import { register } from 'src/api/auth';

const $q = useQuasar();

const email = ref('');
const password = ref('');
const phone_number = ref('');
const first_name = ref('');
const last_name = ref('');

const onSubmit = async () => {
  try {
    await register(email.value, password.value, phone_number.value, first_name.value, last_name.value);
    $q.notify({
      color: 'positive',
      message: 'Регистрация успешна!'
    });
    // Перенаправление на страницу входа
  } catch (error) {
    $q.notify({
      color: 'negative',
      message: 'Ошибка при регистрации'
    });
  }
};
</script>