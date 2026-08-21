import pandas as pd
import matplotlib.pyplot as plt


# Load the music streaming data.
df = pd.read_csv("Q12_music_streaming.csv")

# Remove the two rows that do not have listening-time values.
df_cleaned = df.dropna(subset=["avg_listening_minutes"])


# Visualization 1: average listening time for each subscription tier.
average_listening = (
	df_cleaned.groupby("subscription_tier")["avg_listening_minutes"]
	.mean()
	.sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
average_listening.plot(kind="bar", color=["#2a9d8f", "#e9c46a", "#f4a261"])
plt.title("Average Listening Time by Subscription Tier")
plt.xlabel("Subscription tier")
plt.ylabel("Average listening time (minutes)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Visualization 2: relationship between sessions and listening time.
plt.figure(figsize=(8, 5))
plt.scatter(
	df_cleaned["session_count"],
	df_cleaned["avg_listening_minutes"],
	color="#264653",
	alpha=0.75,
)
plt.title("Sessions and Average Listening Time")
plt.xlabel("Number of sessions")
plt.ylabel("Average listening time (minutes)")
plt.tight_layout()
plt.show()
