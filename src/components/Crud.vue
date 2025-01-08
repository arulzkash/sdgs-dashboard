<template>
  <div>
    <h1>CRUD Operations</h1>
    <button @click="loadUsers">Load Users</button>
    <table v-if="users.length">
      <thead>
        <tr>
          <th>ID</th>
          <th>Username</th>
          <th>Email</th>
          <th>Actions</th>
        </tr>
      </thead>
      
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>
            <button @click="editUser(user.id)">Edit</button>
            <button @click="deleteUser(user.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-else>No users found.</p>
  </div>
</template>

<script>
import { fetchUsers, deleteUser } from "@/api/api.js";

export default {
  name: "CrudPage",
  data() {
    return {
      users: [],
    };
  },
  methods: {
    async loadUsers() {
      try {
        this.users = await fetchUsers();
      } catch (error) {
        console.error("Error loading users:", error);
      }
    },
    async deleteUser(id) {
      try {
        await deleteUser(id);
        this.loadUsers(); // Reload users after deletion
      } catch (error) {
        console.error(`Error deleting user with ID ${id}:`, error);
      }
    },
    editUser(id) {
      // Implement edit user functionality
      console.log(`Edit user with ID ${id}`);
    },
  },
  mounted() {
    this.loadUsers();
  },
};
</script>

<style scoped>
/* Add your styles here */
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
}

th {
  background-color: #f2f2f2;
}
</style>