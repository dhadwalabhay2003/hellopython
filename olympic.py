import pandas as pd

# Load the dataset using a corrected file path
df = pd.read_csv(r'https://www.kaggle.com/datasets/datasciencedonut/olympic-swimming-1912-to-2020')

# Assuming the dataset has columns named 'Country', 'Sport', and 'Medal'
# Replace 'Country', 'Sport', and 'Medal' with the actual column names if they are different

# Filter the data for swimming events
df_swimming = df[df['Sport'] == 'Swimming']

# Group by 'Country' and 'Medal' to count the occurrences
medal_count = df_swimming.groupby(['Country', 'Medal']).size().unstack(fill_value=0)

# Add a total column for the sum of all medals
medal_count['Total'] = medal_count.sum(axis=1)

# Convert the DataFrame to a dictionary of dictionaries
medal_dict = medal_count.to_dict(orient='index')

# Function to get the medal count for a specific country
def get_swimming_medal_count(country):
    if country in medal_dict:
        medal_tuple = (
            medal_dict[country].get('Gold', 0),
            medal_dict[country].get('Silver', 0),
            medal_dict[country].get('Bronze', 0),
            medal_dict[country].get('Total', 0)
        )
        return medal_tuple
    else:
        return "Country not found in the dataset or has not won any medals in swimming."

# List of available countries in the dataset
available_countries = list(medal_dict.keys())

# Function to handle user input and display the results
def display_medal_count():
    print("Available countries:", available_countries)
    country_name = input("Enter the country name from the list above: ")
    result = get_swimming_medal_count(country_name)
    
    if isinstance(result, tuple):
        print(f"Medal count for {country_name} in swimming:")
        print(f"Gold: {result[0]}")
        print(f"Silver: {result[1]}")
        print(f"Bronze: {result[2]}")
        print(f"Total: {result[3]}")
    else:
        print(result)

# Run the display function
display_medal_count()
