from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


DATA_DIR = Path("data")
RAW_ENROLLMENTS = DATA_DIR / "raw" / "enrollments_dirty.csv"
RAW_COLLEGES = DATA_DIR / "raw" / "colleges.csv"

PROCESSED_DIR = DATA_DIR / "processed"
CLEAN_ENROLLMENTS = PROCESSED_DIR / "enrollments_clean.csv"
DEPARTMENT_SUMMARY = PROCESSED_DIR / "department_summary.csv"
VISUALIZATION = PROCESSED_DIR / "tuition_summary.png"


PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def clean_enrollments(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

  
    df["Tuition Fee"] = df["Tuition Fee"].fillna(0)
    df["Payment Status"] = df["Payment Status"].fillna("Unknown")


    df = df.dropna(subset=["Student ID"])
    df["Student Name"] = df["Student Name"].str.strip().str.title()
    df["Payment Status"] = (
        df["Payment Status"].str.strip().str.capitalize()
    )


    df["Tuition Fee"] = pd.to_numeric(df["Tuition Fee"], errors="coerce")
    df["Enrollment Date"] = pd.to_datetime(
        df["Enrollment Date"], errors="coerce"
    )
    df["Last Sync"] = pd.to_datetime(df["Last Sync"], errors="coerce")


    df = df.sort_values("Last Sync").drop_duplicates(
        "Registration ID", keep="last"
    )


    df = df.rename(
        columns={
            "Registration ID": "registration_id",
            "Student ID": "student_id",
            "Student Name": "student_name",
            "Enrollment Date": "enrollment_date",
            "Tuition Fee": "tuition_fee",
            "Payment Status": "payment_status",
            "Last Sync": "last_sync",
        }
    )


    df["downpayment"] = df["tuition_fee"] * 0.20
    df["enrollment_month"] = df["enrollment_date"].dt.to_period("M")

    return df


def load_and_clean_colleges(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df.rename(
        columns={
            "Student ID": "student_id",
            "College Department": "college_department",
            "Campus Location": "campus_location",
        }
    )


def summarize_departments(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("college_department")
        .agg(
            total_students=("registration_id", "count"),
            total_tuition=("tuition_fee", "sum"),
            avg_tuition=("tuition_fee", "mean"),
        )
        .reset_index()
        .sort_values("total_tuition", ascending=False)
    )


def plot_summary(df: pd.DataFrame, output_path: Path) -> None:
    ax = df.plot(
        kind="bar",
        x="college_department",
        y="total_tuition",
        legend=False,
        color="skyblue",
    )
    plt.title("PH Tuition fee summary per college department")
    plt.xlabel("College Department")
    plt.ylabel("Tuition Fee")
    plt.xticks(rotation=45, ha="right")
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


def main():
  
    enrollments = clean_enrollments(RAW_ENROLLMENTS)
    colleges = load_and_clean_colleges(RAW_COLLEGES)
    merged = enrollments.merge(colleges, on="student_id", how="left")

   
    summary = summarize_departments(merged)


    merged.to_csv(CLEAN_ENROLLMENTS, index=False)
    summary.to_csv(DEPARTMENT_SUMMARY, index=False)
    plot_summary(summary, VISUALIZATION)


    print(f"Cleaned rows: {len(merged)}")
    print("\n--- Department Summary Report ---")
    print(summary)


if __name__ == "__main__":
    main()




