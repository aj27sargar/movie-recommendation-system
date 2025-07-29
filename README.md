```markdown
# 🎬 Movie Recommendation System

A **Python + Streamlit** based application that recommends similar movies based on your selection. This system uses **TMDB movie metadata** and **cosine similarity** to suggest the top 10 similar movies.

> ✅ Built as part of my **Semester 6 Machine Learning Project**.

---

## 🧠 Objective

The goal is to help users discover movies similar to ones they like using a content-based filtering approach. The app uses metadata like genre, cast, overview, and more from TMDB datasets.

---

## 🖼️ Demo Screenshot

![UI Screenshot](./Screenshot%202025-07-29%20170929.png)

---

## 🔍 Features

- 🎯 Select a movie from dropdown
- 🎥 Shows top 10 visually rich movie recommendations
- 🧠 Content-based filtering using `cosine similarity`
- 🧪 Uses TMDB 5000 dataset
- ⚡ Fast search thanks to preprocessed `.pkl` file
- 🎨 Built with an elegant Streamlit UI

---

## 📂 Project Structure

```

movie-recommendation-system/
├── app.py                    # Streamlit web app
├── movie\_data.pkl            # Serialized similarity data
├── tmdb\_5000\_movies.csv      # TMDB movie metadata
├── tmdb\_5000\_credits.csv     # TMDB movie cast/crew data
├── Movie\_Recommendation.ipynb # Notebook (EDA + preprocessing)
├── requirements.txt          # Python dependencies
├── Screenshot 2025-07-29.png # App preview
└── .gitignore

````

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit** – web UI
- **Pandas** – data wrangling
- **Scikit-learn** – similarity metrics
- **Pickle** – save/load model
- **TMDB Dataset** – movie metadata

---

## 🚀 How to Run

### 🧑‍💻 Local Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/aj27sargar/movie-recommendation-system.git
   cd movie-recommendation-system
````

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

4. **Select a movie**, hit **"Recommend"**, and enjoy suggestions!

---

## 🧪 Sample Output

For input movie **"Avatar"**, recommended movies:

* Aliens
* Alien³
* Star Trek Into Darkness
* Alien
* Planet of the Apes
* Silent Running
* Moonraker
* Gravity
* Soldier
* \[More...]

---

## 🔮 Future Scope

* 🔁 Add collaborative filtering (user ratings)
* 🌐 Integrate TMDB API for live data
* 💡 Add search box for free-text input
* 📱 Make it mobile-friendly

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE)

---

## 🙋‍♂️ Author

**Ajit Sargar**
📧 [ajitsargar@kccemsr.edu.in](mailto:ajitsargar@kccemsr.edu.in)
🔗 [GitHub](https://github.com/aj27sargar)

---

## 🙏 Acknowledgements

* [TMDB 5000 Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* [Scikit-learn](https://scikit-learn.org/)
* [Streamlit](https://streamlit.io/)

---
