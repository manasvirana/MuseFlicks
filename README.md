
---

# MuseFlicks

MuseFlicks is a sophisticated movie recommendation system that leverages various technologies and methodologies to provide personalized movie suggestions based on user preferences and content similarity.  It utilizes the Bag-of-Words (BoW) technique to process movie descriptions and enhance user experience.

## Features

### Data Preprocessing:
- Utilized the TMDB 5000 Movies dataset for initial data ingestion ([https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)).
- Applied data cleaning and transformation techniques to ensure data quality and relevance.

### Technologies Used:
- **Streamlit:** Front-end framework for building interactive web applications.
- **CSS:** Custom styling for enhancing the user interface and user experience.

### Natural Language Processing:

- Implemented **Bag-of-Words (BoW)** technique to represent movie descriptions as numerical vectors based on word frequency.
- **Stemming:** Employed to reduce words to their root forms, improving BoW representation accuracy.

## Content Similarity

### Methodology

1. **Feature Extraction:**
  - **Director Name:** Extracted from the movie metadata.
  - **Top 3 Actors:** Identified from the cast list provided in the dataset.
  - **Genres:** Categorized into predefined genres such as Action, Drama, Comedy, etc.
  - **Year of Release:** Captured to reflect temporal similarities.
  - **Plot Overviews:** Textual descriptions processed using BoW to extract key thematic elements.

2. **Similarity Calculation:**
  - **BoW Vectors:** Computed for each movie description using Bag-of-Words.
  - **Cosine Similarity:** Employed to measure similarity between movie vectors based on shared words and their frequencies.

3. **Top Similar Movies:**
  - Identified the top 5 most similar movies for each user-selected movie based on cosine similarity scores.
  - Recommendations consider director names, actors, genres, year of release, and plot summaries (extracted through BoW) to provide tailored suggestions.

### Overview

MuseFlicks is a project designed to suggest top movies based on a curated dataset. It provides users with movie recommendations along with posters, brief overviews, and Google search links for comprehensive information for each suggested film.

## External APIs

- **OMDb API:** Integrated to fetch additional movie details such as ratings, reviews, and metadata.
- **Google Search API:** Used to enhance the search functionality and gather supplementary information.

## Getting Started

To get a local copy up and running, follow these simple steps:

### Installation:

1. **Clone the repository:**
  ```bash
  git clone https://github.com/manasvirana/Museflicks.git 
  ```

2. **Navigate into the project directory:**
  ```bash
  cd Museflicks
  ```

3. **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```

### Running the Application:

1. **Launch the Streamlit app:**
  ```bash
  streamlit run app.py
  ```

2. **Access the application:**
  - Open your web browser and go to [http://localhost:8501](http://localhost:8501).



##Live Link:https://museflicks.onrender.com/

**Note: Please be aware that the free instance powering this demo may spin down due to inactivity. This could lead to initial requests experiencing delays of 50 seconds or more until the instance restarts. Thank you for your understanding



   


