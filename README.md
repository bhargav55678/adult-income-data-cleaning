---

# Week 2: Exploratory Data Analysis

## Objective

The objective of Week 2 was to explore the cleaned Adult Income dataset and understand the relationships between demographic, educational, occupational, financial, and working-related variables and income.

The analysis was performed using Python with Pandas, NumPy, Matplotlib, and Seaborn.

## Dataset Used

The cleaned dataset contains:

- 32,537 records
- 15 columns
- 6 numerical variables
- 9 categorical variables

The target variable is `income`, with two categories:

- `<=50K`
- `>50K`

## Analysis Performed

The following exploratory analyses were completed:

1. Dataset structure and descriptive statistics
2. Income distribution
3. Age distribution
4. Age group vs income
5. Education vs income
6. Occupation vs income
7. Workclass vs income
8. Marital status vs income
9. Sex vs income
10. Hours per week vs income
11. Capital gain vs income
12. Capital loss vs income
13. Numerical correlation analysis
14. Outlier analysis

## Key Findings

### Income Distribution

The dataset contains 32,537 individuals.

- `<=50K`: 24,698 individuals (75.91%)
- `>50K`: 7,839 individuals (24.09%)

This indicates that the target variable is imbalanced, with the `<=50K` category representing the majority of observations.

### Age

The average age is approximately 38.59 years, while the median age is 37 years.

The 26-35 age group contains the largest number of individuals in the dataset.

The proportion of `>50K` income generally increases through the main working-age groups and reaches 39.86% for the 46-55 group.

### Education

Education shows a noticeable relationship with income.

Higher education categories generally contain a larger proportion of individuals earning `>50K`. Doctorate, Prof-school, and Masters categories have particularly high proportions of `>50K` earners.

### Occupation

Income distribution varies significantly across occupations.

The highest proportions of `>50K` earners were observed in:

- Exec-managerial: 48.41%
- Prof-specialty: 44.92%
- Protective-serv: 32.51%
- Tech-support: 30.53%

### Workclass

Self-emp-inc has the highest proportion of `>50K` earners among the workclass categories, followed by Federal-gov.

The `?` category represents unknown workclass information and should be handled carefully during future preprocessing.

### Working Hours

The correlation between `hours-per-week` and the binary income variable is approximately 0.230.

Individuals in the `>50K` category generally show higher working-hour distributions, although there is considerable overlap between the two income groups.

### Capital Gain and Capital Loss

Capital gain is highly skewed because most observations have a value of zero.

The average capital gain is:

- `<=50K`: 148.88
- `>50K`: 4007.16

This large difference suggests that capital gain may be an informative feature for income prediction.

Capital loss is also heavily concentrated around zero.

### Correlation Analysis

Among the numerical variables, the strongest correlations with the binary income variable were:

- Education-num: 0.335
- Age: 0.234
- Hours-per-week: 0.230
- Capital-gain: 0.223
- Capital-loss: 0.151
- Fnlwgt: -0.010

These results suggest that income is influenced by multiple factors rather than a single numerical variable.

### Outlier Analysis

The IQR method was used to identify potential outliers.

For `hours-per-week`, the IQR boundaries were:

- Lower bound: 32.5
- Upper bound: 52.5

Approximately 27.67% of observations were identified as statistical outliers using this rule.

These values were not automatically removed because many may represent legitimate working patterns rather than incorrect data.

## Visualizations

Week 2 visualizations are stored in:

`screenshots/week2/`

The visualizations include:

- Income distribution
- Education vs income
- Occupation vs income
- Age group vs income
- Workclass vs income
- Marital status vs income
- Sex vs income
- Hours per week vs income
- Capital gain vs income
- Capital loss vs income
- Correlation heatmap
- Hours per week outlier analysis

## Week 2 Outcome

The exploratory analysis identified important patterns, class imbalance, skewed financial variables, unknown categorical values, and potential outliers.

These findings will be used in the next stage of the project for feature engineering, encoding, preprocessing, and preparation of the dataset for machine-learning models.



---

# Week 3 — Unsupervised Learning and Clustering

## Overview

In Week 3, unsupervised learning techniques were applied to the cleaned Adult Income dataset. The main objective was to identify groups of individuals with similar characteristics using K-Means clustering.

The clustering process was performed without using the income column as an input feature. Instead, income was analyzed after clustering to understand the characteristics of the resulting groups.

## Clustering Features

The following five numerical features were selected:

- `age`
- `education-num`
- `hours-per-week`
- `capital-gain`
- `capital-loss`

The features were standardized using `StandardScaler` before applying K-Means.

## Choosing the Number of Clusters

The Elbow Method and Silhouette Score were used to evaluate different values of K.

Silhouette scores were calculated for K values from 2 to 10 using a fixed sample of 5,000 observations.

| K | Silhouette Score |
|---|---:|
| 2 | 0.5690 |
| 3 | 0.2453 |
| 4 | 0.2589 |
| 5 | 0.2934 |
| 6 | 0.3026 |
| 7 | 0.3178 |
| 8 | 0.3275 |
| 9 | 0.3286 |
| 10 | 0.3298 |

K = 2 produced the highest silhouette score of **0.5690**, so two clusters were selected for the final K-Means model.

## Final Cluster Results

The final K-Means model divided the dataset into two clusters:

| Metric | Cluster 0 | Cluster 1 |
|---|---:|---:|
| Number of individuals | 1,484 | 31,053 |
| Percentage of dataset | 4.56% | 95.44% |
| Average age | 41.63 | 38.44 |
| Average education-number | 10.99 | 10.04 |
| Average hours per week | 43.36 | 40.30 |
| Average capital gain | 0.00 | 1,129.98 |
| Average capital loss | 1,901.71 | 0.66 |
| Income >50K | 51.95% | 22.76% |

Cluster 0 is a much smaller group but has higher average age, education-number, and working hours. It also has a substantially higher average capital loss and a higher proportion of individuals earning above 50K.

Cluster 1 contains the majority of the dataset and has a much higher average capital gain, while its average capital loss is very low.

## Income Analysis

Income was not used to create the clusters. It was analyzed afterward to understand whether the clusters showed different income patterns.

The percentage of individuals earning above 50K was:

- Cluster 0: **51.95%**
- Cluster 1: **22.76%**

This is a difference of approximately **29.19 percentage points**.

This result represents an observed association within the dataset and does not mean that cluster membership causes a particular income level.

## PCA Visualization

PCA was used to visualize the five-dimensional clustering data in two dimensions.

- PC1 explained **25.93%** of the variance.
- PC2 explained **20.60%** of the variance.
- Together, PC1 and PC2 explained **46.54%** of the total variance.

The PCA visualization provides a two-dimensional view of the cluster assignments.

## Additional Cluster Analysis

After creating the clusters, additional categorical variables were analyzed to understand their characteristics:

- Workclass
- Occupation
- Marital status
- Sex
- Income

These variables were used for post-clustering interpretation and were not used as direct K-Means input features.

## Business and Research Implications

The clustering results can be used for exploratory workforce and demographic analysis.

From a business perspective, the clusters could support workforce segmentation, targeted analysis, and further research into employment and income patterns.

From a research perspective, clustering demonstrates how groups can be discovered without requiring a predefined target variable.

The strong difference in cluster sizes is an important limitation. Cluster 1 represents 95.44% of the dataset, while Cluster 0 represents only 4.56%.

## Week 3 Deliverables

- K-Means clustering implementation
- Elbow Method analysis
- Silhouette Score analysis
- Cluster size visualization
- Cluster profile analysis
- Income distribution by cluster
- Workclass distribution by cluster
- Occupation distribution by cluster
- Marital status distribution by cluster
- Sex distribution by cluster
- PCA cluster visualization
- Week 3 analysis notebook
- Week 3 report

## Files

```text
notebooks/
└── 03_clustering_analysis.ipynb

reports/
└── week3_clustering_report.md

screenshots/
└── week3/
    ├── elbow_method.png
    ├── silhouette_scores.png
    ├── cluster_sizes.png
    ├── cluster_profile.png
    ├── income_by_cluster.png
    ├── workclass_by_cluster.png
    ├── occupation_by_cluster.png
    ├── marital_status_by_cluster.png
    ├── sex_by_cluster.png
    └── pca_clusters.png