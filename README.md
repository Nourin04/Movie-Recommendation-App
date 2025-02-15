

# 🎬 Movie Recommendation System  

## 📌 **Project Overview**  
The **Movie Recommendation System** suggests movies based on a selected movie using **machine learning** and **content-based filtering**. It calculates similarity scores between movies and recommends the top five most similar movies.  

The project leverages **pre-trained models**, **Google Drive-hosted data**, and the **OMDb API** for fetching movie posters. The **Streamlit framework** powers the user-friendly web application interface.

---

## 🚀 **Features**  
✅ **Content-Based Filtering:** Finds similar movies based on textual features  
✅ **Machine Learning Model:** Uses **precomputed similarity scores** for fast recommendations  
✅ **OMDb API Integration:** Fetches **high-quality movie posters** dynamically  
✅ **Interactive UI:** Built with **Streamlit** for a smooth user experience  
✅ **Cloud-Hosted Model:** Loads pre-trained data **from Google Drive** for seamless access  

---

## 🎥 **Demo**  
🚀 **[Live App](#)** _(https://movie-recommendationapp.streamlit.app/)_  

---


##  **LINK TO DATASET**  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv 

---

## 📂 **Project Structure**  

```
movie-recommendation-app/
│── 📂 src/
│   ├── app.py                # Main Streamlit application
│   ├── model.pkl             # Trained similarity model (Optional, stored in Google Drive)
│   ├── movies_list.joblib     # Movie dataset (Stored in Google Drive)
│── 📂 assets/
│   ├── logo.png              # Logo (if applicable)
│── 📜 requirements.txt        # List of required Python packages
│── 📜 README.md              # Project documentation (this file)
```

---

## 🛠️ **Installation & Setup**  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/movie-recommendation-app.git
cd movie-recommendation-app
```

### **2️⃣ Create a Virtual Environment**  
```bash
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Streamlit App**  
```bash
streamlit run app.py
```

---

## 🔗 **Dependencies**  
The project uses the following libraries:  
📌 **Streamlit** → UI framework for the web app  
📌 **Pandas** → Handling movie data  
📌 **Joblib** → Loading pre-trained models  
📌 **Requests** → Fetching posters from OMDb API  
📌 **gdown** → Downloading datasets from Google Drive  

To install all dependencies manually:  
```bash
pip install streamlit pandas joblib requests gdown
```

---

## 🏗️ **How It Works**  

### **1️⃣ Data Loading**  
- The movie dataset (`movies_list.joblib`) and similarity scores (`similarities.joblib`) are stored on **Google Drive**.  
- The app **downloads** and **loads** these files using `gdown`.  

### **2️⃣ Movie Selection**  
- Users **select a movie** from the dropdown menu.  

### **3️⃣ Finding Similar Movies**  
- The app **retrieves similarity scores** from the pre-trained model.  
- **Top 5 most similar movies** are selected.  

### **4️⃣ Fetching Posters**  
- **OMDb API** fetches high-quality **movie posters** dynamically.  

### **5️⃣ Displaying Recommendations**  
- **Movies and posters** are shown in a grid format.  

---

## 🎨 **UI Improvements**  
✔️ **Dark Theme Styling**  
✔️ **Wide Layout for Better Display**  
✔️ **CSS Animations for Posters**  
✔️ **Sidebar with App Info**  
✔️ **Custom Buttons and Icons**  

---

## 🔥 **Future Enhancements**  
🚀 **Hybrid Recommendation (Content + Collaborative Filtering)**  
🚀 **User-Based Recommendations (Personalized)**  
🚀 **Genre-Based Recommendations**  
🚀 **Deploying on Streamlit Cloud or Hugging Face Spaces**  

---

## 📧 **Contact**  
🔹 **GitHub:** [YourUsername](https://github.com/Nourin04)  
🔹 **Email:** nourinnn1823@gmail.com  

