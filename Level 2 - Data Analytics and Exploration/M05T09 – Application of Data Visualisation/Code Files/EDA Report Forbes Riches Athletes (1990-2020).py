# -*- coding: utf-8 -*-
"""
Modular Forbes Richest Athletes EDA
@author: juleigar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import chardet
import missingno as msno

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# ------------------ DATA LOADING ------------------
def load_data(file_path):
    """Detect encoding and load CSV safely"""
    try:
        with open(file_path, "rb") as f:
            encoding = chardet.detect(f.read())["encoding"]
        df = pd.read_csv(file_path, encoding=encoding)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# ------------------ DATA CLEANING ------------------
def clean_sport(df):
    """Standardize Sport column"""
    df["Sport"] = (
        df["Sport"]
        .astype(str)
        .str.lower()
        .str.replace(r'[^a-z\s]', ' ', regex=True)
        .str.replace(r'\s+', ' ', regex=True)
        .str.strip()
    )
    replacement_map = {
        "auto racing nascar": "motorsports",
        "nascar": "motorsports",
        "auto racing": "motorsports",
        "f motorsports": "motorsports",
        "f racing": "motorsports",
        "hockey": "ice hockey",
        "nfl": "american football",
        "nba": "basketball",
        "american football baseball": "american football",
    }
    df["Sport"] = df["Sport"].replace(replacement_map, regex=False)
    return df

def clean_nationality(df):
    """Standardize Nationality column"""
    nationality_map = {
        "USA": "American",
        "Brazil": "Brazilian",
        "France": "French",
        "Australia": "Australian",
        "Canada": "Canadian",
        "UK": "British",
        "Austria": "Austrian",
        "Germany": "German",
        "Russia": "Russian",
        "Italy": "Italian",
        "Finland": "Finnish",
        "Switzerland": "Swiss",
        "Philippines": "Filipino",
        "Filipino": "Filipino",
        "Portugal": "Portuguese",
        "Dominican": "Dominican",
        "Argentina": "Argentine",
        "Spain": "Spanish",
        "Serbia": "Serbian",
        "Northern Ireland": "Northern Irish",
        "Ireland": "Irish",
        "Mexico": "Mexican"
    }
    df["Nationality"] = df["Nationality"].astype(str).str.strip().replace(nationality_map, regex=False)
    return df

def clean_previous_rank(df):
    """Clean Previous Year Rank column"""
    df["Previous Year Rank"] = df["Previous Year Rank"].replace(
        ["nan", "not ranked", "none", "?", "??"], np.nan
    )
    df["PrevRank_GT_Flag"] = df["Previous Year Rank"].astype(str).str.contains('>', na=False)
    df["PrevYearRank_Clean"] = df["Previous Year Rank"].astype(str).str.replace(r'>', ' ', regex=True)
    df["PrevYearRank_Clean"] = pd.to_numeric(df["PrevYearRank_Clean"], errors='coerce')
    return df

def preprocess_earnings(df):
    """Convert earnings to numeric"""
    df['earnings ($ million)'] = pd.to_numeric(df['earnings ($ million)'], errors='coerce')
    return df

# ------------------ VISUALIZATION FUNCTIONS ------------------
def plot_missing_data(df):
    """Fig 1: Visualize missing data"""
    if df is not None:
        plt.figure(figsize=(12,6))
        msno.bar(df)
        plt.title("Fig 1: Missing Data Overview")
        plt.show()

def plot_earnings_distribution(df):
    """Fig 2 & 3: Boxplot and Histogram of Earnings"""
    plt.figure(figsize=(12,6))
    sns.boxplot(x="earnings ($ million)", data=df)
    plt.title("Fig 2: Box Plot of Earnings in Millions")
    plt.show()

    plt.figure(figsize=(12,6))
    sns.histplot(x="earnings ($ million)", data=df, bins=30, kde=True)
    plt.title("Fig 1: Histogram of Earnings")
    plt.show()

def plot_median_earnings_by_year(df):
    """Fig 4: Median earnings per year, highlight missing data"""
    df['Year'] = df['Year'].astype(int)
    
    # Calculate median earnings per year
    median_earnings_year = df.groupby("Year")["earnings ($ million)"].median().reset_index()
    
    # Create full year range 1990-2020
    full_years = pd.DataFrame({'Year': range(df['Year'].min(), df['Year'].max()+1)})
    
    # Merge with median earnings, missing years will have NaN
    merged = full_years.merge(median_earnings_year, on='Year', how='left')
    
    plt.figure(figsize=(12,6))
    
    # Plot median earnings line (ignore NaNs, will break line for missing)
    sns.lineplot(data=merged, x='Year', y='earnings ($ million)', marker='o', label='Median Earnings')
    
    # Highlight missing years with red vertical line
    missing_years = merged[merged['earnings ($ million)'].isna()]['Year'].tolist()
    for year in missing_years:
        plt.axvline(x=year, color='red', linestyle='--', label=f'Missing {year}')
    
    plt.xticks(merged['Year'][::2], rotation=45)
    plt.title("Fig 2: Median Earnings by Year (Missing Years Highlighted)")
    plt.ylabel("Earnings ($ Million)")
    plt.xlabel("Year")
    
    # Avoid duplicate legend entries for multiple missing years
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    
    plt.show()

def plot_earnings_by_sport_year(df, top_n=5):
    """Fig 5: Median earnings per year for top N sports"""
    
    # Step 1: Find top N sports by total earnings
    top_sports = (
        df.groupby("Sport")["earnings ($ million)"].sum()
        .sort_values(ascending=False)
        .head(top_n)
        .index
    )
    
    # Step 2: Filter the dataframe for only top N sports
    df_top_sports = df[df["Sport"].isin(top_sports)]
    
    # Step 3: Group by Year and Sport and calculate median earnings
    df_year_sport = df_top_sports.groupby(["Year", "Sport"])["earnings ($ million)"].median().reset_index()
    
    # Step 4: Plot
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df_year_sport, x="Year", y="earnings ($ million)", hue="Sport", marker="o")
    plt.title(f"Fig 3: Median Earnings by Year for Top {top_n} Sports")
    plt.ylabel("Median Earnings ($ Million)")
    plt.xlabel("Year")
    plt.xticks(df_year_sport['Year'].unique()[::2], rotation=45)
    plt.legend(title="Sport")
    plt.tight_layout()
    plt.show()


def plot_top_earners_with_monica(df, top_n=10):
    """Fig8: Top earners overall including Monica Seles"""
    
    # 1. Aggregate total earnings for each athlete
    total_earnings = df.groupby(["Name", "Sport"])["earnings ($ million)"].sum().reset_index()

    # 2. Add Monica Seles manually if not present
    seles_data = {'Name': 'Monica Seles', 'Sport': 'tennis', 'earnings ($ million)': 8.2}
    seles_df = pd.DataFrame([seles_data])
    
    # Concatenate her data
    total_earnings = pd.concat([total_earnings, seles_df], ignore_index=True)
    
    # 3. Sort descending by earnings
    total_earnings = total_earnings.sort_values("earnings ($ million)", ascending=False)
    
    # 4. Take top N, then append Monica if not already included
    top_earners = total_earnings.head(top_n)
    if 'Monica Seles' not in top_earners['Name'].values:
        monica_row = total_earnings[total_earnings['Name'] == 'Monica Seles']
        top_earners = pd.concat([top_earners, monica_row], ignore_index=True)
    
    # 5. Plot
    plt.figure(figsize=(12,6))
    sns.barplot(data=top_earners, x="Name", y="earnings ($ million)", hue="Sport")
    plt.title(f"Fig 8: Top {top_n} Total Earners (1990-2020) Including Monica Seles")
    plt.xticks(rotation=45)
    plt.ylabel("Earnings ($ Million)")
    plt.xlabel("Athlete")
    plt.legend(title="Sport")
    plt.tight_layout()
    plt.show()


def plot_number_one_athletes(df):
    """Fig 5: #1 ranked athletes by year"""
    filtered_df = df[df["Current Rank"] == 1]
    top_ranked = filtered_df[["Year", "Name", "earnings ($ million)"]].drop_duplicates().sort_values("Year")

    plt.figure(figsize=(13,6))
    sns.barplot(data=top_ranked, x="Year", y="earnings ($ million)", hue="Name", dodge=False)

    for i, row in top_ranked.iterrows():
        plt.text(
            x=row["Year"],
            y=row["earnings ($ million)"] + 3,
            s=row["Name"],
            ha="center",
            fontsize=10,
            rotation=90
        )

    plt.title("Fig 5: Forbes #1 Ranked Athlete by Year (and Their Earnings)", fontsize=12)
    plt.ylabel("Earnings ($ Million)")
    plt.xlabel("Year")
    plt.legend(title="Athlete", bbox_to_anchor=(1.00, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def plot_unique_athletes_stacked(df, top_n_sports=6):
    """
    Fig X: Stacked bar plot of unique athletes per year for top N sports.

    Parameters:
    df (DataFrame): Forbes athletes dataframe
    top_n_sports (int): Number of top sports to display
    """
    # Count unique athletes per year per sport
    unique_athletes = df.groupby(["Year", "Sport"])["Name"].nunique().reset_index()
    unique_athletes.rename(columns={"Name": "UniqueAthletes"}, inplace=True)

    # Determine top N sports by total athletes across all years
    top_sports = (
        unique_athletes.groupby("Sport")["UniqueAthletes"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n_sports)
        .index
    )

    # Filter to top N sports
    unique_athletes_top = unique_athletes[unique_athletes["Sport"].isin(top_sports)]

    # Pivot for stacked barplot
    df_pivot = unique_athletes_top.pivot(index="Year", columns="Sport", values="UniqueAthletes").fillna(0)

    # Plot
    df_pivot.plot(kind="bar", stacked=True, figsize=(14,6), colormap="tab20")
    plt.title(f"Fig X: Unique Athletes per Year (Stacked by Top {top_n_sports} Sports)")
    plt.ylabel("Number of Unique Athletes")
    plt.xlabel("Year")
    plt.xticks(rotation=45)
    plt.legend(title="Sport", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def plot_unique_athletes_stacked_percent(df, top_n_sports=6):
    """
    Fig 7: Stacked bar plot of % unique athletes per year for top N sports.

    Parameters:
    df (DataFrame): Forbes athletes dataframe
    top_n_sports (int): Number of top sports to display
    """
    # Count unique athletes per year per sport
    unique_athletes = df.groupby(["Year", "Sport"])["Name"].nunique().reset_index()
    unique_athletes.rename(columns={"Name": "UniqueAthletes"}, inplace=True)

    # Determine top N sports by total athletes across all years
    top_sports = (
        unique_athletes.groupby("Sport")["UniqueAthletes"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n_sports)
        .index
    )

    # Filter to top N sports
    unique_athletes_top = unique_athletes[unique_athletes["Sport"].isin(top_sports)]

    # Pivot for stacked barplot
    df_pivot = unique_athletes_top.pivot(index="Year", columns="Sport", values="UniqueAthletes").fillna(0)

    # Convert to percentages
    df_percent = df_pivot.div(df_pivot.sum(axis=1), axis=0) * 100

    # Plot
    df_percent.plot(kind="bar", stacked=True, figsize=(12,6), colormap="tab20")
    plt.title(f"Fig 7: % of Unique Athletes per Year (Top {top_n_sports} Sports)")
    plt.ylabel("Percentage of Unique Athletes")
    plt.xlabel("Year")
    plt.xticks(rotation=45)
    plt.legend(title="Sport", bbox_to_anchor=(-0.01, 1), loc="upper right")

    plt.tight_layout()
    plt.show()




def plot_top_nationalities_stacked_percent(df, top_n=5):
    """Fig 6: Top Nationalities by Total Earnings (stacked by Sport) with percentages"""
    # Sum earnings per nationality
    nationality_earnings = df.groupby("Nationality")["earnings ($ million)"].sum().reset_index()
    top_nationalities = nationality_earnings.sort_values("earnings ($ million)", ascending=False).head(top_n)["Nationality"].tolist()
    
    # Filter top nationalities
    df_top = df[df["Nationality"].isin(top_nationalities)]
    
    # Pivot: index = nationality, columns = sport, values = sum of earnings
    pivot = df_top.pivot_table(
        index="Nationality",
        columns="Sport",
        values="earnings ($ million)",
        aggfunc="sum",
        fill_value=0
    )
    
    # Convert to percentages per nationality
    pivot_percent = pivot.div(pivot.sum(axis=1), axis=0) * 100
    
    # Plot stacked bar chart
    ax = pivot_percent.plot(kind="bar", stacked=True, figsize=(12,6), colormap="tab20")
    
    plt.title(f"Fig 6: Top {top_n} Nationalities by Earnings (Stacked by Sport, %)", fontsize=14)
    plt.ylabel("Percentage of Total Earnings")
    plt.xlabel("Nationality")
    
    # Move legend to the left
    plt.legend(title="Sport", bbox_to_anchor=(-0.15, 1), loc='upper left')
    
    # Show percentage labels inside bars
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        if height > 0:
            x, y = p.get_x(), p.get_y()
            ax.text(x + width/2, y + height/2, f"{height:.1f}%", ha="center", va="center", fontsize=8, color="white")
    
    plt.tight_layout()
    plt.show()

# ------------------ MAIN ------------------
def main():
    file_path = "Forbes Richest Athletes (Forbes Richest Athletes 1990-2020).csv"
    df = load_data(file_path)
    if df is None:
        return

    # ------------------ DATA CLEANING ------------------
    df = clean_sport(df)
    df = clean_nationality(df)
    df = clean_previous_rank(df)
    df = preprocess_earnings(df)

    # ------------------ EDA & VISUALIZATIONS ------------------
    # Fig numbers are included in titles for easy reference in your report
    plot_missing_data(df)                # Fig 1
    plot_earnings_distribution(df)      # Fig 2 & Fig 3
    plot_median_earnings_by_year(df)    # Fig 4
    plot_earnings_by_sport_year(df)     # Fig 5
    plot_number_one_athletes(df)         # Fig 6
    plot_unique_athletes_stacked_percent(df, top_n_sports=6) # Fig 7
    plot_top_nationalities_stacked_percent(df, top_n=5) #Fig 8
    plot_top_earners_with_monica(df) #Fig 9
if __name__ == "__main__":
    main()
