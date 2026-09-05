from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


# ============================================================
# PATHS
# ============================================================

ROOT = Path(__file__).resolve().parent.parent
SCREENSHOTS = ROOT / "screenshots" / "week5"
OUTPUT = ROOT / "reports" / "Week5_Deep_Learning_Report.docx"

OUTPUT.parent.mkdir(parents=True, exist_ok=True)


# ============================================================
# DOCUMENT SETUP
# ============================================================

doc = Document()

section = doc.sections[0]
section.top_margin = Inches(0.7)
section.bottom_margin = Inches(0.7)
section.left_margin = Inches(0.8)
section.right_margin = Inches(0.8)

styles = doc.styles

styles["Normal"].font.name = "Calibri"
styles["Normal"].font.size = Pt(10.5)

styles["Title"].font.name = "Calibri"
styles["Title"].font.size = Pt(24)

styles["Heading 1"].font.name = "Calibri"
styles["Heading 1"].font.size = Pt(17)

styles["Heading 2"].font.name = "Calibri"
styles["Heading 2"].font.size = Pt(13)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def add_heading(text, level=1):
    doc.add_heading(text, level=level)


def add_paragraph(text="", bold_prefix=None):
    p = doc.add_paragraph()

    if bold_prefix and text.startswith(bold_prefix):
        run = p.add_run(bold_prefix)
        run.bold = True
        p.add_run(text[len(bold_prefix):])
    else:
        p.add_run(text)

    return p


def add_bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.add_run(text)
    return p


def add_code(code):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)

    run = p.add_run(code)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)

    return p


def add_image(filename, caption, width=6.2):
    path = SCREENSHOTS / filename

    if path.exists():
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        run = p.add_run()
        run.add_picture(str(path), width=Inches(width))

        cp = doc.add_paragraph()
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER

        r = cp.add_run(caption)
        r.italic = True
        r.font.size = Pt(9)
    else:
        p = doc.add_paragraph()
        r = p.add_run(f"[Figure not found: {filename}]")
        r.italic = True


def add_page_break():
    doc.add_page_break()


# ============================================================
# TITLE PAGE
# ============================================================

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

r = title.add_run("WEEK 5 REPORT")
r.bold = True
r.font.size = Pt(24)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

r = p.add_run("Deep Learning Application in Data Science")
r.bold = True
r.font.size = Pt(18)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

p.add_run(
    "\nAdult Income Classification using a Neural Network\n\n"
    "Dataset: Adult Income Dataset\n"
    "Framework: TensorFlow / Keras\n"
    "Problem Type: Binary Classification"
)

doc.add_paragraph("\n")

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run(
    "This report documents the complete deep-learning workflow, "
    "including preprocessing, neural-network design, training, "
    "evaluation, error analysis, model improvement, and comparison "
    "with the Week 4 machine-learning baseline."
)

add_page_break()


# ============================================================
# 1. INTRODUCTION
# ============================================================

add_heading("1. Introduction", 1)

add_paragraph(
    "The objective of Week 5 was to explore the fundamentals of deep "
    "learning and apply a neural network to a real-world data-science "
    "problem. The Adult Income dataset was continued from the earlier "
    "weeks of the project so that the deep-learning model could be "
    "evaluated against the traditional machine-learning approaches "
    "developed previously."
)

add_paragraph(
    "The task is to predict whether an individual earns more than "
    "$50K per year based on demographic, educational, employment, "
    "and financial attributes. A fully connected feed-forward neural "
    "network was implemented using TensorFlow and Keras."
)

add_paragraph(
    "The experiment focused not only on predictive performance but "
    "also on practical deep-learning considerations such as class "
    "imbalance, overfitting, dropout regularization, early stopping, "
    "CPU-based training, and the effect of increasing network complexity."
)


# ============================================================
# 2. PROBLEM STATEMENT
# ============================================================

add_heading("2. Problem Statement", 1)

add_paragraph(
    "The problem is formulated as a binary classification task. "
    "The target variable indicates whether an individual's income "
    "belongs to the <=50K category or the >50K category."
)

add_paragraph(
    "The goal of the neural network is therefore to learn a nonlinear "
    "relationship between the available demographic, education, "
    "employment, and financial features and the final income class."
)

add_paragraph(
    "The model is evaluated using accuracy, precision, recall, "
    "F1-score, ROC-AUC, confusion matrix, and error analysis."
)


# ============================================================
# 3. DATASET
# ============================================================

add_heading("3. Dataset Description", 1)

add_paragraph(
    "The cleaned Adult Income dataset contains 32,537 observations "
    "and 15 columns. After separating the target variable, the model "
    "uses 14 input features."
)

add_paragraph(
    "The target distribution contains 24,698 observations in the "
    "<=50K class and 7,839 observations in the >50K class. This "
    "imbalance was considered during model training."
)

add_image(
    "week5_target_distribution.png",
    "Figure 1. Distribution of the target income classes."
)


# ============================================================
# 4. DATA PREPARATION
# ============================================================

add_heading("4. Data Preparation", 1)

add_paragraph(
    "The cleaned dataset prepared during the earlier stages of the "
    "project was loaded into pandas. The income column was converted "
    "into a binary target representation, where 0 represents <=50K "
    "and 1 represents >50K."
)

add_paragraph(
    "The input variables consisted of six numerical features and "
    "eight categorical features."
)

add_paragraph(
    "Numerical features included age, fnlwgt, education-num, "
    "capital-gain, capital-loss, and hours-per-week."
)

add_paragraph(
    "Categorical features included workclass, education, "
    "marital-status, occupation, relationship, race, sex, and "
    "native-country."
)

add_paragraph(
    "Categorical variables were encoded numerically and numerical "
    "variables were scaled before being supplied to the neural network."
)

add_code(
'''import pandas as pd
import numpy as np

df = pd.read_csv("../data/processed/adult_cleaned.csv")

X = df.drop("income", axis=1)
y = df["income"]

print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print(y.value_counts())'''
)


# ============================================================
# 5. TRAINING / VALIDATION / TEST
# ============================================================

add_heading("5. Dataset Splitting", 1)

add_paragraph(
    "The dataset was divided into training, validation, and test "
    "sets. The training set was used to learn the neural-network "
    "parameters, the validation set was used to monitor performance "
    "during training, and the test set was reserved for the final "
    "evaluation."
)

add_paragraph(
    "Using a separate validation set allowed training behaviour to "
    "be monitored without repeatedly evaluating the final test set."
)


# ============================================================
# 6. NETWORK ARCHITECTURE
# ============================================================

add_heading("6. Neural Network Architecture", 1)

add_paragraph(
    "A compact fully connected neural network was selected because "
    "the Adult Income dataset is structured tabular data rather than "
    "image, audio, or sequential data."
)

add_paragraph(
    "The final baseline architecture contains an input representation "
    "for 14 features, followed by a Dense layer containing 64 neurons "
    "with ReLU activation, a 30% dropout layer, a Dense layer with "
    "32 neurons using ReLU activation, a 20% dropout layer, and a "
    "single sigmoid output neuron."
)

add_paragraph(
    "The network contains 27,269 total parameters, of which 9,089 "
    "are trainable."
)

add_image(
    "week5_neural_network_architecture.png",
    "Figure 2. Final baseline neural-network architecture."
)

add_code(
'''model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dropout(0.30),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dropout(0.20),
    tf.keras.layers.Dense(1, activation="sigmoid")
])'''
)


# ============================================================
# 7. TRAINING DESIGN
# ============================================================

add_heading("7. Model Compilation and Training", 1)

add_paragraph(
    "The network was compiled using the Adam optimizer and binary "
    "cross-entropy loss because the task is binary classification. "
    "Accuracy, precision, and recall were monitored during training."
)

add_paragraph(
    "Class weights were incorporated to reduce the effect of the "
    "imbalance between the majority <=50K class and the minority "
    ">50K class."
)

add_paragraph(
    "Early stopping was used during training. Training was allowed "
    "to continue for up to 30 epochs, but the model stopped at epoch "
    "15 after validation performance stopped improving. The weights "
    "from the best validation epoch were restored, with epoch 10 "
    "providing the best validation performance."
)

add_code(
'''model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=[
        "accuracy",
        tf.keras.metrics.Precision(),
        tf.keras.metrics.Recall()
    ]
)

early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)'''
)


# ============================================================
# 8. TRAINING CURVES
# ============================================================

add_heading("8. Training and Validation Performance", 1)

add_image(
    "week5_training_validation_accuracy.png",
    "Figure 3. Training versus validation accuracy across epochs."
)

add_paragraph(
    "The training accuracy increased from approximately 76.33% in "
    "the first epoch to around 81.58% by epoch 15. Validation accuracy "
    "fluctuated during training and reached approximately 81.66% at "
    "epoch 10, which was selected as the best validation point."
)

add_image(
    "week5_training_validation_loss.png",
    "Figure 4. Training versus validation loss across epochs."
)

add_paragraph(
    "Training loss decreased substantially during the first few epochs "
    "and continued to decline gradually. Validation loss fluctuated "
    "around the later epochs, which supported the use of early stopping "
    "to avoid unnecessary training."
)


# ============================================================
# 9. TEST PERFORMANCE
# ============================================================

add_heading("9. Test Set Evaluation", 1)

add_paragraph(
    "The final baseline neural network was evaluated on 4,881 unseen "
    "test observations."
)

table = doc.add_table(rows=1, cols=2)
table.style = "Table Grid"

hdr = table.rows[0].cells
hdr[0].text = "Metric"
hdr[1].text = "Score"

metrics = [
    ("Accuracy", "0.8275"),
    ("Precision", "0.6023"),
    ("Recall", "0.8359"),
    ("F1-Score", "0.7001"),
    ("ROC-AUC", "0.9135"),
]

for metric, score in metrics:
    row = table.add_row().cells
    row[0].text = metric
    row[1].text = score

add_paragraph(
    "The model achieved 82.75% accuracy and a ROC-AUC of 91.35%. "
    "The recall of 83.59% for the positive income class shows that "
    "the class-weighted training strategy helped the model identify "
    "a large proportion of >50K observations."
)


# ============================================================
# 10. CONFUSION MATRIX
# ============================================================

add_heading("10. Confusion Matrix", 1)

add_image(
    "week5_confusion_matrix.png",
    "Figure 5. Confusion matrix for the baseline neural network."
)

add_paragraph(
    "The confusion matrix contains 3,056 correctly classified <=50K "
    "observations and 983 correctly classified >50K observations. "
    "There were 649 false positives and 193 false negatives."
)

add_paragraph(
    "The relatively small number of false negatives is consistent "
    "with the model's high recall of 83.59% for the >50K class."
)


# ============================================================
# 11. ROC CURVE
# ============================================================

add_heading("11. ROC Curve and AUC", 1)

add_image(
    "week5_roc_curve.png",
    "Figure 6. ROC curve of the baseline neural network."
)

add_paragraph(
    "The neural network achieved a ROC-AUC of 0.9135. This indicates "
    "strong ability to distinguish between the two income classes "
    "across different classification thresholds."
)


# ============================================================
# 12. ERROR ANALYSIS
# ============================================================

add_heading("12. Error Analysis", 1)

add_image(
    "week5_error_analysis.png",
    "Figure 7. Comparison of numerical feature averages for correct and incorrect predictions."
)

add_paragraph(
    "The model produced 4,039 correct predictions and 842 incorrect "
    "predictions on the test set. This corresponds to an error rate "
    "of 17.25%."
)

add_paragraph(
    "Incorrect predictions had an average age of 43.72 compared with "
    "37.77 for correct predictions. Their average education-num was "
    "10.70 compared with 9.91, while average hours-per-week was "
    "45.25 compared with 39.27."
)

add_paragraph(
    "The average capital-gain was substantially higher among correctly "
    "classified observations, at 1,270.47 compared with 350.75 among "
    "incorrect predictions. These differences indicate that some "
    "individuals have combinations of characteristics that make their "
    "income category harder for the network to distinguish."
)


# ============================================================
# 13. IMPROVED NETWORK
# ============================================================

add_heading("13. Improved Neural Network", 1)

add_paragraph(
    "An improved neural-network configuration was tested to determine "
    "whether increasing model capacity could improve minority-class "
    "performance. The experiment used a larger architecture and "
    "additional regularization."
)

add_paragraph(
    "The improved model achieved the following test performance:"
)

table = doc.add_table(rows=1, cols=2)
table.style = "Table Grid"

hdr = table.rows[0].cells
hdr[0].text = "Metric"
hdr[1].text = "Improved Model"

improved_metrics = [
    ("Accuracy", "0.8134"),
    ("Precision", "0.5735"),
    ("Recall", "0.8793"),
    ("F1-Score", "0.6942"),
    ("ROC-AUC", "0.9135"),
]

for metric, score in improved_metrics:
    row = table.add_row().cells
    row[0].text = metric
    row[1].text = score

add_image(
    "week5_nn_improvement_comparison.png",
    "Figure 8. Baseline versus improved neural-network performance."
)

add_paragraph(
    "The improved model increased recall from 83.59% to 87.93%, "
    "which means it identified more of the >50K observations. However, "
    "accuracy decreased from 82.75% to 81.34%, precision decreased "
    "from 60.23% to 57.35%, and F1-score decreased from 70.01% to "
    "69.42%."
)

add_paragraph(
    "Therefore, the increased network complexity did not provide a "
    "better overall performance profile. The baseline architecture "
    "was retained as the final model because it offered a better "
    "balance between the evaluation metrics."
)


# ============================================================
# 14. WEEK 4 COMPARISON
# ============================================================

add_heading("14. Comparison with Week 4 Machine Learning", 1)

add_image(
    "week5_model_comparison.png",
    "Figure 9. Comparison of model performance."
)

add_paragraph(
    "The Week 4 Random Forest model achieved 87.11% accuracy, "
    "82.17% precision, 59.38% recall, 68.94% F1-score, and "
    "92.30% ROC-AUC."
)

add_paragraph(
    "The Week 5 neural network achieved 82.75% accuracy, 60.23% "
    "precision, 83.59% recall, 70.01% F1-score, and 91.35% ROC-AUC."
)

comparison = doc.add_table(rows=1, cols=3)
comparison.style = "Table Grid"

hdr = comparison.rows[0].cells
hdr[0].text = "Metric"
hdr[1].text = "Random Forest"
hdr[2].text = "Neural Network"

comparison_data = [
    ("Accuracy", "87.11%", "82.75%"),
    ("Precision", "82.17%", "60.23%"),
    ("Recall", "59.38%", "83.59%"),
    ("F1-Score", "68.94%", "70.01%"),
    ("ROC-AUC", "92.30%", "91.35%"),
]

for metric, rf, nn in comparison_data:
    row = comparison.add_row().cells
    row[0].text = metric
    row[1].text = rf
    row[2].text = nn

add_paragraph(
    "The comparison demonstrates that deep learning does not "
    "automatically outperform traditional machine learning on "
    "structured tabular data. Random Forest provided substantially "
    "higher precision and accuracy, while the neural network provided "
    "much higher recall for the >50K class. The neural network also "
    "achieved a slightly higher F1-score than Random Forest."
)


# ============================================================
# 15. CHALLENGES
# ============================================================

add_heading("15. Challenges and Solutions", 1)

add_heading("15.1 Class Imbalance", 2)

add_paragraph(
    "The target contained 24,698 <=50K observations and 7,839 >50K "
    "observations. This imbalance could cause the model to favor the "
    "majority class."
)

add_paragraph(
    "Class weights were therefore used during training. This helped "
    "increase recall for the >50K class."
)

add_heading("15.2 Overfitting", 2)

add_paragraph(
    "Neural networks can memorize training patterns rather than "
    "generalizing to unseen data. Dropout layers and early stopping "
    "were used to reduce this risk."
)

add_heading("15.3 CPU-Based Training", 2)

add_paragraph(
    "The experiment was performed using CPU-based training. Since "
    "the dataset is relatively small and tabular, a compact network "
    "was sufficient and avoided unnecessary computational complexity."
)

add_heading("15.4 Model Complexity", 2)

add_paragraph(
    "Increasing the size of the network improved recall but reduced "
    "other important metrics. This demonstrated that a more complex "
    "architecture is not necessarily better for this dataset."
)


# ============================================================
# 16. LIMITATIONS
# ============================================================

add_heading("16. Limitations", 1)

limitations = [
    "The Adult Income dataset is structured tabular data, where tree-based models can be highly competitive.",
    "The model was trained using CPU resources rather than a dedicated GPU.",
    "Class weighting improved recall but reduced precision.",
    "Neural networks are less directly interpretable than tree-based feature-importance methods.",
    "The historical Adult Income dataset may not generalize directly to modern populations."
]

for item in limitations:
    add_bullet(item)


# ============================================================
# 17. FUTURE IMPROVEMENTS
# ============================================================

add_heading("17. Future Improvements", 1)

future = [
    "Perform systematic hyperparameter tuning for learning rate, batch size, dropout, and hidden-layer size.",
    "Experiment with different classification thresholds to improve the precision-recall trade-off.",
    "Investigate focal loss and other approaches for handling class imbalance.",
    "Apply SHAP or similar explainability techniques to understand individual predictions.",
    "Compare against specialized deep-learning architectures designed for tabular data.",
    "Use repeated cross-validation to obtain a more robust estimate of neural-network performance."
]

for item in future:
    add_bullet(item)


# ============================================================
# 18. KEY INSIGHTS
# ============================================================

add_heading("18. Key Insights", 1)

insights = [
    "The baseline neural network achieved 82.75% accuracy and 91.35% ROC-AUC on unseen test data.",
    "The model achieved 83.59% recall for the >50K income class.",
    "The confusion matrix contained 983 correctly identified >50K observations and 193 false negatives.",
    "The model produced 842 incorrect predictions out of 4,881 test observations, giving an error rate of 17.25%.",
    "Incorrect predictions were associated with higher average age and hours-per-week than correct predictions.",
    "The improved model increased recall to 87.93% but reduced accuracy, precision, and F1-score.",
    "Random Forest remained stronger in accuracy and precision, while the neural network provided stronger recall.",
    "The experiment demonstrates that model selection should depend on the practical objective rather than accuracy alone."
]

for item in insights:
    add_bullet(item)


# ============================================================
# 19. CONCLUSION
# ============================================================

add_heading("19. Conclusion", 1)

add_paragraph(
    "This week applied deep learning to the Adult Income classification "
    "problem using a fully connected neural network implemented with "
    "TensorFlow and Keras."
)

add_paragraph(
    "The final baseline neural network achieved 82.75% accuracy, "
    "60.23% precision, 83.59% recall, 70.01% F1-score, and 91.35% "
    "ROC-AUC on the unseen test set. The use of class weighting helped "
    "the model identify a large proportion of higher-income individuals."
)

add_paragraph(
    "An improved architecture was also tested. Although it increased "
    "recall to 87.93%, its accuracy, precision, and F1-score decreased. "
    "This showed that increasing neural-network complexity does not "
    "necessarily improve overall performance on tabular data."
)

add_paragraph(
    "The comparison with the Week 4 Random Forest model further "
    "demonstrated the importance of selecting models according to "
    "the actual problem requirements. Random Forest achieved better "
    "accuracy and precision, while the neural network provided stronger "
    "recall for the minority income class."
)

add_paragraph(
    "Overall, this experiment provided practical experience with "
    "neural-network architecture design, training, validation, "
    "regularization, class imbalance, model evaluation, error analysis, "
    "and performance comparison. It also demonstrated that deep "
    "learning is a powerful tool, but it should be applied thoughtfully "
    "rather than assuming that a neural network will always outperform "
    "traditional machine-learning techniques."
)


# ============================================================
# 20. DELIVERABLES
# ============================================================

add_heading("20. Project Deliverables", 1)

add_bullet("Week 5 deep-learning notebook: notebooks/05_deep_learning.ipynb")
add_bullet("Processed dataset: data/processed/adult_cleaned.csv")
add_bullet("Week 5 visualizations: screenshots/week5/")
add_bullet("Final report: reports/Week5_Deep_Learning_Report.docx")
add_bullet("GitHub repository: adult-income-data-cleaning")


# ============================================================
# SAVE
# ============================================================

doc.save(OUTPUT)

print()
print("==============================================")
print("Week 5 report created successfully!")
print("==============================================")
print(f"Saved to: {OUTPUT}")
print()