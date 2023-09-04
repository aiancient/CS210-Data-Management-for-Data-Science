import math
from collections import defaultdict
from collections import Counter

# You may not add any other imports

# For each function, replace "pass" with your code

# --- TASK 1: READING DATA ---

# 1.1
def read_ratings_data(f):
    movieRating = {}
    for line in open(f):
        movie, rating, userID = line.split("|")
        if movie not in movieRating:
            movieRating[movie.strip()] = []
        ratingList = movieRating.get(movie)
        ratingList.append(float(rating))
    return movieRating

# 1.2
def read_movie_genre(f):
    movieGenre = {}
    for line in open(f):
        genre, movieID, movie = line.split("|")
        if movie not in movieGenre:
            movieGenre[movie.strip()] = genre.strip()
    return movieGenre

# --- TASK 2: PROCESSING DATA ---

# 2.1
def create_genre_dict(d):
    genreDict = {}
    for movieKey in d.keys(): 
        if d[movieKey] not in genreDict: 
            genreDict[d[movieKey]] = []
        genreMovieList = genreDict.get(d[movieKey])
        genreMovieList.append(movieKey)
    return genreDict

# 2.2
def calculate_average_rating(d):
    averageRating = {}
    for movie in d.keys():
        total = 0
        count = 0
        for rating in d[movie]:
            total += rating
            count += 1
        averageRating[movie] = total/count
    return averageRating

# --- TASK 3: RECOMMENDATION ---

# 3.1
def get_popular_movies(d, n=10):
    popMoviesLH = {}
    popMoviesLH = dict(sorted(d.items(),
                      key= lambda movie: movie[1]))
    popMoviesHL = dict(reversed(list(popMoviesLH.items())))
    return dict(list(popMoviesHL.items())[0: n])

# 3.2
def filter_movies(d, thres_rating=3):
    filteredMovies = {}
    for k in d:
        if d[k]>=thres_rating: 
            filteredMovies[k] = d[k]
    return filteredMovies

# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=50):
    genreMovies = []
    for k in genre_to_movies:
        if k.lower()==genre.lower(): 
            genreMovies.append(genre_to_movies[k])
    
    genreMoviesWAverages = {} 
    for k in movie_to_average_rating:
        if k in genreMovies[0]: 
            genreMoviesWAverages[k] = movie_to_average_rating[k]
    
    topNMoviesOfGenreLH = {}
    topNMoviesOfGenreLH = dict(sorted(genreMoviesWAverages.items(),
                      key= lambda movie: movie[1]))
    topNMoviesOfGenreHL = dict(reversed(list(topNMoviesOfGenreLH.items())))
    return dict(list(topNMoviesOfGenreHL.items())[0: n])
    

# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    genreMovies = []
    for k in genre_to_movies:
        if k.lower()==genre.lower(): 
            genreMovies.append(genre_to_movies[k])
    
    genreMoviesWAverages = {} 
    for k in movie_to_average_rating:
        if k in genreMovies[0]: 
            genreMoviesWAverages[k] = movie_to_average_rating[k]
    
    total = 0
    for k in genreMoviesWAverages:
        total += genreMoviesWAverages[k]
    
    return total/len(genreMoviesWAverages)

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    genresWPop = {}
    for k in genre_to_movies:
        if k not in genresWPop.keys():
            genreRating = get_genre_rating(k, genre_to_movies,movie_to_average_rating)
            genresWPop[k] = genreRating
            
    genrePopLH = {}
    genrePopLH = dict(sorted(genresWPop.items(),
                      key= lambda movie: movie[1]))
    genrePopHL = dict(reversed(list(genrePopLH.items())))
    return dict(list(genrePopHL.items())[0: n])

# --- TASK 4: USER FOCUSED ---

# 4.1
def read_user_ratings(f):
    userMovieRatings = {}
    for line in open(f):
        movie, rating, userID = line.split("|")
        if userID.strip() not in userMovieRatings:
            userMovieRatings[userID.strip()] = []
        ratingList = userMovieRatings.get(userID.strip())
        
        ratingList.append([movie.strip(),float(rating)])
    return userMovieRatings

# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    userGenreWMovieRating = {}
    userMovies = []
    for k in user_to_movies:
        if int(k)==user_id:
            userMovies = user_to_movies[k]
    
    for mR in userMovies:
        movieGenre = movie_to_genre[mR[0]]
        if movieGenre not in userGenreWMovieRating:
            userGenreWMovieRating[movieGenre] = []
        genreMoviesList = userGenreWMovieRating.get(movieGenre)
        genreMoviesList.append(mR)
    
    genreWRating = {}
    for k in userGenreWMovieRating:
        genreMoviesList = userGenreWMovieRating.get(k)
        total = 0
        count = 0
        for movie in genreMoviesList:
            total += movie[1]
            count += 1
        genreAverage = total / count
        genreWRating[k] = genreAverage
    
    genreAnswer = ''
    rating = 0
    for k in genreWRating:
        if genreWRating[k]>=rating:
            genreAnswer = k
            rating = genreWRating[k]
   
    return genreAnswer
    

# 4.3
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    userGenre = get_user_genre(user_id,user_to_movies,movie_to_genre)
    popInGenreMovies = get_popular_in_genre(userGenre, create_genre_dict(movie_to_genre), movie_to_average_rating, n=50)
    
    #print(user_to_movies)
    moviesWatched = user_to_movies.get(str(user_id))
    moviesWatchedDic = {}
    for movie in moviesWatched: 
        moviesWatchedDic[movie[0]] = movie[1]
    
    topRec = {}
    count = 0
    for k in popInGenreMovies: 
        if k not in moviesWatchedDic.keys():
            topRec[k] = popInGenreMovies[k]
            count += 1
        if count==3:
            break 
    return topRec
# --- main function for your testing ---
def main():
    
main()
