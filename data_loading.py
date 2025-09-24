import pandas as pd


def load_full_crime_data_df():
    year_range = list(range(2020, 2026))
    main_df = None
    for year in year_range:
        df = pd.read_csv(f"data/crime_data_{year}.csv")
        if main_df is None:
            main_df = df
        else:
            main_df = pd.concat([main_df, df], ignore_index=True)
    return main_df
