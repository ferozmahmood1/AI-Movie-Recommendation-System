# ============================================================
# Monthly Assessment Project
# Python for AI & Data Science
# Project Title: AI-Based Movie Recommendation System
# Google Colab One-Cell Version
# ============================================================

print("=" * 70)
print("        Welcome to the AI-Based Movie Recommendation System")
print("=" * 70)

print("\nThis system recommends movies based on your age, genre, rating, and mood.")
print("Please enter the required information below.\n")

# ============================================================
# Movie Dataset Creation
# Dataset created using a list of tuples
# Format:
# (Movie Name, Genre, Rating, Minimum Age Requirement, Mood/Interest)
# ============================================================

movies = [
    ("Toy Story", "Animation", 8.3, 5, "happy"),
    ("Finding Nemo", "Animation", 8.2, 5, "happy"),
    ("The Lion King", "Animation", 8.5, 6, "emotional"),
    ("Coco", "Animation", 8.4, 7, "emotional"),
    ("Spider-Man", "Action", 7.4, 13, "excited"),
    ("Avengers: Endgame", "Action", 8.4, 13, "excited"),
    ("The Dark Knight", "Action", 9.0, 16, "serious"),
    ("Inception", "Sci-Fi", 8.8, 13, "thoughtful"),
    ("Interstellar", "Sci-Fi", 8.7, 13, "thoughtful"),
    ("The Martian", "Sci-Fi", 8.0, 13, "inspiring"),
    ("Jumanji", "Adventure", 7.0, 10, "fun"),
    ("Harry Potter", "Fantasy", 7.6, 10, "magical")
]

# ============================================================
# Display Available Genres
# ============================================================

print("Available Genres:")
print("- Animation")
print("- Action")
print("- Sci-Fi")
print("- Adventure")
print("- Fantasy")

print("\nAvailable Moods or Interests:")
print("- happy")
print("- emotional")
print("- excited")
print("- serious")
print("- thoughtful")
print("- inspiring")
print("- fun")
print("- magical")

# ============================================================
# User Input Section
# ============================================================

user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age: "))
preferred_genre = input("Enter your preferred genre: ")
user_mood = input("Enter your mood or interest: ")

# Bonus Feature: Search functionality
search_choice = input("\nDo you want to search for a movie also? Type yes or no: ")

searched_movie = ""

if search_choice.lower() == "yes":
    searched_movie = input("Enter movie name to search: ")

# ============================================================
# Lists for storing recommendations
# ============================================================

recommended_movies = []
high_rated_movies = []
mood_based_movies = []
watch_history = []
search_results = []

# ============================================================
# Count Total Movies Using For Loop
# ============================================================

total_movies = 0

for movie in movies:
    total_movies = total_movies + 1

# ============================================================
# Recommendation Logic
# Conditions used:
# 1. Genre matching
# 2. Age checking
# 3. High rating checking
# 4. Mood matching
# ============================================================

for movie in movies:
    movie_name = movie[0]
    movie_genre = movie[1]
    movie_rating = movie[2]
    minimum_age = movie[3]
    movie_mood = movie[4]

    # Main recommendation condition: genre must match and user must meet age requirement
    if preferred_genre.lower() == movie_genre.lower() and user_age >= minimum_age:
        recommended_movies.append(movie)
        watch_history.append(movie_name)

        # Highly rated movies are prioritized
        if movie_rating >= 8.0:
            high_rated_movies.append(movie)

        # Bonus: mood-based recommendation
        if user_mood.lower() == movie_mood.lower():
            mood_based_movies.append(movie)

    # Bonus: search functionality
    if searched_movie.lower() == movie_name.lower():
        search_results.append(movie)

# ============================================================
# Output Section
# ============================================================

print("\n" + "=" * 70)
print("                  MOVIE RECOMMENDATION REPORT")
print("=" * 70)

print("\nUser Name:", user_name)
print("User Age:", user_age)
print("Preferred Genre:", preferred_genre)
print("Mood/Interest:", user_mood)
print("Total Movies in Dataset:", total_movies)

print("\n" + "-" * 70)
print("Recommended Movies for", user_name)
print("-" * 70)

if len(recommended_movies) > 0:
    for movie in recommended_movies:
        print("\nMovie Name:", movie[0])
        print("Genre:", movie[1])
        print("Rating:", movie[2])
        print("Minimum Age Required:", movie[3])
        print("Mood/Interest:", movie[4])
else:
    print("\nSorry, no suitable movies were found for your age and selected genre.")
    print("Please try another genre from the available options.")

# ============================================================
# Highly Rated Recommendations
# ============================================================

print("\n" + "-" * 70)
print("Highly Rated Recommendations")
print("-" * 70)

if len(high_rated_movies) > 0:
    for movie in high_rated_movies:
        print("⭐", movie[0], "| Rating:", movie[2], "| Genre:", movie[1])
else:
    print("No highly rated movies found for your selected genre and age.")

# ============================================================
# Mood-Based Recommendations
# ============================================================

print("\n" + "-" * 70)
print("Mood-Based Recommendations")
print("-" * 70)

if len(mood_based_movies) > 0:
    for movie in mood_based_movies:
        print("🎬", movie[0], "| Mood:", movie[4], "| Rating:", movie[2])
else:
    print("No exact mood-based match found.")
    print("Genre and age-based recommendations are already shown above.")

# ============================================================
# Age Restriction Message
# ============================================================

print("\n" + "-" * 70)
print("Age Restriction Check")
print("-" * 70)

restricted_count = 0

for movie in movies:
    if preferred_genre.lower() == movie[1].lower() and user_age < movie[3]:
        restricted_count = restricted_count + 1
        print("Restricted Movie:", movie[0], "| Required Age:", movie[3])

if restricted_count == 0:
    print("No age-restricted movies were blocked for your selected genre.")
else:
    print("Total Age-Restricted Movies Blocked:", restricted_count)

# ============================================================
# Bonus Feature: Search Result
# ============================================================

if search_choice.lower() == "yes":
    print("\n" + "-" * 70)
    print("Movie Search Result")
    print("-" * 70)

    if len(search_results) > 0:
        for movie in search_results:
            print("Movie Found:", movie[0])
            print("Genre:", movie[1])
            print("Rating:", movie[2])
            print("Minimum Age Required:", movie[3])

            if user_age >= movie[3]:
                print("Status: You are allowed to watch this movie.")
            else:
                print("Status: You are not allowed to watch this movie because of age restriction.")
    else:
        print("Movie not found in the dataset.")

# ============================================================
# Bonus Feature: Watch History Tracking
# ============================================================

print("\n" + "-" * 70)
print("Watch History / Recommendation History")
print("-" * 70)

if len(watch_history) > 0:
    for movie_name in watch_history:
        print("-", movie_name)
else:
    print("No movies were added to watch history.")

# ============================================================
# Final Message
# ============================================================

print("\n" + "=" * 70)
print("Thank you for using the AI-Based Movie Recommendation System!")
print("=" * 70)