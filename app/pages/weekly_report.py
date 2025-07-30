def weekly_table(df):
    PERCENT_COLS = [
        "XL Δ% Baseline→MOCN",
        "XL Δ% Baseline→Latest",
        "SF Δ% Baseline→MOCN",
        "SF Δ% Baseline→Latest"
    ]
    # Pastikan float (handle error jika sudah % string)
    for col in PERCENT_COLS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    def highlight(val):
        if pd.isnull(val):
            return ""
        if val < 0:
            return "color: white; background-color: #d0312d"
        elif val > 0:
            return "color: white; background-color: #1ea75f"
        else:
            return ""

    # Apply percent format ke SEMUA percent cols sekaligus
    format_dict = {col: "{:.2f}%" for col in PERCENT_COLS if col in df.columns}
    styler = df.style.format(format_dict)
    # Apply coloring per kolom (tetap satu per satu)
    for col in PERCENT_COLS:
        if col in df.columns:
            styler = styler.applymap(highlight, subset=[col])

    return styler
