// filepath: /c:/project2/sdgs-dashboard/src/components/Crud.vue

<template>
  <div>
    <div class="Title-container">
      <h1>Manage Data</h1>
    </div>
    <!-- Tambahkan container untuk tombol -->
    <div class="button-container">
      <button @click="navigateToAdd" class="primary-button">Add Document</button>
    </div>
    <table v-if="documents.length">
      <thead>
        <tr>
          <th>NO</th>
          <th title="Country Name">Country Name</th>
          <th title="Country ISO3">Country ISO3</th>
          <th title="Year" class="sortable-header underline" @click="toggleSortOrder">Year</th>
          <th title="Agricultural land (sq. km)">Agri. land (sq. km)</th>
          <th title="Agricultural land (% of land area)">Agri. land (%)</th>
          <th title="Arable land (% of land area)">Arable land (%)</th>
          <th >Actions</th>
        </tr>
      </thead>
      
      <tbody>
        <tr v-for="(document, index) in documents" :key="document._id">
          <td>{{ index + 1 }}</td>
          <td>{{ document["Country Name"] }}</td>
          <td>{{ document["Country ISO3"] }}</td>
          <td>{{ document.Year }}</td>
          <td>{{ formatNumber(document.data["Agricultural land (sq. km)"]) }}</td>
          <td>{{ formatNumber(document.data["Agricultural land (% of land area)"]) }}</td>
          <td>{{ formatNumber(document.data["Arable land (% of land area)"]) }}</td>
          <td class="actions-container">
            <button class="btn-sm warning-button" @click="editDocument(document._id)">Edit</button>
            <button class="btn-sm danger-button" @click="confirmDelete(document._id)">Delete</button>
            <button class="btn-sm primary-button"  @click="viewDetailsWithAlert(document._id)">Detail</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-else>No documents found.</p>
  </div>
</template>

<script>
import { fetchDocuments, deleteDocument,fetchDocumentById } from "@/api/api.js";
import Swal from 'sweetalert2';
// import axios from "axios";
export default {
  name: "CrudPage",
  data() {
    return {
      documents: [],
      sortOrder: 'desc', // Default sort order
      selectedDocument: null, // Untuk menyimpan dokumen yang dipilih
      showDetailModal: false, // Untuk mengontrol tampilan modal detail
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
async viewDetailsWithAlert(documentId) {
  try {
    const response = await fetchDocumentById(documentId);
    console.log("API Response:", response); // Log the API response
    this.selectedDocument = response; // Menyimpan document yang terpilih

    // Buat konten yang ingin ditampilkan di SweetAlert2
    let details = '';
    
    // Loop untuk mengecek semua field dan hanya menampilkan yang bukan undefined
    const fields = [
      "Country Name",
      "Country ISO3",
      "Year",
      "Agricultural land (sq. km)",
      "Agricultural land (% of land area)",
      "Arable land (% of land area)",
      "Average precipitation in depth (mm per year)",
      "Cereal yield (kg per hectare)",
      "Population in urban agglomerations of more than 1 million (% of total population)",
      "Population growth (annual %)",
      "Urban population growth (annual %)",
      "Urban population",
      "Urban population (% of total population)"
    ];
    
    fields.forEach(field => {
      // Cek apakah nilai field tersebut ada (bukan undefined)
      if (this.selectedDocument[field] !== undefined && this.selectedDocument[field] !== null) {
        details += `<div><strong>${field}:</strong> ${this.selectedDocument[field]}<div/>`;
      }
      else if (this.selectedDocument.data[field] !== undefined && this.selectedDocument.data[field] !== null) {
        details += `<div><strong>${field}:</strong> ${this.selectedDocument.data[field]}<div/>`;
      }
    });

    // Tampilkan detail menggunakan SweetAlert2
    await Swal.fire({
      title: 'Document Details',
      html: details,
      icon: 'info',
      confirmButtonText: 'Close'
    });

    // Setelah menutup alert, load ulang data untuk menampilkan data awal
    this.loadDocuments();
  } catch (error) {
    console.error("Error fetching document details:", error);
    await Swal.fire({
      title: 'Error',
      text: 'Failed to fetch document details. Please try again.',
      icon: 'error',
      confirmButtonText: 'Close'
    });
  }
},

    formatNumber(value) {
      if (typeof value === "number") {
        return value.toFixed(2); // Format angka hingga 2 desimal
      }
      return value;
    },
    toggleSortOrder() {
      // Toggle the sort order between 'asc' and 'desc'
      this.sortOrder = this.sortOrder === 'desc' ? 'asc' : 'desc';
      this.sortDocuments(); // Re-sort documents after toggling
    },
    async deleteDocument(id) {
      try {
        await deleteDocument(id);
        this.loadDocuments(); // Reload documents after deletion
      } catch (error) {
        console.error(`Error deleting document with ID ${id}:`, error);
      }
    },
    confirmDelete(id) {
      if (confirm("Are you sure you want to delete this document?")) {
        this.deleteDocument(id);
      }
    },

    editDocument(id) {
      this.$router.push(`/edit/${id}`); // Navigate to the edit page
    },
    navigateToAdd() {
      this.$router.push('/add'); // Navigate to the add page
    },
    // eslint-disable-next-line no-dupe-keys, vue/no-dupe-keys
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
/* Default styles (light mode) */
/* Gaya untuk container tombol */
.button-container {
  margin: 10px 0; /* Beri jarak atas dan bawah */
  display: flex; /* Untuk tata letak fleksibel */
  justify-content: flex-start; /* Posisi tombol di kiri (bisa diganti ke 'center' atau 'flex-end') */
}

.actions-container{
  display: flex;
  gap: 4px;
}
.Title-container {
  font-size: xx-large;
  display: flex;
  flex-direction: column; /* Elemen diatur secara vertikal */
  align-items: center; /* Elemen dipusatkan secara horizontal */
  margin-top: 20px; /* Jarak dari atas halaman */
}


/* Button Warning (Kuning) */
.warning-button {
  background-color: #ffc107; /* Warna kuning */
  color: black; /* Teks hitam */
  padding: 5px 10px; /* Ukuran tombol */
  border: none; /* Hapus border default */
  border-radius: 5px; /* Sudut membulat */
  cursor: pointer; /* Tampilkan kursor pointer */
  font-size: 14px; /* Ukuran font */
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2); /* Efek bayangan */
  transition: background-color 0.3s; /* Efek animasi */
}

/* Gaya tombol saat di-hover */
.warning-button:hover {
  background-color: #e0a800; /* Warna kuning lebih gelap saat hover */
}

/* Button Danger (Merah) */
.danger-button {
  background-color: #dc3545; /* Warna merah */
  color: white; /* Teks putih */
  padding: 5px 10px; /* Ukuran tombol */
  border: none; /* Hapus border default */
  border-radius: 5px; /* Sudut membulat */
  cursor: pointer; /* Tampilkan kursor pointer */
  font-size: 14px; /* Ukuran font */
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2); /* Efek bayangan */
  transition: background-color 0.3s; /* Efek animasi */
}

/* Gaya tombol saat di-hover */
.danger-button:hover {
  background-color: #a71d2a; /* Warna merah lebih gelap saat hover */
}


/* Gaya tombol utama */
.primary-button {
  background-color: #007bff; /* Warna biru */
  color: white; /* Teks putih */
  padding: 5px 10px; /* Ukuran tombol */
  border: none; /* Hapus border default */
  border-radius: 5px; /* Sudut membulat */
  cursor: pointer; /* Tampilkan kursor pointer */
  font-size: 14px; /* Ukuran font */
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2); /* Efek bayangan */
  transition: background-color 0.3s; /* Efek animasi */
}

/* Gaya tombol saat di-hover */
.primary-button:hover {
  background-color: #0056b3; /* Warna biru lebih gelap saat hover */
}

table {
  width: 100%;
  border-collapse: collapse;
  overflow-x: auto;
  display: block;
  font-size: 12px;
}

th, td {
  border: 1px solid #ddd;
  padding: 4px;
  color: black; /* Teks default hitam */
}

th {
  background-color: #f2f2f2;
  cursor: pointer;
}

tbody tr:nth-child(odd) {
  background-color: #f9f9f9;
}

tbody tr:nth-child(even) {
  background-color: #ffffff;
}

/* year button sort */
.sortable-header.underline {
  cursor: pointer; /* Menunjukkan bahwa elemen bisa diklik */
  text-decoration: underline; /* Memberikan garis bawah permanen */
  text-decoration-color: #000000; /* Warna garis bawah (bisa disesuaikan) */
  text-decoration-thickness: 2px; /* Ketebalan garis bawah */
}



/* Buttons */
.edit-button, .delete-button {
  background-color: #e7e7e7;
  color: black;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  margin-right: 5px;
}

.edit-button:hover {
  background-color: #d4d4d4;
}

.delete-button:hover {
  background-color: #d4d4d4;
}

/* Dark mode styles */
body.dark-mode table {
  background-color: #2e2e2e; /* Background tabel gelap */
  color: white; /* Teks putih */
}

body.dark-mode th, body.dark-mode td {
  border: 1px solid #555; /* Border gelap */
}

body.dark-mode th {
  background-color: #444; /* Header gelap */
}

body.dark-mode tbody tr:nth-child(odd) {
  background-color: #3a3a3a; /* Baris ganjil gelap */
}

body.dark-mode tbody tr:nth-child(even) {
  background-color: #2e2e2e; /* Baris genap gelap */
}

body.dark-mode .edit-button, body.dark-mode .delete-button {
  background-color: #555;
  color: white;
}

body.dark-mode .edit-button:hover, body.dark-mode .delete-button:hover {
  background-color: #666;
}
</style>
