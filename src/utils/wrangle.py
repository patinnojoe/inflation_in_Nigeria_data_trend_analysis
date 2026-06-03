import pandas as pd

def wrangle(csv_path):
    
    # read the csv file
    df = pd.read_csv(csv_path)
    
    # get the columns with missing values
    missing_values = df.isnull().sum()

    # determine columns to drop: any column with missing values greater than 50
    columns_to_drop = missing_values[
        missing_values > 50
    ].index
    
    # create the analysis_df
    analysis_df = df.drop(columns=columns_to_drop)
    
    # rename all columns 
    analysis_df = analysis_df.rename(columns={

    # Time
    "Year": "year",
    "Month": "month",

    # Headline / Core CPI
    "All Items": "overall_cpi",
    "All Items less Farm Produce. ": "core_cpi_ex_food",
    "All Items less Farm Produce. and Energy": "core_cpi_ex_food_energy",

    # Food & Imports
    "Imported Food": "imported_food_cpi",
    "Food": "food_cpi",
    "Food &  Non Alcoholic Bev.": "food_non_alcoholic_beverages_cpi",

    # Specific consumption categories
    "ALCOHOLIC BEVERAGES, TOBACCO AND  NARCOTICS": "alcohol_tobacco_drugs_cpi",
    "Clothing and Footwear": "clothing_footwear_cpi",
    "HOUSING, WATER, ELECTRICITY, GAS AND OTHER FUELS": "utilities_housing_energy_cpi",
    "FURNISHINGS, HOUSEHOLD EQUIPMENT AND ROUTINE HOUSEHOLD MAINTENANCE": "household_goods_cpi",

    # Social services / human capital
    "Health.": "health_cpi",
    "Transport": "transport_cpi",
    "INFORMATION AND COMMUNICATION": "communication_cpi",
    "RECREATION, SPORT AND CULTURE": "recreation_culture_cpi",
    "EDUCATION SERVICES": "education_cpi",
    "RESTAURANTS AND ACCOMODATION SERVICES": "restaurants_accommodation_cpi",

    # Misc / residual consumption
    "PERSONAL CARE, SOCIAL PROTECTION AND MISCELLANEOUS GOODS AND SERVICES": "personal_care_misc_cpi",

    # Inflation rates
    "Month-on (%)": "mom_inflation_pct",
    "Year-on (%)": "yoy_inflation_pct",
    "12-month average (%)": "avg_12m_inflation_pct"
})

    # create month map to convert months to int values
    month_map = {
    "Jan": 1,
    "January": 1,
    'Feb': 2,
    "February": 2,
    "March": 3,
    "Mar": 3,
    "April": 4,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "June": 6,
    "Jul": 7,
    "July": 7,
    "Aug": 8,
    "August": 8,
    "Sep": 9,
    "September": 9,
    "Oct": 10,
    "October": 10,
    "Nov": 11,
    "November": 11,
    "Dec": 12,
    "December": 12
}

    #  Clean up spaces and casing first (highly recommended)
    analysis_df['month'] = analysis_df['month'].astype(str).str.strip().str.title()

    #  Run the mapping
    analysis_df['month'] = analysis_df['month'].map(month_map)
    # create date object
    analysis_df["date"] = pd.to_datetime({
        "year": analysis_df["year"],
        "month": analysis_df["month"],
        "day": 1
    })

    analysis_df.set_index('date', inplace=True)
    analysis_df.drop(columns=['year', 'month'], inplace=True)

    
    return analysis_df