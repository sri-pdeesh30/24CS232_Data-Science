import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv('Q12_music_streaming.csv')

# Display the first 5 rows to get an idea of the data
print("DISPLAYING FIRST 5 USING head()")
df.head()

# Get a summary of the DataFrame to check data types and non-null values
df.info()


# Display descriptive statistics for numerical columns
print("\nDISPLAYING DESCRIPTIVE STATISTICS FOR NUMERICAL COLUMNS")
df.describe()


# Drop rows where 'avg_listening_minutes' or 'session_count' are missing
df_cleaned = df.dropna(subset=['avg_listening_minutes', 'session_count'])


# Check the info again to see if missing values are handled
print("\nDISPLAYING INFO AFTER DROPPING MISSING VALUES")
df_cleaned.info()


# Calculate the average listening minutes for each unique user
# We'll group by user_id and subscription_tier to ensure we get the right tier for each user's average
user_avg_listening = df_cleaned.groupby(['user_id', 'subscription_tier'])['avg_listening_minutes'].mean().reset_index()
print("\nDISPLAYING AVERAGE LISTENING MINUTES FOR EACH USER")
# Display the first few rows of our new user-level average data
user_avg_listening.head()


# Calculate descriptive statistics for average listening minutes in each subscription tier
tier_listening_stats = user_avg_listening.groupby('subscription_tier')['avg_listening_minutes'].agg(['mean', 'median', 'std', 'min', 'max', 'count'])

# Display the results
print(tier_listening_stats)