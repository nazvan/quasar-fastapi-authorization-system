<template>
  <q-page padding>
    <h1 class="text-h4 q-mb-md">Вход</h1>
    <LoginForm />
  </q-page>
</template>

<script setup lang="ts">
import LoginForm from 'components/LoginForm.vue';

defineOptions({
  name: 'LoginPage'
});
</script>