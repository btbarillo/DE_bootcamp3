from pathlib import Path
import numpy as np
import pandas as pd

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

ENROLLMENTS_PATH = RAW_DIR / "enrollments_dirty.csv"
COLLEGES_PATH = RAW_DIR / "colleges.csv"

np.random.seed(42)

n = 40


student_names = [
    "  juan dela cruz ",
    "MARIA CLARA SANTOS",
    "jose rizal ",
    "Ana Reyes",
    "  benjamin cruz ",
    "KATRINA GONZALES",
    "gabriel mendoza ",
    " Sofia Bautista ",
]


enrollments_data = {
    "Registration ID": [
        i if i != 105 else 104 for i in range(101, 101 + n)
    ],  
    "Student ID": [
        f"S{np.random.randint(202600, 202610)}" if i not in [3, 15] else np.nan
        for i in range(n)
    ],
    "Student Name": [np.random.choice(student_names) for _ in range(n)],
    "Enrollment Date": [
        "2026-06-10",
        "2026-06-12",
        "invalid-date",
        "2026-06-15",
        "2026-06-20",
        "2026-07-01",
        "2026-07-05",
        "2026-07-10",
        "2026-07-12",
        "2026-07-15",
    ]
    * 4,
    "Tuition Fee": [
        round(x, 2) if i != 8 else np.nan
        for i, x in enumerate(np.random.uniform(25000.0, 65000.0, n))
    ],
    "Payment Status": np.random.choice(
        [" PAID ", "pending", "Paid", "CANCELLED", "paid", np.nan], n
    ),
    "Last Sync": pd.date_range("2026-06-01 08:00", periods=n, freq="D").astype(
        str
    ),
}

df_enrollments = pd.DataFrame(enrollments_data)
df_enrollments.to_csv(ENROLLMENTS_PATH, index=False)


colleges_data = {
    "Student ID": [f"S{i}" for i in range(202600, 202610)],
    "College Department": [
        "College of Engineering",
        "College of Business Administration",
        "College of Computer Studies",
        "College of Arts and Sciences",
        "College of Nursing",
        "College of Education",
        "College of Architecture",
        "College of Pharmacy",
        "College of Accountancy",
        "College of Fine Arts",
    ],
    "Campus Location": [
        "Manila Campus",
        "Quezon City Campus",
        "Makati Campus",
        "Cebu Campus",
        "Manila Campus",
        "Quezon City Campus",
        "Manila Campus",
        "Makati Campus",
        "Manila Campus",
        "Quezon City Campus",
    ],
}

df_colleges = pd.DataFrame(colleges_data)
df_colleges.to_csv(COLLEGES_PATH, index=False)

print(
    f"Successfully generated '{ENROLLMENTS_PATH}' (40 rows) and '{COLLEGES_PATH}'!"
)