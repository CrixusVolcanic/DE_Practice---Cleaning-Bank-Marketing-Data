# Data Engineering Practice: Personal Loan Marketing Campaign Data Cleaning

This project focuses on cleaning and formatting data collected by a bank as part of a recent marketing campaign aimed at promoting personal loans. The cleaned data will be used to set up a PostgreSQL database to store the campaign's information, allowing for seamless integration of future marketing campaign data.

## Project Overview

Personal loans are a significant source of revenue for banks, with interest rates in the UK around 10% for a two-year loan. The project involves cleaning, reformatting, and splitting the provided data into three CSV files (`client.csv`, `campaign.csv`, and `economics.csv`) to match the required structure and data types.

### Data Sources

The original data comes from a CSV file named `bank_marketing.csv`, which contains information about clients, their interactions during the campaign, and relevant economic indicators.

### Objective

The goal is to prepare the data for ingestion into a PostgreSQL database by:
- Cleaning and transforming the data according to the bank's specifications.
- Splitting the data into three CSV files:
  - `client.csv`
  - `campaign.csv`
  - `economics.csv`

## Data Cleaning and Transformation

### 1. `client.csv`
| Column        | Data Type | Description                                      | Cleaning Requirements                                   |
|---------------|-----------|--------------------------------------------------|---------------------------------------------------------|
| client_id     | integer   | Client ID                                        | N/A                                                     |
| age           | integer   | Client's age in years                            | N/A                                                     |
| job           | object    | Client's type of job                             | Replace "." with "_"                                    |
| marital       | object    | Client's marital status                          | N/A                                                     |
| education     | object    | Client's level of education                      | Replace "." with "_"; Convert "unknown" to `np.NaN`     |
| credit_default| bool      | Whether the client's credit is in default        | Convert to boolean: `1` for "yes", otherwise `0`        |
| mortgage      | bool      | Whether the client has an existing mortgage      | Convert to boolean: `1` for "yes", otherwise `0`        |

### 2. `campaign.csv`
| Column                        | Data Type | Description                                      | Cleaning Requirements                                   |
|-------------------------------|-----------|--------------------------------------------------|---------------------------------------------------------|
| client_id                     | integer   | Client ID                                        | N/A                                                     |
| number_contacts               | integer   | Number of contact attempts in the current campaign | N/A                                                     |
| contact_duration              | integer   | Last contact duration in seconds                 | N/A                                                     |
| previous_campaign_contacts    | integer   | Contact attempts in the previous campaign        | N/A                                                     |
| previous_outcome              | bool      | Outcome of the previous campaign                 | Convert to boolean: `1` for "success", otherwise `0`    |
| campaign_outcome              | bool      | Outcome of the current campaign                  | Convert to boolean: `1` for "yes", otherwise `0`        |
| last_contact_date             | datetime  | Last contact date                                | Combine day, month, and a created year column (2022)    |
|                               |           |                                                  | Format: `YYYY-MM-DD`                                    |

### 3. `economics.csv`
| Column                | Data Type | Description                                      | Cleaning Requirements                                   |
|-----------------------|-----------|--------------------------------------------------|---------------------------------------------------------|
| client_id             | integer   | Client ID                                        | N/A                                                     |
| cons_price_idx        | float     | Consumer price index (monthly indicator)         | N/A                                                     |
| euribor_three_months  | float     | Euro Interbank Offered Rate (3-month rate)       | N/A                                                     |

## Tools and Libraries

The project was developed using the following libraries and tools:

- Python 3
- Pandas
- NumPy

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/CrixusVolcanic/DE_Practice---Cleaning-Bank-Marketing-Data.git
