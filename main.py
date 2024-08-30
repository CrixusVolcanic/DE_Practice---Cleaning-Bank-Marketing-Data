import pandas as pd
import numpy as np

def fn_cleaning_data():

    # Read in csv
    marketing = pd.read_csv("bank_marketing.csv")

    # Split into the three tables
    client = marketing[["client_id", "age", "job", "marital", 
                        "education", "credit_default", "mortgage"]]
    campaign = marketing[["client_id", "number_contacts", "month", "day", 
                "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome"]]
    economics = marketing[["client_id", "cons_price_idx", "euribor_three_months"]]

    ## Editing the client dataset
    # Clean education column
    client["education"] = client["education"].str.replace(".", "_")
    client["education"] = client["education"].replace("unknown", np.nan)

    # Clean job column
    client["job"] = client["job"].str.replace(".", "_")

    # Clean and convert client columns to bool data type
    for col in ["credit_default", "mortgage"]:
        client[col] = client[col].map({"yes": 1,
                                        "no": 0,
                                        "unknown": 0})
        client[col] = client[col].astype(bool)

    # Editing the campaign dataset
    # Change campaign_outcome to binary values
    campaign["campaign_outcome"] = campaign["campaign_outcome"].map({"yes": 1, 
                                                                    "no": 0})

    # Convert previous_outcome to binary values
    campaign["previous_outcome"] = campaign["previous_outcome"].map({"success": 1, 
                                                                    "failure": 0,
                                                                    "nonexistent": 0})

    # Add year column
    campaign["year"] = "2022"

    # Convert day to string
    campaign["day"] = campaign["day"].astype(str)

    # Add last_contact_date column
    campaign["last_contact_date"] = campaign["year"] + "-" + campaign["month"] + "-" + campaign["day"]

    # Convert to datetime
    campaign["last_contact_date"] = pd.to_datetime(campaign["last_contact_date"], 
                                                format="%Y-%b-%d")

    # Clean and convert outcome columns to bool
    for col in ["campaign_outcome", "previous_outcome"]:
        campaign[col] = campaign[col].astype(bool)

    # Drop unneccessary columns
    campaign.drop(columns=["month", "day", "year"], inplace=True)

    ### Assert validations
    assert client['job'].str.contains(r'\.').sum() == 0
    assert client['education'].str.contains(r'\.').sum() == 0
    assert client['education'].str.contains('unknown').sum() == 0

    assert client['client_id'].dtype == int
    assert client['age'].dtype == int
    assert client['job'].dtype == object
    assert client['marital'].dtype == object
    assert client['education'].dtype == object
    assert client['credit_default'].dtype == bool
    assert client['mortgage'].dtype == bool

    ### Assert validations
    assert campaign['client_id'].dtype == int
    assert campaign['number_contacts'].dtype == int
    assert campaign['contact_duration'].dtype == int
    assert campaign['previous_campaign_contacts'].dtype == int

    assert campaign['previous_outcome'].dtype == bool
    assert campaign['campaign_outcome'].dtype == bool
    assert campaign['last_contact_date'].dtype == 'datetime64[ns]'

    # Save tables to individual csv files
    client.to_csv("client.csv", index=False)
    campaign.to_csv("campaign.csv", index=False)
    economics.to_csv("economics.csv", index=False)

if __name__ == "__main__":

    fn_cleaning_data()

    # Start coding...
import pandas as pd
import numpy as np



