<template>
  <q-page padding>
    <h1 class="text-h4 q-mb-md">Регистрация</h1>
    <RegisterForm />
  </q-page>
</template>

<script setup lang="ts">
import RegisterForm from 'components/RegisterForm.vue';

defineOptions({
  name: 'RegisterPage'
});
</script>