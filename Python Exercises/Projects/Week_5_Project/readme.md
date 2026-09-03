# PH University Student Enrollment Data Pipeline

An automated end-to-end Python data engineering pipeline built with Pandas and Matplotlib. 

## 🎯 Primary Objective
The main goal of this pipeline is to analyze university student enrollment records in the Philippines to **determine which college department generates the highest total tuition revenue**, while calculating key enrollment metrics and automating raw data cleaning.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **Libraries:** `pandas`, `matplotlib`

To install the required dependencies, run:

```bash
pip install pandas matplotlib

## Repository Structure
.
├── enrollments_dirty.csv     # Raw, uncleaned enrollment records
├── colleges.csv              # Lookup table mapping students to college departments
├── main.py                   # Master ETL and data processing script
├── enrollments_clean.csv     # Cleaned, merged, and transformed primary dataset
├── department_summary.csv    # Aggregated metrics (total revenue, student count, avg fee)
└── tuition_summary.png       # Bar chart visualizing tuition revenue by department
