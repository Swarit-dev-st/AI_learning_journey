ratings = []
from pathlib import Path

data_file = Path(__file__).parent / "ml-100k" / "u.data"

with open(data_file) as f:
    for line in f:
        parts = line.strip().split('\t')
        user_id = int(parts[0])
        movie_id = int(parts[1])
        rating = float(parts[2])

        ratings.append((user_id, movie_id, rating))



print(f"Total ratings: {len(ratings)}")
print(f"First 5 ratings: {ratings[:5]}")

all_ratings = [r[2] for r in ratings]
print(f"Highest Rating: {max(all_ratings)}")
print(f"Lowest Rating: {min(all_ratings)}")
print(f"Average Rating: {sum(all_ratings) / len(all_ratings):.2f}")

user_counts = {}
for user_id, movie_id, rating in ratings:
    if user_id not in user_counts:
        user_counts[user_id] = 0
    user_counts[user_id] += 1

sorted_user = sorted(user_counts.items(), key=lambda x: x[1], reverse=True)

print("\nTop 5 users by number of ratings:")
for user_id,count in sorted_user[:5]:
    print(f"User {user_id} rated {count} movies")

avg_ratings_per_user = len(ratings) / len(user_counts)
print (f"\nAverage movies Rated per User: {avg_ratings_per_user:.2f}")