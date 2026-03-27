# AI_LAB

This repository contains AI laboratory assignments for Semester 6, with code, reports, and notebooks for multiple lab exercises in machine learning, computer vision, and heuristic search.

## 📁 Workspace Overview

- `Lab 1/` — AI Assignment 1 (Classification domain)
  - `AI_Assignment_1_Task_1.ipynb`
  - `AI_Assignment_1_Task_2.ipynb`
  - `data.csv`
  - `AI Assignment 1.docx`, `AI Assignment 1.pdf`, `AI_Assignment1_LAB1.pdf`
- `Lab 2/` — AI Assignment 2 (Image classification tasks)
  - `Task_1.ipynb` through `Task_4.ipynb`
  - `Report.pdf`, `Doc-report.docx`, `AI Assignment 2 .pdf`
- `Lab_4/` — Heuristic search & scheduling (Greedy + A*)
  - `README.md` (detailed lab-specific instructions)
  - `Report.pdf`
  - `Task_A/` and `Task_B/`

> Note: Lab_3 is intentionally absent from this repository (practice assignment not uploaded).

---

## 🧩 Lab 1 (AI Assignment 1) — Supervised Classification

### Goal
Build and analyze classification models on structured tabular data (`data.csv`), demonstrate model training, evaluation metrics, and insights for two task variants.

### Key files
- `Lab 1/AI_Assignment_1_Task_1.ipynb`
  - Data loading and cleaning
  - Feature engineering and preprocessing
  - Model training (e.g., Decision Tree, Logistic Regression, KNN, SVM or similar)
  - Performance evaluation (accuracy, precision, recall, F1-score, confusion matrix)
- `Lab 1/AI_Assignment_1_Task_2.ipynb`
  - Further model experimentation
  - Hyperparameter tuning (GridSearchCV/RandomizedSearchCV)
  - Comparative analysis between models

### How to run
1. Activate your Python environment.
2. Install dependencies:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```
3. Run notebooks in Jupyter:
   ```bash
   jupyter notebook "Lab 1/AI_Assignment_1_Task_1.ipynb"
   jupyter notebook "Lab 1/AI_Assignment_1_Task_2.ipynb"
   ```

---

## 🖼️ Lab 2 (AI Assignment 2) — Image Classification

### Goal
Implement image classification workflows using one or more deep learning models; tasks cover data preprocessing, augmentation, transfer learning, and evaluation on image datasets.

### Key files
- `Lab 2/Task_1.ipynb` – dataset import, exploration, and preprocessing pipeline.
- `Lab 2/Task_2.ipynb` – model development (CNN architectures or pretrained backbones), training loop.
- `Lab 2/Task_3.ipynb` – model tuning, validation, and test set evaluation.
- `Lab 2/Task_4.ipynb` – final reporting, confusion matrix, precision/recall curves and case study.

### How to run
1. Install dependencies:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn tensorflow keras opencv-python
   ```
2. Launch Jupyter and run each task notebook.

---

## 🚀 Lab_4 — Heuristic Search Algorithms (Greedy and A*)

This lab has its own detailed instructions under `Lab_4/README.md` and includes:
- `Task_A/Code.py` (Greedy scheduling algorithm)
- `Task_B/code.py` (A* search scheduling algorithm)
- Flowchart generation via Graphviz scripts

### How to run
1. Install required packages:
   ```bash
   pip install graphviz
   ```
2. Ensure Graphviz core is installed and on PATH.
3. Run:
   ```bash
   cd "Lab_4/Task_A" && python Code.py
   cd "Lab_4/Task_B" && python code.py
   ```
4. Generate/refresh flowcharts:
   ```bash
   cd "Lab_4/Task_A/flowchart" && python flowchart.py
   cd "Lab_4/Task_B/Flowchart" && python flowchart.py
   ```

---

## 🧪 Validation and Reporting

- Each lab contains final reports (`Report.pdf`) and documentation files (`Doc-report.docx`) that describe the problem statement, methodology, result analysis, performance comparisons, and conclusion.
- Reference the corresponding PDF/DOCX in each lab folder for assignment-specific scoring criteria.

---

## ⚙️ Common Prerequisites

- Python 3.8+
- Jupyter Notebook / JupyterLab
- Libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `tensorflow`/`keras`, `opencv-python`, `graphviz`

## 📌 Notes

- Keep notebooks running in order: `Lab 1` tasks then `Lab 2` tasks then `Lab_4`
- Data files are included (e.g., `Lab 1/data.csv`); subfolders contain independent scripts and visualizations.
- Use the included reports for academic assessments and grading references.