# Solar Resource Data Analysis & Dashboard

This project analyzes and compares solar resource data (GHI, DNI, DHI, and related meteorological variables) from three West African countries: **Togo**, **Benin**, and **Sierra Leone**. It includes data cleaning, exploratory data analysis (EDA), statistical testing, and an interactive dashboard for visualizing and comparing solar metrics.

---

## Project Structure

```
solar-challenge-week1/
│
├── app/
│   ├── main.py         # Streamlit dashboard app
│   └── utils.py        # (Utility functions, if any)
│
├── data/
│   └── processed/
│       ├── benin-cleaned.csv
│       ├── togo-cleaned.csv
│       └── sierraleone-cleaned.csv
│
├── notebooks/
│   ├── benin_eda.ipynb         # EDA for Benin
│   ├── togo_eda.ipynb          # EDA for Togo
│   ├── sierraleone_eda.ipynb   # EDA for Sierra Leone
│   ├── compare_countries.ipynb # Cross-country comparison & stats
│   └── README.md
│
└── .gitignore
```

---

## Key Components

### 1. Data Preparation

- **Cleaned Datasets:**  
  Each country’s raw solar data is cleaned and saved as a CSV in `data/processed/`.
- **Cleaning Steps:**  
  - Remove or impute outliers (using Z-score or physical limits)
  - Handle missing values
  - Standardize column names and units

### 2. Exploratory Data Analysis (EDA)

- **Country-specific EDA:**  
  Each country has a dedicated notebook for in-depth analysis, including:
  - Distribution plots (histograms, boxplots)
  - Outlier detection
  - Time series and seasonal trends
  - Correlation heatmaps
  - Scatter plots (e.g., WS vs. GHI, RH vs. Tamb)

- **Cross-country Comparison:**  
  The `compare_countries.ipynb` notebook:
  - Combines all cleaned datasets
  - Produces side-by-side boxplots for GHI, DNI, DHI (colored by country)
  - Generates summary tables (mean, median, std) for each metric and country
  - Ranks countries by average GHI

### 3. Statistical Testing

- **Normality Check:**  
  Visualizes GHI distributions for each country.
- **Kruskal–Wallis Test:**  
  Non-parametric test to assess if GHI distributions differ significantly between countries.
- **Interpretation:**  
  p-values and conclusions are clearly noted in the notebook.

### 4. Interactive Dashboard

- **Streamlit App (`app/main.py`):**
  - Lets users select countries to compare
  - Displays boxplots of GHI by country
  - (Extendable: add more plots, metrics, or interactivity as needed)

---

## How to Run

## Prerequisites

Before reproducing this project, ensure you have the following installed:

- Python 3.x
- Git
- pip (Python package manager)

## Steps to Reproduce

### 1. **Clone the Repository**  
    Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Reid-T-W/solar-challenge-week1.git
    cd solar-challenge-week1
    ```

### 2. Environment Setup

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Data Preparation

- Ensure cleaned CSVs are present in `data/processed/`.
- If not, run the EDA notebooks to generate them.

### 4. Run the Dashboard

```bash
cd app
streamlit run main.py
```

### 4. Explore Notebooks

- Open any notebook in the `notebooks/` folder with Jupyter or VS Code to view or rerun the analysis.

---

## Example Outputs

- **Boxplots:** Compare GHI, DNI, DHI distributions across countries.
- **Summary Table:** Mean, median, and standard deviation for each metric and country.
- **Statistical Test Results:** p-values indicating if differences are significant.
- **Bar Chart:** Ranking countries by average GHI.

---

## Key Insights

- Togo exhibits the highest median GHI among the three countries, indicating greater solar resource potential. The median is selected over the mean as it is more robust to outliers.
- Sierra Leone shows the greatest variability in GHI, DNI, and DHI, suggesting more fluctuation in solar irradiance.
- Statistical testing (Kruskal–Wallis) confirms significant differences in GHI distributions between countries (p < 0.05), indicating their solar resource potentials are not equal.

---

## Extending the Project

- Add more interactive visualizations to the dashboard (scatter plots, time series, etc.)
- Integrate additional meteorological variables.
- Automate data cleaning and EDA for new datasets.

---

## License

This project is for educational and research purposes.

---

## Authors

- [Your Name]
- Kifiya 10 Academy, Week 1 Solar Challenge










2. **Set Up a Virtual Environment (Optional)**
    It is recommended to use a virtual environment to manage dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

