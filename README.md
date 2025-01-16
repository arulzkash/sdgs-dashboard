# 🌍 Dashboard SDG 13 Climate Change

## 📖 Description
This dashboard visualizes data related to SDG 13 (Climate Action) by showcasing trends and insights using interactive charts. It provides insights into agricultural and forestry land use, forest area vs protected areas, energy indicators, urbanization impacts, and more. Users can manage and customize the displayed fields via CRUD functionality.

---

## ✨ Key Features

1. **Visualization of Key Indicators**
   - **Agricultural and Forestry Land Use**: Trends in land use for agriculture and forestry in Indonesia (area in km² and as a percentage of total land area).
   - **Forest Area vs Protected Areas**: Contribution of forested areas and protected areas to environmental conservation.
   - **Energy Indicators**: Percentage of the population with access to electricity and renewable energy consumption.
   - **Urbanization and Renewable Energy**: Impact of urbanization on renewable energy usage.
   - **Population Density vs Forest Areas**: Relationship between population density and forest area.
   and more...

2. **CRUD Functionality**
   - Manage dashboard fields via CRUD (Create, Read, Update, Delete) operations.
   - Add, update, or delete documents dynamically to customize dashboard displays.

3. **Sorting Functionality**
   - Sort documents to prioritize or organize data fields for visualization.

4. **Interactive Dashboard**
   - Built with Vue.js for a seamless and dynamic user experience.
   - MongoDB Charts integration for visually appealing and interactive graphs.

---

## 🛠️ Technologies Used

- **Frontend**: Vue.js
- **Backend**: FastAPI
- **Visualization**: MongoDB Charts
- **Database**: MongoDB Atlas (cloud-based)

---

## 🚀 Installation

Follow these steps to set up the application locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/arulzkash/bookstore.git
   ```

2. Navigate to the project directory:
   ```bash
   cd sdg13-climate-change-dashboard
   ```

3. Install dependencies:
   - For the frontend:
     ```bash
     cd frontend
     npm install
     ```
   - For the backend:
     ```bash
     cd backend
     pip install -r requirements.txt
     ```

4. Configure the database connection:
   - Update the MongoDB Atlas connection string in the backend `.env` file.

5. Run the application:
   - Start the backend server:
     ```bash
     uvicorn main:app --reload
     ```
   - Start the frontend:
     ```bash
     npm run serve
     ```

6. Access the dashboard via your browser at `http://localhost:8080`.

---

## 🛒 Usage

1. **Dashboard**
   - View key visualizations such as agricultural land trends, energy indicators, and urbanization impacts.

2. **CRUD Functionality**
   - Manage fields and documents directly from the dashboard to customize data visualizations.

3. **Sorting**
   - Organize displayed fields by applying sorting rules.

---

## 📂 Project Structure

```
sdg13-climate-change-dashboard/
├── frontend/           # Vue.js frontend code
├── backend/            # FastAPI backend code
├── assets/             # Static assets and styles
├── .env                # Environment configuration
├── README.md           # Project documentation
```

---

## 📷 Screenshots

1. **Dashboard**
    ![image](https://github.com/user-attachments/assets/21e1d85f-315f-4354-b2a6-3010a7ec8937)
    ![image](https://github.com/user-attachments/assets/1991f884-caf9-418f-a7e8-75e6d23c2a5d)
    ![image](https://github.com/user-attachments/assets/fb043e62-c75b-4602-a594-c47fd7459f58)


2. **CRUD**
   ![image](https://github.com/user-attachments/assets/2563f0d3-4335-4863-b9eb-3c9b3e316ac1)
   ![image](https://github.com/user-attachments/assets/37bb31c4-7ec3-493b-8fc6-33328dd803eb)
   ![image](https://github.com/user-attachments/assets/69ad106f-5496-44a7-8163-36104aba5994)


3. **FASTAPI**
   ![image](https://github.com/user-attachments/assets/16d0a298-d2f1-4442-90f9-e66707811bf9)




---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

- @boyaditya
- @arulzkash
- @harismln22
- @ridhonaufaldyy
- Muhamad Irfan
