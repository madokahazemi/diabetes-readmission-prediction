![banner](assets/Banner.png)


 # Key findings: Predicting hospital readmissions within 30 days is challenging, with the best model (LightGBM) achieving an Average Precision of 15.7%, but the analysis reveals that the number of previous inpatient visits, number of diagnoses, and length of hospital stay are the strongest predictors of readmission risk.

## Authors

- [@madokahazemi](https://www.github.com/madokahazemi)

## Table of Contents

  - [Business problem](#business-problem)
  - [Data source](#data-source)
  - [Methods](#methods)
  - [Tech Stack](#tech-stack)
  - [EDA](#EDA)
  - [Lessons learned and recommendation](#lessons-learned-and-recommendation)
  - [Limitation and future work](#limitation-and-future-work)
  - [Explore the notebook](#explore-the-notebook)
  - [Repository structure](#repository-structure)

## Business problem

Hospital readmissions within 30 days of discharge are a significant challenge in healthcare, leading to increased costs and potentially indicating gaps in care quality. This project aims to develop a predictive model to identify patients at high risk of readmission, enabling healthcare providers to implement targeted interventions and improve patient outcomes while optimizing resource allocation.


## Data source

- [Diabetes 130-US Hospitals for Years 1999-2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)

## Methods

- Exploratory data analysis
- Bivariate analysis
- Multivariate correlation
- Sampling:
  - SMOTE
  - Random Undersampling
  - ADASYN
  - SMOTETomek
- Model deployment:
  - Logistic Regression
  - Random Forest
  - XGBoost
  - LightGBM
  - CatBoost


## Tech Stack

- Python (refer to requirement.txt for the packages used in this project)


## EDA

Dataset overview: 
- Number of features: 50
- Number of samples: 101,766

Key features include:
- Demographic information: age, gender, race
- Medical history: number of previous visits, diagnoses, medication information
- Current visit details: time in hospital, number of lab procedures, number of medications
- Outcome variable: readmitted (target variable)

 Feature engineering:
 - Number of medication changes (Derived from 23 medication features representing changes in different medications during a patient's hospital stay. This is based on research linking medication changes to diabetic readmission rates.)


![heatmap](assets/EDA_Heatmap.png)


Top 3 models (with hypertuned parameters):

| Model     	          |  Sampler               | Average Precision 	 | Recall       	  | AUC score 	| 
|-------------------	  |------------------      |------------------	       |------------------  |------------------	|
| LightGBM              |	None	                 | 16.2% 	                   | 37.8% 	            | 64.1% 	            |
| Random Forest         |	Random undersampling   | 15.5% 	                   | 35.9% 	            | 64.3% 	            |
| Logistic Regression   |	Random undersampling    | 14.9% 	                   | 47.6% 	            | 63.6% 	            |

Model evaluation (Confusion matrix, ROC-Curve and PR-Curve of LightGBM classifier):

![Model evaluation](assets/LightGBM_evaluation.png)

Feature importance:

![Feature importance](assets/LightGBM_FeatureImportance.png)

- **The final model used for this project: LightGBM**
- **Metrics used: Average Precision**
- **Why choose Average Precision as metrics**:
Average Precision provides a comprehensive evaluation of the model's performance across all possible classification thresholds. It summarizes the precision-recall curve into a single score, effectively capturing the model's ability to identify true positives (correct readmission predictions) while considering the precision-recall trade-off. This makes Average Precision particularly suitable for our readmission prediction task, where we need to balance the identification of high-risk patients with the efficient use of healthcare resources.


  - ***Note***: There is always a trade-off between precision and recall. Choosing the right balance depends on the specific healthcare context, available resources, and the relative costs of false positives versus false negatives.
    - In a well-resourced healthcare setting, having a good recall (sensitivity) is ideal, as it ensures that most patients at risk of readmission are identified and receive additional care.
    - In a resource-constrained healthcare setting, In this case, the hospital needs to be more selective in identifying high-risk patients to ensure that limited resources are used most effectively. Having good precision (specificity) becomes more desirable, as it helps ensure that interventions are targeted at patients who are most likely to be readmitted.



## Lessons learned and recommendation

While the model's performance (with an Average Precision of about 15.7% for the best model) indicates the challenging nature of predicting readmissions, it stil provides predictive features for identifying high-risk patients.

- Recommendation:
  - Focus on patients with frequent inpatient visits and complex diagnoses.
  - Consider longer hospital stays as potential indicators of higher readmission risk.
  - Factor in patient age and number of prescribed medications when assessing risk.
  - Pay less attention to factors like gender and specific diagnosis categories, which showed less predictive power.



## Limitation and future work

Despite multiple attempts to improve model performance (including addressing class imbalance with threshold adjustments, oversampling, undersampling, and combinations of these techniques), we were unable to achieve a satisfactory PR-AUC curve. This persistent challenge likely stems from several factors:

  - Complex nature of readmissions: Hospital readmissions are influenced by a wide range of factors, many of which may not be fully captured by our current dataset or available features, limiting the predictive power of our model.
  - Temporal aspects: Our current approach may not adequately capture the time-dependent nature of patient health trajectories.
  - Class imbalance: The rarity of readmission events poses challenges for prediction.


Future work:
  - Retrain the model without the least predictive features and apply more advanced feature selection methods, such as recursive feature elimination (RFE) or LASSO regularization to potentially improve performance and reduce noise.
  - Experiment with more advanced feature engineering techniques, such as polynomial features or interaction terms.
  - Explore deep learning models, particularly recurrent neural networks (RNNs) or transformers, to capture temporal patterns in patient history.
  - Implement more sophisticated ensemble methods, such as stacking or blending multiple models.
  - Try advanced sampling techniques to better handle class imbalance.



## Explore the notebook

To explore the notebook file [here](https://github.com/madokahazemi/diabetes-readmission-prediction/blob/main/code/Prediction%20on%20Hospital%20Readmission.ipynb)




## Repository structure


```

├── assets
│   ├── Banner.png                                 <- banner image used in the README.
│   ├── EDA_heatmap.png                            <- heatmap image used in the README.
│   ├── LightGBM_evaluation.png                    <- model evaluation image used in the README.
│   ├── LightGBM_FeatureImportance.png             <- feature importance image used in the README.
│
├── data
│   ├── diabetes_data.csv                          <- the dataset with patient information.
│
│├── code
│   ├── Prediction on Hosputal Readmission.ipynb   <- main python notebook where all the analysis and modeling are done.
│
│
│├── .gitignore                                    <- used to ignore certain folder and files that won't be commit to git.
│
├── poetry.lock                                    <- detailed, pinned dependency specifications for Poetry.
│
├── pyproject.toml                                 <- configuration file for Poetry, defining project metadata and dependencies.
│
├── README.md                                      <- this readme file.
│
├── requirements.txt                               <- list of all the dependencies with their versions.


```



