# define constant variables

OCCUPATION_MAP = {
    0: "other",
    1: "academic/educator",
    2: "artist",
    3: "clerical/admin",
    4: "college/grad student",
    5: "customer service",
    6: "doctor/health care",
    7: "executive/managerial",
    8: "farmer",
    9: "homemaker",
    10: "K-12 student",
    11: "lawyer",
    12: "programmer",
    13: "retired",
    14: "sales/marketing",
    15: "scientist",
    16: "self-employed",
    17: "technician/engineer",
    18: "tradesman/engineer",
    19: "unemployed",
    20: "writer"
}

USER_ID_NAME = 'user_id'
MOVIE_ID_NAME = 'movie_id'
RATING_NAME = 'rating'
RATING_COLUMN_NAMES = [USER_ID_NAME, MOVIE_ID_NAME, RATING_NAME, 'timestamp']
MOVIE_COLUMN_NAMES = [MOVIE_ID_NAME, 'title', 'genres', 'year']
USER_COLUMN_NAMES = [USER_ID_NAME, 'gender', 'age', 'occupation', 'zip_code']



