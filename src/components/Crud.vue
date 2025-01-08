// filepath: /c:/project2/sdgs-dashboard/src/components/Crud.vue
<template>
  <div>
    <h1>CRUD Operations</h1>
    <button @click="loadDocuments">Load Documents</button>
    <table v-if="documents.length">
      <thead>
        <tr>
          <th>Actions</th>
          <th title="Country Name">Country Name</th>
          <th title="Country ISO3">Country ISO3</th>
          <th title="Year" @click="sortDocuments">Year</th>
          <th title="Agricultural land (sq. km)">Agri. land (sq. km)</th>
          <th title="Agricultural land (% of land area)">Agri. land (%)</th>
          <th title="Arable land (% of land area)">Arable land (%)</th>
          <th title="Rural land area where elevation is below 5 meters (sq. km)">Rural land below 5m (sq. km)</th>
          <th title="Rural land area where elevation is below 5 meters (% of total land area)">Rural land below 5m (%)</th>
          <th title="Urban land area where elevation is below 5 meters (sq. km)">Urban land below 5m (sq. km)</th>
          <th title="Urban land area where elevation is below 5 meters (% of total land area)">Urban land below 5m (%)</th>
          <th title="Land area where elevation is below 5 meters (% of total land area)">Land below 5m (%)</th>
          <th title="Forest area (sq. km)">Forest area (sq. km)</th>
          <th title="Forest area (% of land area)">Forest area (%)</th>
          <th title="Average precipitation in depth (mm per year)">Precipitation (mm/year)</th>
          <th title="Cereal yield (kg per hectare)">Cereal yield (kg/ha)</th>
          <th title="Access to electricity (% of population)">Electricity access (%)</th>
          <th title="Renewable energy consumption (% of total final energy consumption)">Renewable energy (%)</th>
          <th title="Disaster risk reduction progress score (1-5 scale; 5=best)">Disaster risk score</th>
          <th title="Rural population living in areas where elevation is below 5 meters (% of total population)">Rural pop. below 5m (%)</th>
          <th title="Urban population living in areas where elevation is below 5 meters (% of total population)">Urban pop. below 5m (%)</th>
          <th title="Population living in areas where elevation is below 5 meters (% of total population)">Pop. below 5m (%)</th>
          <th title="Population in urban agglomerations of more than 1 million (% of total population)">Urban agglom. > 1M (%)</th>
          <th title="Terrestrial protected areas (% of total land area)">Terrestrial protected (%)</th>
          <th title="Marine protected areas (% of territorial waters)">Marine protected (%)</th>
          <th title="Terrestrial and marine protected areas (% of total territorial area)">Total protected (%)</th>
          <th title="Ease of doing business rank (1=most business-friendly regulations)">Ease of business rank</th>
          <th title="CPIA public sector management and institutions cluster average (1=low to 6=high)">CPIA score</th>
          <th title="Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)">Poverty ratio (%)</th>
          <th title="Population growth (annual %)">Pop. growth (%)</th>
          <th title="Urban population growth (annual %)">Urban pop. growth (%)</th>
          <th title="Urban population">Urban pop.</th>
          <th title="Urban population (% of total population)">Urban pop. (%)</th>
        </tr>
      </thead>
      
      <tbody>
        <tr v-for="document in documents" :key="document._id">
          <td>
            <button class="edit-button" @click="editDocument(document._id)">Edit</button>
            <button class="delete-button" @click="deleteDocument(document._id)">Delete</button>
          </td>
          <td>{{ document["Country Name"] }}</td>
          <td>{{ document["Country ISO3"] }}</td>
          <td>{{ document.Year }}</td>
          <td>{{ formatNumber(document.data["Agricultural land (sq. km)"]) }}</td>
          <td>{{ formatNumber(document.data["Agricultural land (% of land area)"]) }}</td>
          <td>{{ formatNumber(document.data["Arable land (% of land area)"]) }}</td>
          <td>{{ formatNumber(document.data["Rural land area where elevation is below 5 meters (sq. km)"]) }}</td>
          <td>{{ formatNumber(document.data["Rural land area where elevation is below 5 meters (% of total land area)"]) }}</td>
          <td>{{ formatNumber(document.data["Urban land area where elevation is below 5 meters (sq. km)"]) }}</td>
          <td>{{ formatNumber(document.data["Urban land area where elevation is below 5 meters (% of total land area)"]) }}</td>
          <td>{{ formatNumber(document.data["Land area where elevation is below 5 meters (% of total land area)"]) }}</td>
          <td>{{ formatNumber(document.data["Forest area (sq. km)"]) }}</td>
          <td>{{ formatNumber(document.data["Forest area (% of land area)"]) }}</td>
          <td>{{ formatNumber(document.data["Average precipitation in depth (mm per year)"]) }}</td>
          <td>{{ formatNumber(document.data["Cereal yield (kg per hectare)"]) }}</td>
          <td>{{ formatNumber(document.data["Access to electricity (% of population)"]) }}</td>
          <td>{{ formatNumber(document.data["Renewable energy consumption (% of total final energy consumption)"]) }}</td>
          <td>{{ formatNumber(document.data["Disaster risk reduction progress score (1-5 scale; 5=best)"]) }}</td>
          <td>{{ formatNumber(document.data["Rural population living in areas where elevation is below 5 meters (% of total population)"]) }}</td>
          <td>{{ formatNumber(document.data["Urban population living in areas where elevation is below 5 meters (% of total population)"]) }}</td>
          <td>{{ formatNumber(document.data["Population living in areas where elevation is below 5 meters (% of total population)"]) }}</td>
          <td>{{ formatNumber(document.data["Population in urban agglomerations of more than 1 million (% of total population)"]) }}</td>
          <td>{{ formatNumber(document.data["Terrestrial protected areas (% of total land area)"]) }}</td>
          <td>{{ formatNumber(document.data["Marine protected areas (% of territorial waters)"]) }}</td>
          <td>{{ formatNumber(document.data["Terrestrial and marine protected areas (% of total territorial area)"]) }}</td>
          <td>{{ formatNumber(document.data["Ease of doing business rank (1=most business-friendly regulations)"]) }}</td>
          <td>{{ formatNumber(document.data["CPIA public sector management and institutions cluster average (1=low to 6=high)"]) }}</td>
          <td>{{ formatNumber(document.data["Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)"]) }}</td>
          <td>{{ formatNumber(document.data["Population growth (annual %)"]) }}</td>
          <td>{{ formatNumber(document.data["Urban population growth (annual %)"]) }}</td>
          <td>{{ formatNumber(document.data["Urban population"]) }}</td>
          <td>{{ formatNumber(document.data["Urban population (% of total population)"]) }}</td>
        </tr>
      </tbody>
    </table>
    <p v-else>No documents found.</p>
  </div>
</template>

<script>
import { fetchDocuments, deleteDocument } from "@/api/api.js";

export default {
  name: "CrudPage",
  data() {
    return {
      documents: [],
      sortOrder: 'desc', // Default sort order
    };
  },
  methods: {
    async loadDocuments() {
      try {
        const response = await fetchDocuments();
        console.log("API Response:", response); // Log the API response
        this.documents = response;
        this.sortDocuments(); // Sort documents after loading
      } catch (error) {
        console.error("Error loading documents:", error);
      }
    },
    sortDocuments() {
      this.documents.sort((a, b) => {
        if (this.sortOrder === 'desc') {
          return b.Year - a.Year;
        } else {
          return a.Year - b.Year;
        }
      });
    },
    async deleteDocument(id) {
      try {
        await deleteDocument(id);
        this.loadDocuments(); // Reload documents after deletion
      } catch (error) {
        console.error(`Error deleting document with ID ${id}:`, error);
      }
    },
    editDocument(id) {
      this.$router.push(`/edit/${id}`); // Navigate to the edit page
    },
    formatNumber(value) {
      if (typeof value === 'number') {
        return value.toFixed(2); // Format number to 2 decimal places
      }
      return value;
    }
  },
  mounted() {
    this.loadDocuments();
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  overflow-x: auto;
  display: block;
  font-size: 12px; /* Smaller font size for compact view */
}

th, td {
  border: 1px solid #ddd;
  padding: 4px; /* Reduced padding for compact view */
}

th {
  background-color: #f2f2f2;
  cursor: pointer; /* Indicate that the header is clickable */
}

tbody tr:nth-child(odd) {
  background-color: #f9f9f9; /* Light gray for odd rows */
}

tbody tr:nth-child(even) {
  background-color: #ffffff; /* White for even rows */
}

.edit-button, .delete-button {
  background-color: #e7e7e7; /* Light gray */
  color: black;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  margin-right: 5px;
}

.edit-button:hover {
  background-color: #d4d4d4; /* Darker gray */
}

.delete-button:hover {
  background-color: #d4d4d4; /* Darker gray */
}
</style>