import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: 'register', component: () => import('pages/Register.vue') },
      { path: 'login', component: () => import('pages/Login.vue') },
      { path: 'dashboard', component: () => import('pages/Dashboard.vue'), meta: { requiresAuth: true } },
      { path: 'images', component: () => import('pages/ImagesPage.vue'), meta: { requiresAuth: true } },
      { path: 'settings', component: () => import('pages/SettingsPage.vue'), meta: { requiresAuth: true } }
    ],
  },
  // ... остальные маршруты
];

export default routes;