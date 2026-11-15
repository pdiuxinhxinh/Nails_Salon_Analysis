
import pandas as pd

def validate(df):
    """Validate the dataframe and raise an error if any checks fail."""

    problems = []

    def check(condition, message):
        if not condition:
            problems.append(message)

    # 1. Check required columns
    required_cols = [
        "id", "date", "start", "service_name",
        "service_type", "status", "source", "service_price"
    ]

    missing_cols = set(required_cols) - set(df.columns)
    check(not missing_cols, f"Missing columns: {sorted(missing_cols)}")

    # Stop if required columns are missing
    if missing_cols:
        raise AssertionError(
            "Validation failed:\n- " + "\n- ".join(problems)
        )

    # 2. Check personal information has been removed
    identifying_cols = {
        "name", "phone", "email", "notes",
        "client_name", "phone_number"
    }
    remaining_cols = identifying_cols & set(df.columns)

    check(
        not remaining_cols,
        f"Identifying columns still present: {sorted(remaining_cols)}"
    )

    # 3. Check missing values in important columns
    for col in ["id", "date_parsed", "start", "service_name",
                "service_type", "status", "source"]:
        check(df[col].notna().all(), f"Missing values in {col}")

    # 4. Check data types
    check(
        pd.api.types.is_datetime64_any_dtype(df["date_parsed"]),
        "date_parsed is not datetime"
    )
    check(
        pd.api.types.is_datetime64_any_dtype(df["start"]),
        "start is not datetime"
    )
    check(
        pd.api.types.is_numeric_dtype(df["service_price"]),
        "service_price is not numeric"
    )

    # 5. Check appointment dates
    if pd.api.types.is_datetime64_any_dtype(df["date_parsed"]):
        check(
            df["date_parsed"].between(
                pd.Timestamp("2024-01-01"),
                pd.Timestamp.today().normalize()
            ).all(),
            "Appointment date outside 2024 to today"
        )

    # 6. Check prices
    check(
        (df["service_price"].dropna() >= 0).all(),
        "Negative prices"
    )

    # 7. Report validation results
    if problems:
        raise AssertionError(
            "Validation failed:\n- " + "\n- ".join(problems)
        )

    print(
        f"All checks passed: {len(df):,} rows, "
        f"{df.shape[1]} columns"
    )
    return df

