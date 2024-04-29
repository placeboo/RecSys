from src.data_loader import load_raw_data, RawDataPaths
from src.data_split import data_split

def main(
        RAW_DATA_PATHS: RawDataPaths,
        test_size: float = 0.2,
        random_state: int = 17
):
    # load the raw data (had minor data processing)
    rating_df, movie_df, user_df = load_raw_data(RAW_DATA_PATHS)
    trainset, testset = data_split(rating_df, test_size=test_size, random_state=random_state)




if __name__ == '__main__':
    RAW_DATA_PATHS = RawDataPaths(
        rating_path="data/raw/ml-1m/ratings.dat",
        movie_path="data/raw/ml-1m/movies.dat",
        user_path="data/raw/ml-1m/users.dat"
    )
    main(RAW_DATA_PATHS)