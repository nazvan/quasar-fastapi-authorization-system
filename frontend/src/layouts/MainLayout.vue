<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          v-if="isAuthenticated"
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
        <q-toolbar-title>
          Ваше приложение
        </q-toolbar-title>
        <q-btn v-if="!isAuthenticated" to="/register" flat label="Регистрация" />
        <q-btn v-if="!isAuthenticated" to="/login" flat label="Вход" />
        <q-btn v-if="isAuthenticated" to="/dashboard" flat label="Панель управления" />
        <LogoutButton v-if="isAuthenticated" />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-if="isAuthenticated"
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label header>
          Меню
        </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from 'src/stores/auth';
import { storeToRefs } from 'pinia';
import EssentialLink, { EssentialLinkProps } from 'components/EssentialLink.vue';
import LogoutButton from 'components/LogoutButton.vue';


defineOptions({
  name: 'MainLayout'
});

const essentialLinks: EssentialLinkProps[] = [
  {
    title: 'Все изображения',
    caption: 'Просмотр всех изображений',
    icon: 'image',
    link: '/images'
  },
  {
    title: 'Настройки',
    caption: 'Настройки приложения',
    icon: 'settings',
    link: '/settings'
  }
];

const leftDrawerOpen = ref(false);
const authStore = useAuthStore();
const { isAuthenticated } = storeToRefs(authStore);

const toggleLeftDrawer = () => {
  leftDrawerOpen.value = !leftDrawerOpen.value;
};
</script>