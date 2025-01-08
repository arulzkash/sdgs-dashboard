import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/Home.vue";
import Crud from "@/components/Crud.vue";
import Dashboard from "@/components/Dashboard.vue";
import EditDocument from "@/components/EditDocument.vue";

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
      {
        path: "/edit/:id",
        name: "EditDocument",
        component: EditDocument,
      },
    ],
  },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
