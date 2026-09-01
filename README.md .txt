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
