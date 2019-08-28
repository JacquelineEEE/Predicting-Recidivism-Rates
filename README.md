# Predicting Recidivism Rates
This work is designed to support entities offering services to formerly incarcerated individuals. The dataset consists of individuals currently incarcerated in the Texas Prison System.


### Problem Statement:
Is an inmate's initial crime and their age at the time it was committed predictive of recidivism?

### Goal:
To create a model that predicts the likelihood of recidivism for an inmate in an attempt to support the efforts of any entity providing services for previously incarcerated individuals.

### Contents
**In this Repository**

| Name | Link | Description |
| ---- | ---- | ----------- |
| Slides (Aug 27, 2019) | [Link](./Slides_Aug2019.pdf) | Process, Findings, Next Steps |
| Prep Code Notebooks | [Link](./Prep_Notebooks) |Creating Functions, Scraping, etc. |
| Project Code Notebooks | [Link](./Project_Notebooks) | EDA/Cleaning/Modeling/Summary Visualizations |
| Datasets | [Link](./datasets) | Workflow from scrape, to cleaning, to feature engineering, to test set probability results. The [Propublica COMPAS datasets](https://www.propublica.org/datastore/dataset/compas-recidivism-risk-score-data-and-analysis) are also there for reference. |
| Functions | [Link](./Project_Notebooks/inmate_scrape.py) | The final functions used to scrape and save data from the [Texas Tribune Prison Main Page](https://www.texastribune.org/library/data/texas-prisons/) |

**Data Dictionaries**
<details>
<summary>Scraping/Initial CSVs</summary>
  > [Priors Scrape csv](../datasets/my_data/priors_FINAL.csv)
>  [Inmate Details csv](./datasets/my_data/inmate_details_FINAL.csv)
  > [Merged csv](./datasets/my_data/complete_raw_df.csv) | This is the complete dataset used to begin the project
>   [All Lifelines Link](./datasets/all_lifelines.csv)

| Data | Type | Description |
| --- | --- | :--- |

### Process
1. Research
2. Data Collection
3. Cleaning, Feature Engineering, & EDA
4. Model Fitting & Metrics
5. Model Selection & Application
6. Summary Statistics


## Research
I began this project by looking into available government datasets. I also found Probublica's work exposing racial bias in the COMPAS algorithm (kaggle and research/explanatory articles). This allowed me to gain access to their process,  their notebooks of work, and their datasets.

From here I considered what data I might want, and I started looking into the Huntsville State Penitentiary.

The Texas Tribune became the exclusive source of my data for this project. Through this website I learned I could access all prisons in the Texas System and each current inmate.

## Data Collection
> Beautiful Soup | Amazon Web Services

This part of the project took an extensive amount of time and offered a great deal of learning opportunity. Creating effective, efficient, and intentional functions to scrape the data needed was a days-long process of trial and error.

#### Highlights of learning:
- the invaluable nature of `try/except` statements
- automating `saving to a .csv` routinely within the function
  -- building out a shell of the notebook from a partial .csv while the scrape is running
- ensuring the same `unique identifier` for each observation is in all datasets intended to be merged (ie: names of individuals is not sufficient, a qualifying id or url tag is essential)
- the scrape can take days (and days and days)

#### Final Counts:
- `56,600` unique inmate basic detail observations
- `47,500` unique inmate prior detail observations
- merged dataset with `47,500 unique inmates`

## Cleaning, Feature Engineering, & EDA
