from dataclasses import dataclass
from typing import Tuple

import pandas as pd
from src.constant import *
@dataclass
class RawDataPaths:
    """
    Raw data paths
    Args:
        rating_path: path to rating data
        movie_path: path to movie data
        user_path: path to user data
    """
    rating_path: str
    user_path: str
    movie_path: str

def load_raw_data(raw_data_paths: RawDataPaths) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Load raw data
    Args:
        raw_data_paths: raw data paths
    Returns:
        rating_df: rating data
        movie_df: movie data
        user_df: user data
    """
    # movie
    movie_df = pd.read_csv(raw_data_paths.movie_path,  delimiter='::', header=None, engine='python', encoding='latin-1')
    # remove year from title and add year column
    movie_df[3] = movie_df[1].str.extract(r"\((\d{4})\)$")
    movie_df[1] = movie_df[1].str.replace(r"\(\d{4}\)$", "", regex=True)
    movie_df[2] = movie_df[2].str.split("|")
    movie_df.columns = MOVIE_COLUMN_NAMES

    # rating
    rating_df = pd.read_csv(raw_data_paths.rating_path, delimiter='::', header=None, engine='python', encoding='latin-1')
    rating_df.columns = RATING_COLUMN_NAMES

    # user
    user_df = pd.read_csv(raw_data_paths.user_path, delimiter='::', header=None, engine='python', encoding='latin-1')
    user_df.columns = USER_COLUMN_NAMES
    # map occupation
    user_df[USER_COLUMN_NAMES[3]] = user_df[USER_COLUMN_NAMES[3]].map(OCCUPATION_MAP)

    return rating_df, movie_df, user_df

