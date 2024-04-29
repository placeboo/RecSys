from surprise import Reader, Dataset
from surprise.model_selection import train_test_split, LeaveOneOut
from src.constant import USER_ID_NAME, MOVIE_ID_NAME, RATING_NAME

def data_split(rating_df, test_size=0.2, random_state=17):
    """
    :param rating_df: pandas.DataFrame, rating data. It must have three columns, corresponding to the user (raw) ids, the item (raw) ids, and the ratings, in this order.
    :param test_size: float, default 0.2, test size ratio.

    :return: trainset, testset, where trainset is Trainset object from surprise library, testset is list of tuples.
    """
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(rating_df[[USER_ID_NAME, MOVIE_ID_NAME, RATING_NAME]], reader)
    trainset, testset = train_test_split(data, test_size=test_size, random_state=random_state)
    return trainset, testset

def left_out_split(rating_df, random_state=17):
    """
    :param rating_df: pandas.DataFrame, rating data. It must have three columns, corresponding to the user (raw) ids, the item (raw) ids, and the ratings, in this order.

    :return: loo, where loo is LeaveOneOut object from surprise library.
    """
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(rating_df[[USER_ID_NAME, MOVIE_ID_NAME, RATING_NAME]], reader)
    loo = LeaveOneOut(n_splits=1, random_state=random_state)
    trainset_loo, testset_loo = list(loo.split(data))[0]
    return trainset_loo, testset_loo