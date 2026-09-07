# Health_CoRisk_Analyzer

## Project Overview

Health_CoRisk_Analyzer investigates how clinical and lifestyle factors relate to heart attack risk and mortality risk in a patient dataset. The main focus is on understanding whether variables such as BMI, smoking status, blood pressure, family history, diabetes, medication adherence, and physical activity are associated with higher risk levels.

This project uses Python, pandas, numpy, matplotlib, and seaborn to perform ETL-style cleaning, feature engineering, and exploratory visual analysis. The output is a structured notebook-based workflow that is easy to follow and suitable for both technical and non-technical audiences.

## Data App and Dashboard Requirement

This project is designed as a data app and dashboard prototype in addition to a notebook-based analysis. The goal is to combine data analysis, visualisation, and a user-friendly interface so users can explore risk patterns quickly and make evidence-based decisions.

The business requirement is to provide a fast analytics prototype that supports operational and clinical understanding of cardiovascular risk. In a professional environment, the value of the system is not only in producing charts but in helping stakeholders answer practical questions such as:

- Which patient groups show the highest heart attack risk?
- How do smoking status, blood pressure, BMI, and adherence behaviour relate to risk outcomes?
- Which risk factors deserve priority for interventions or monitoring?

The UI is therefore built around a simple decision-support workflow: data exploration, filtering, visual interpretation, and summary insight generation. The analysis is aligned with the business objective of identifying high-risk patterns that could inform prevention strategies, patient education, and service planning.

This means the project reflects the professional expectation that data analysis and dashboard design must be driven by business context, not only technical output. The UI and underlying analysis are therefore linked to real organisational questions and designed to support rapid insight generation for stakeholders with different levels of technical expertise.

## Dataset

The project uses the dataset:

- Patient Comorbidity Risk Assessment Dataset
- Source: Kaggle
- Link: https://www.kaggle.com/datasets/velvetcrystal/patient-comorbidity-risk-assessment-dataset
- File: `Datasets/Patient_Comorbidity_Risk_Assessment_Dataset.csv`

The dataset includes patient-level information related to comorbidities, lifestyle behaviour, and risk indicators such as BMI, smoking status, blood pressure, family history, physical activity, diabetes, medication adherence, and predicted risk percentages.

## Business and Analytical Objective

The aim of the project is to evaluate patient risk factors in a way that supports understanding of cardiovascular health risk. The analysis tests whether common clinical variables are associated with higher heart attack and mortality risk.

Key hypotheses explored:

- Higher BMI is associated with higher `Heart_Attack_Risk_Percentage`.
- Positive `Family_History_CVD` is associated with higher `Heart_Attack_Risk_Percentage`.
- High BMI and family history together show a higher risk than either factor alone.
- Current smoking is associated with higher `Heart_Attack_Risk_Percentage`.
- High `Systolic_BP` (>= 140) is associated with higher `Mortality_Risk_Percentage`.
- Low physical activity is associated with higher heart attack and mortality risk.
- `Diabetes` is associated with higher `Mortality_Risk_Percentage`.
- Low medication adherence is associated with higher `Mortality_Risk_Percentage`.

## Project Goals

This project aims to:

- clean and validate a health dataset
- create meaningful features for risk analysis
- explore group differences in heart attack and mortality risk
- communicate findings clearly through narrative and visualisation
- reflect on ethical, privacy, and governance issues in healthcare data analysis

## Methodology

### Data preparation

The notebook workflow includes:

- importing the dataset
- reviewing the dataset shape, columns, and dtypes
- checking for missing or invalid values
- converting numeric columns to suitable types
- filling missing values using robust statistics such as medians
- creating derived variables for analysis

### Feature engineering

New variables were created to support the hypothesis testing, including:

- `BMI_Category`
- `Obesity_Flag`
- `Obesity_x_FH`
- `Smoking_current`
- `SBP_high`
- `Low_Adherence`
- `comorbidity_count`

These engineered columns make the data easier to compare across categories and improve the clarity of the analysis.

### Analysis techniques

The project uses:

- summary statistics
- grouped averages
- bar charts, boxplots, and violin plots
- feature engineering for risk comparison
- narrative interpretation of results

### Machine-learning comparison

The project also includes a separate exploratory machine-learning notebook:
`jupyter_notebooks/Health_Co_Risk_ML_Comparison.ipynb`.

This notebook compares three classification algorithms:

- Logistic Regression
- Decision Tree
- Random Forest

The workflow uses `train_test_split`, preprocessing pipelines, model `.fit()` training, `.predict()` predictions, and evaluation with accuracy, precision, recall, F1-score, and ROC-AUC. It also includes performance charts, confusion matrices, and ROC curves.

Because the source dataset provides a continuous `Heart_Attack_Risk_Percentage`, the notebook creates an exploratory `High_Heart_Attack_Risk` classification target using the dataset median as the cutoff. The supplied heart-attack and mortality risk columns are excluded from the model features to reduce target leakage.

The algorithm with the strongest F1-score is identified as the best exploratory model because F1-score balances precision and recall when identifying higher-risk records. The result is not treated as a clinical recommendation: model performance requires external validation, and the target threshold is a project decision rather than a clinically approved definition.

The ML notebook is intentionally independent of `app.py`. It does not change the dashboard, its filters, KPI cards, charts, or runtime behaviour. This keeps the existing business-facing app stable while providing a documented modelling comparison for further analysis.

## Learning Outcomes and Pass Criteria Mapping

### Understand ethical considerations, data privacy, and governance in data analytics practices

Criteria:
- 1.1 Examine ethical issues, data privacy, and governance in the project's methodology.
- 1.2 Evaluate the legal and social implications of data handling and justify approaches that promote responsible and compliant practice.

Evidence in this project:

1.1 Ethical issues, data privacy, and governance are addressed through careful handling of the health dataset. The project uses a public research dataset, limits analysis to aggregated patterns, and avoids identifying or exposing individual patients. Bias and fairness are acknowledged by treating the findings as population-level observations rather than individual diagnoses. The methodology documents the cleaning and feature engineering steps transparently so ethical decisions are visible and reproducible.

1.2 The project responds to legal and social implications by following responsible data handling practices consistent with GDPR principles, including data minimisation, secure local processing, restricted use of personally sensitive information, and transparent documentation of the source data and analytical workflow. Social implications are also considered by recognising that health-data findings can influence public perception and policy, so the project presents findings as evidence-based risk patterns rather than value judgments about individuals or groups.

Supporting information implemented in the project:
- privacy and fairness are discussed in the project narrative
- the dataset is treated as a public aggregate research source rather than personal health records
- the README and notebook explain that findings are general risk associations and not individual medical predictions

### complex data insights to audiences

Criteria:
- 2.1 Clarify complex data insights and present them in a way that is accessible to both technical and non-technical audiences.
- 2.2 Demonstrate the use of appropriate visualisations and narratives to enhance user understanding.
- 2.3 Collate and organise project documentation using a structured approach to ensure clarity and accessibility.

Evidence in this project:

2.1 The results are communicated in a way that is understandable to both technical and non-technical audiences. Technical detail is preserved through grouped summaries, statistical comparisons, and feature engineering steps, while plain English explanations ensure that the broader meaning of the findings is easy to interpret. This is especially important for health-risk insights where the audience may include clinicians, analysts, and non-specialist stakeholders.

2.2 The project uses a combination of visualisations and narrative guidance to support understanding. Bar charts compare risk by category, boxplots show threshold-based differences, and violin plots illustrate distribution patterns. The notebook and README include explanatory text alongside plots so the audience can understand not only the numbers but also why they matter.

2.3 The project documentation is structured logically and consistently. It contains a clear introduction, dataset overview, methodology, feature engineering, findings, ethical governance discussion, and project reflection. This organisation makes the project easy to navigate and ensures clarity for assessments and future review.

Supporting information implemented in the project:
- visualisations are labelled clearly and matched to plain-language explanations
- the README explains how the analysis is designed to communicate insights to different audiences
- documentation is structured to improve accessibility and maintainability

### Review and refine data analytics project plans

Criteria:
- 3.1 Collate and present a complete project plan, including implementation, maintenance, updates, and evaluation phases.
- 3.2 Reflect on the practical challenges and considerations in executing the project.

Evidence in this project:

3.1 A complete project plan is included in the README and covers the full lifecycle of the analysis. The project moved through scoping, data acquisition, preparation, feature engineering, exploratory analysis, communication, update planning, and evaluation. This demonstrates the ability to plan and review a complete data analytics workflow rather than stopping at the initial analysis stage.

3.2 The project includes reflective discussion on practical challenges. These include missing values, data cleaning requirements, interpretation of health factors, the need for clear visual communication, and the importance of fair interpretation. These reflections show the practical realities of executing a data project and the need to revise and improve the analysis as issues are identified.

Supporting information implemented in the project:
- the README includes a project plan with implementation, maintenance, update, and evaluation phases
- a reflection section explains the main challenges encountered and the lessons learned
- future improvements and review points are documented to show continuous project development

## Project Plan

1. Define scope and objective
   - identify the research question and the health factors to analyse
   - confirm the project aim and expected outputs

2. Data collection and review
   - source the dataset from Kaggle
   - review structure, columns, and relevance to the research question

3. Data cleaning and preparation
   - handle missing values and convert columns to suitable data types
   - prepare a reliable dataset for analysis

4. Feature engineering and exploratory analysis
   - build derived variables such as BMI category and treatment adherence flags
   - compare risk groups using descriptive analysis and visualisation

5. Interpretation and communication
   - summarise patterns in clear language
   - explain what the charts show and how they support the hypotheses

6. Maintenance and updates
   - re-run analysis after data corrections or additional records are added
   - update code comments and documentation when findings evolve

7. Evaluation and improvement
   - review the project against the objectives
   - identify limitations and potential future enhancements

## Reflection on Project Challenges

This project involved several practical challenges:

- data quality issues, including missing values and inconsistent fields
- the need for careful cleaning so that comparisons were meaningful
- translating medical terms into simple explanatory language for non-technical readers
- balancing technical analysis with ethical responsibility and avoidable bias

These challenges were addressed through methodical cleaning, careful interpretation, and clear documentation, which supports a stronger and more defensible final project.

## Key Findings

The analysis suggests that the following variables are associated with higher risk levels:

- higher BMI
- positive family history of cardiovascular disease
- current smoking status
- elevated systolic blood pressure
- lower physical activity
- diabetes presence
- low medication adherence

The notebook shows these relationships through visual comparisons and grouped summaries. The results are intended to support understanding of risk patterns in the dataset rather than to provide individual medical advice.

## Communication Strategy for Different Audiences

To satisfy the requirement to present insights clearly to both technical and non-technical audiences, the project uses a blended communication approach:

- technical readers can view grouped summaries, data engineering steps, and visual comparisons
- non-technical readers can follow the charts, titles, explanations, and summary findings written in plain language
- the notebook and README combine analytical detail with accessible narrative

This ensures that the project remains understandable without losing analytical credibility.

## Project Structure

- `Datasets/` — source data
- `jupyter_notebooks/` — notebooks containing ETL, EDA, visualisation, and ML comparison
- `README.md` — project overview, methodology, ethics, governance, and plan
- `requirements.txt` — project dependencies

## Data App and Dashboard Requirement

The project is designed as both a notebook-based analysis and a business-facing data app named Health_CoRisk_Analyzer. The goal is to combine data analysis, data visualisation, and an interactive user interface so users can explore risk patterns quickly and make evidence-based recommendations.

In a professional business environment, the value of the system is not only in producing charts, but in helping stakeholders answer practical questions such as:

- Which patient groups show the highest heart attack risk?
- How do smoking status, blood pressure, BMI, and medication adherence relate to mortality risk?
- Which risk factors should be prioritised for intervention or monitoring?

The UI and the analysis are therefore aligned with organisational requirements and designed for rapid insight generation. The dashboard supports technical users with detailed metrics and non-technical users with simplified summaries and clear visual storytelling.

## Setup and Run Instructions

1. Open the project folder in VS Code.
2. Create a virtual environment if needed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the dashboard app:

```bash
streamlit run app.py
```

5. Open `jupyter_notebooks/Health_Co_Risk_analyzer.ipynb` and run the cells in sequence to review the full exploratory analysis.
6. Open `jupyter_notebooks/Health_Co_Risk_ML_Comparison.ipynb` and run the cells in sequence to compare the three exploratory ML algorithms.

## Kanban project dashboard

Kanban project dashboard is used for the developement of the project. 
the following is the link for it
https://github.com/users/ghargelg-code26/projects/3

### Heroku 
### App Information:

* App Name         health-co-risk-analyzer
* App Link(Domain) https://health-co-risk-analyzer-91efeef89f7c.herokuapp.com/    
* Region           United States
* Stack            heroku-24
* Frameworks       Python(version 3.12.14)
* GitHub Repo      ghargelg-code26/Health_CoRisk_Analyzer
* Heroku Git URL   https://git.heroku.com/health-co-risk-analyzer.git
* Generation       Cedar
* Latest Version Realease : Released v5 https://health-co-risk-analyzer-91efeef89f7c.herokuapp.com/ deployed to Heroku deployed to Heroku


* The App live link is: https://smart-cart-analytics-0a5e54da0e9e.herokuapp.com/ 

* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App at the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the `.slugignore` file.

## AI and Tool Usage

AI-assisted tools were used to support the organisation of the analysis workflow, refine the notebook explanations, and improve the clarity and structure of the documentation. The final analytical work, visualisations, and interpretation were completed using Python libraries such as pandas, numpy, matplotlib, and seaborn.

## Reflection

This project demonstrates how data analysis can be used to explore real-world health questions while still maintaining ethical responsibility and clear communication. The strongest learning outcome was the combination of technical analysis with transparent interpretation. It is not enough to produce charts; a strong data project must also explain why the results matter, who the audience is, and how the work remains fair and useful.

## Conclusion

Health_CoRisk_Analyzer successfully demonstrates the value of data cleaning, feature engineering, and exploratory data analysis in understanding cardiovascular risk. The project satisfies the assessed learning outcomes by combining technical analysis with ethical awareness, governance thinking, audience-focused communication, and a structured review of the project plan.

## Credits

This project was developed as part of the Code Institute Data Analytics Capstone learning process. Support was provided through course materials, guidance, and practical exercises designed to build analytical and presentation skills.
