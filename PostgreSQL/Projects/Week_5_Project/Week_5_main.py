import pandas as pd


# Phase 2: Data Ingestion & Inspection

df_enrollment = pd.read_csv("C:/Users/Bernadette/Documents/GitHub/DE_bootcamp3/PostgreSQL/Projects/Week_5_Project/enrollments_dirty.csv")
df_college = pd.read_csv("C:/Users/Bernadette/Documents/GitHub/DE_bootcamp3/PostgreSQL/Projects/Week_5_Project/colleges.csv")



# Phase 3: Data Cleaning Pipeline

# 1. Fill missing values
df_enrollment["Tuition Fee"] = df_enrollment["Tuition Fee"].fillna(0)
df_enrollment["Payment Status"] = df_enrollment["Payment Status"].fillna("Unknown")

# 2. Drop rows with missing Student IDs
df_enrollment = df_enrollment.dropna(subset=["Student ID"])

# 3. Clean and standardize text formatting
df_enrollment["Student Name"] = df_enrollment["Student Name"].str.strip().str.title()
df_enrollment["Payment Status"] = df_enrollment["Payment Status"].str.strip().str.capitalize()

# 4. Enforce numeric and datetime data types
df_enrollment["Tuition Fee"] = pd.to_numeric(df_enrollment["Tuition Fee"], errors="coerce")
df_enrollment["Enrollment Date"] = pd.to_datetime(df_enrollment["Enrollment Date"], errors="coerce")
df_enrollment["Last Sync"] = pd.to_datetime(df_enrollment["Last Sync"], errors="coerce")

# 5. Sort chronologically and deduplicate
df_enrollment = df_enrollment.sort_values(by="Last Sync")
df_enrollment = df_enrollment.drop_duplicates(subset=["Registration ID"], keep="last")



# Phase 4: Transformation, Merging & Analysis

# 1. Standardize column names to snake_case
df_enrollment = df_enrollment.rename(columns={
    "Registration ID": "registration_id",
    "Student ID": "student_id",
    "Student Name": "student_name",
    "Enrollment Date": "enrollment_date",
    "Tuition Fee": "tuition_fee",
    "Payment Status": "payment_status",
    "Last Sync": "last_sync"
})

df_college = df_college.rename(columns={
    "Student ID": "student_id",
    "College Department": "college_department",
    "Campus Location": "campus_location"
})

# 2. Feature Engineering
df_enrollment["downpayment"] = df_enrollment["tuition_fee"] * 0.20
df_enrollment["enrollment_month"] = df_enrollment["enrollment_date"].dt.to_period("M")

# 3. Data Integration (Left Join)
merged = df_enrollment.merge(df_college, on="student_id", how="left", indicator=True)

# 4. Aggregation by Department
summary = merged.groupby("college_department").agg(
    total_students=("registration_id", "count"),
    total_tuition=("tuition_fee", "sum"),
    avg_tuition=("tuition_fee", "mean")
).reset_index()

print("--- Merged Clean Data Preview ---")
print(merged.head())

print("\n--- Department Summary Report ---")
print(summary)



# Phase 5: Exporting & Visualization

