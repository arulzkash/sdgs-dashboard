import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/Home.vue";
import Crud from "@/components/Crud.vue";
import Dashboard from "@/components/Dashboard.vue";

const routes = [
  {
    path: "/",
    component: Home,
    children: [
      {
        path: "",
        name: "DashboardPage",
        component: Dashboard,
      },
      {
        path: "crud",
        name: "CrudPage",
        component: Crud,
      },
    ],
  },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
