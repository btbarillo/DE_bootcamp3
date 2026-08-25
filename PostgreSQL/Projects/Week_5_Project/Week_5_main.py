import pandas as pd

# Step 2: Ingestion & Inspection
df_enrollment = pd.read_csv("C:/Users/Bernadette/Documents/GitHub/DE_bootcamp3/PostgreSQL/Projects/Week_5_Project/enrollments_dirty.csv")
print(df_enrollment)

df_college = pd.read_csv("C:/Users/Bernadette/Documents/GitHub/DE_bootcamp3/PostgreSQL/Projects/Week_5_Project/colleges.csv")
print(df_college)

# Step 3: Data Cleaning
df_enrollment["Tuition Fee"] = df_enrollment["Tuition Fee"].fillna(0)
df_enrollment["Payment Status"] = df_enrollment["Payment Status"].fillna("Unknown")
df_enrollment = df_enrollment.dropna(subset=["Student ID"])

# Text formatting
df_enrollment["Student Name"] = df_enrollment["Student Name"].str.strip().str.title()
df_enrollment["Payment Status"] = df_enrollment["Payment Status"].str.strip().str.capitalize()

# Type conversion
df_enrollment["Tuition Fee"] = pd.to_numeric(df_enrollment["Tuition Fee"], errors="coerce")
df_enrollment["Enrollment Date"] = pd.to_datetime(df_enrollment["Enrollment Date"], errors="coerce")
df_enrollment["Last Sync"] = pd.to_datetime(df_enrollment["Last Sync"], errors="coerce")

# Sorting and deduplication
df_enrollment = df_enrollment.sort_values(by="Last Sync")
df_enrollment = df_enrollment.drop_duplicates(subset=["Registration ID"], keep="last")

print(df_enrollment)