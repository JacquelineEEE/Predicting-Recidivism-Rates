# Predicting Recidivism Rates
This work is designed to support entities offering services to formerly incarcerated individuals. The dataset consists of individuals currently incarcerated in the Texas Prison System.


### Problem Statement:
Is an inmate's initial crime and their age at the time it was committed predictive of recidivism?

### Goal:
To create a model that predicts the likelihood of recidivism for an inmate in an attempt to support the efforts of any entity providing services for previously incarcerated individuals.


### Contents
**In this Repository**

| Name | Link | Description |
| ---- | ---- | :---------- |
| Slides (Aug 27, 2019) | [Link](./Slides_Aug2019.pdf) | Process, Findings, Next Steps |
| Prep Code Notebooks | [Link](./Prep_Notebooks) |Creating Functions, Scraping, etc. |
| Project Code Notebooks | [Link](./Project_Notebooks) | EDA/Cleaning/Modeling/Summary Visualizations |
| Datasets | [Link](./datasets) | Workflow from scrape, to cleaning, to feature engineering, to test set probability results. The [Propublica COMPAS datasets](https://www.propublica.org/datastore/dataset/compas-recidivism-risk-score-data-and-analysis) are also there for reference. |
| Functions | [Link](./Project_Notebooks/inmate_scrape.py) | The final functions used to scrape and save data from the [Texas Tribune Prison Main Page](https://www.texastribune.org/library/data/texas-prisons/) |



**Data Dictionaries**

Data Summary:
- `40,214` unique inmates incarcerated in a Texas prison as of 8-23-2019
- `101` of the 108 total Texas prison facilities represented
- each individual's current offense, and up to three additional priors
- basic inmate identification s/a: home county, DOB, race, sex, & age

<details>
<summary> Scraping/Initial Datasets </summary>

>  [Priors csv](./datasets/my_data/priors_FINAL.csv)

>  [Inmate Details csv](./datasets/my_data/inmate_details_FINAL.csv)

>  [Merged csv](./datasets/my_data/complete_raw_df.csv)


**Priors csv**

All inmates have a `pr_crime_0`, which is their current offense. Some inmates have additional priors, and these are identified as pr_crime_1, pr_crime_2, and pr_crime_3. If an inmate does not have any or all of these priors, these cells for that inmate are filled with `'No_data'`. Connected to each offense is `pr_commit_date`, `pr_term`, and `pr_begins`. Below each of these is listed only once. However, each inmate could have information in some or all of these. Pr_crime_3 is their oldest prior, whereas pr_crime_1 is their most recent. This information was scraped from the [Texas Tribune](https://www.texastribune.org/library/data/texas-prisons/units).

| Data | Type | Description |
| --- | --- | :--- |
| name | string | inmate's name |
| TDCJ_ID | int | unique identification number for each inmate |
| pr_crime_0 | string | current offense; `pr_crime_1`, `_2`, `_3` also present |
| pr_commit_date_0 | string | the date this offense was committed; `pr_commit_date_1`, `_2`, `_3` also present |
| pr_term_0 | string | the length of time of the sentence; `pr_term_1`, `_2`, `_3` also present |
| pr_begins_0 | string | the first day of the sentence; `pr_begins_1`, `_2`, `_3` also present  |


**Inmate Details csv**

This is the personal information of each inmate.

| Data | Type | Description |
| --- | --- | :--- |
| name | string | inmate's name |
| sex | string | 'Male', 'Female' |
| race | string | each inmate's race |
| age | int | current age |
| max_sentence | string | each inmate's maximum sentence|
| prison_unit | string | the prison they are located |
| DOB | string | each inmate's date of birth |
| home_county | string | each inmate's home county |
| TDCJ_ID | int | unique identification number for each inmate |
| proj_release_date | string | an inmate's projected release date |

</details>

<details>
<summary> Model Ready Dataset </summary>

>  [Model Ready Dataset](./datasets/my_data/complete_model_ready.csv)

**Model Ready Dataset**

This is the `cleaned dataset` with features ready to be trained. Steps that were taken are explained below in the `process section` of the README. These features have been added to the original dataset, and the descriptions below address added or altered features exclusively.

17 types of crimes were categorized and made into dummy variables. The remaining crimes were distributed in a category called `other_crime`. Only one is represented in the dictionary below. Details about the categories are discussed in the `process` section of the README. Additionally, `101 prisons` were represented in the final dataset, and dummy variables were created. The base variable name is used to represent all below. `Ages` and `terms` were converted to floats and binned to be able to check each within the model. For both, the floats were used as features.

| Data | Type | Description |
| --- | --- | :--- |
| feature_crime | string | the inmate's initial offense (up to three priors) |
| feature_startdate | datetime | when the sentence of the initial offense began |
| feature_term | string | the years, months, and days of the inmate's term |
| feature_commit_date | datetime | the date the offense was committed |
| target_value | mixed | if there is a re-offense, the crime itself; if no re-offense, the int 0|
| final_target | int | the y-value; ``{1: reoffend, 0: no re-offense}``|
| theft_crime | int | ``{1: theft related crime, 0: not}`` |
| prison_unit_ | int | ``{1: at this prison, 0: not}`` |
| commit_age | float | the age of each inmate at the time the feature crime occurred |
| feature_term_flt | float | the years, months, and days of each inmate's term in a numerical float |
| term_binned_ | int | ``{1: remaining term in that range, 0: not}``; in years: `Less than 1`, `1_to_5`, `11_15`, `16_20`, `21_30`, `31_40`, `40+` |
| age_binned_ | int | ``{1: age in that range, 0: not}``; `Under 18`, `18 to 30`, `31 to 40`, `41 to 50`, `51 to 60`, `61 to 70`, `Above 70` |

</details>

## Process
**1. Research**

**2. Data Collection**

**3. Cleaning, Feature Engineering, & EDA**

**4. Model Fitting & Metrics**

**5. Model Selection & Application**

**6. Summary Statistics**

## Process Details:
### Step 1: Research
> What data do I want?

> What data is available?

> What can I actually obtain?

<details>
<summary> Research Details </summary>

I began this project by looking into available government datasets. I also found Probublica's work exposing racial bias in the COMPAS algorithm (kaggle and research/explanatory articles). This allowed me to gain access to their process,  their notebooks of work, and their datasets.

From here I considered what data I might want, and I started looking into the Huntsville State Penitentiary.

The Texas Tribune became the exclusive source of my data for this project. Through this website I learned I could access all prisons in the Texas System and each current inmate.

</details>

### Step 2: Data Collection
> Now that I found it, how in the world am I going to get it?

<details>
<summary> Data Collection Details </summary>

- Beautiful Soup
- Amazon Web Services

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

#### Limitations of the Data:
- Only scraped the 4 most recent crimes, rather than all, so some inmates `feature_crime` was not their actual initial crime (this was a choice I made based on my limitations of time, it is absolutely possible to acquire all priors for each inmate).
- Only current inmates are represented in the dataset, this is missing individuals previously incarcerated that have not reoffended. These individuals would enhance the model.
- There are many types of facilities represented in the Texas Tribune database (`State Jail`, `Prison`, `Work Program`, `Transfer Facility`). The non-prison units are not filtered out of this dataset.
- No additional inmate information was acquired (ie: education, occupation, family information, etc).

</details>

### Step 3: Cleaning, Feature Engineering, & EDA
> What do I need?

> What can I actually do?

> How can I make this happen?

<details>
<summary> Cleaning, Feature Engineering, & EDA Details </summary>

Almost all of the data had to be manipulated or converted from its original form in order to explore or be used to model. These are some of the highlights.

#### Term Lengths:
This was a new challenge for me, because it was the first time there was inconsistency in the structure of the strings.
This is a sample of what some of the unique terms, as strings, were:

![Unique Terms](./images/unique_terms.pdf)


![Unique Terms](./images/unique_terms.pdf)


</details>
