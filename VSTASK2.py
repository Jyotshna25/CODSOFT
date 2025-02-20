# Simple Collaborative Filtering Recommendation System
class CollaborativeFilteringRecommender:

    def __init__(self):
        """
        Initializes the dataset containing user ratings for movies and music.
        """
        self.users = {
            "Alice": {"Inception": 5, "Interstellar": 4, "The Matrix": 3, "Bohemian Rhapsody": 2},
            "Bob": {"Inception": 4, "The Matrix": 5, "The Dark Knight": 5, "Imagine": 3},
            "Charlie": {"Interstellar": 5, "Avengers: Endgame": 4, "Bohemian Rhapsody": 4, "Hotel California": 3},
            "David": {"The Matrix": 5, "The Dark Knight": 4, "Billie Jean": 5, "Hotel California": 4},
            "Emma": {"Inception": 4, "Interstellar": 3, "Bohemian Rhapsody": 5, "Shape of You": 4}
        }

    def find_similar_users(self, target_user):
        """
        Finds users with similar tastes based on shared item ratings.
        """
        if target_user not in self.users:
            return f"User '{target_user}' not found in database."

        target_ratings = self.users[target_user]
        similarity_scores = {}

        for user, ratings in self.users.items():
            if user == target_user:
                continue  # Skip the target user

            common_items = 0
            similarity_score = 0

            for item in target_ratings:
                if item in ratings:  # Check if both users have rated the same item
                    common_items += 1
                    similarity_score += abs(target_ratings[item] - ratings[item])  # Calculate rating difference

            if common_items > 0:
                similarity_scores[user] = similarity_score / common_items  # Average difference

        # Sort users by similarity (lower difference = more similar)
        similar_users = sorted(similarity_scores, key=lambda x: similarity_scores[x])
        return similar_users

    def recommend_items(self, target_user, top_n=3):
        """
        Recommends items based on similar users' preferences.
        """
        similar_users = self.find_similar_users(target_user)

        if isinstance(similar_users, str):  # If user not found
            return similar_users

        target_rated_items = set(self.users[target_user].keys())
        recommendations = {}

        for similar_user in similar_users:
            for item, rating in self.users[similar_user].items():
                if item not in target_rated_items:  # Recommend only new items
                    if item not in recommendations:
                        recommendations[item] = 0
                    recommendations[item] += rating  # Sum ratings from similar users

        # Sort recommendations by rating (higher is better)
        sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

        return sorted_recommendations[:top_n]


# Create an instance of the collaborative filtering system
collab_recommender = CollaborativeFilteringRecommender()

# User selects a name (e.g., Alice)
target_user = "Alice"

# Get recommendations for Alice
print(f" Recommendations for '{target_user}':")
recommendations = collab_recommender.recommend_items(target_user)

# Display recommendations
for title, score in recommendations:
    print(f" {title} | Estimated Interest Score: {score}")

print("\n---------------------------\n")

# Try another example (Bob)
target_user = "Bob"

print(f" Recommendations for '{target_user}':")
recommendations = collab_recommender.recommend_items(target_user)

# Display recommendations
for title, score in recommendations:
    print(f" {title} | Estimated Interest Score: {score}")
