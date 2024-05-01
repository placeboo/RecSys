from src.data_loader import load_raw_data, RawDataPaths
from src.data_split import data_split, left_out_split
from src.models import KNNRecommender
from src.evaluation import evaluate_predictions, get_hit_rate
from surprise import NormalPredictor

def main(RAW_DATA_PATHS: RawDataPaths,
        test_size: float = 0.2,
        random_state: int = 17):

    models = {
        'KNN': KNNRecommender()
    }
    # load the raw data (had minor data processing)
    rating_df, movie_df, user_df = load_raw_data(RAW_DATA_PATHS)
    trainset, testset = data_split(rating_df, test_size=test_size, random_state=random_state)
    train_loo, test_loo = left_out_split(rating_df, random_state=random_state)

    results = {}
    for name, model in models.items():
        print(f"---------- Training {name} ----------")
        model.fit(trainset)
        predictions = model.test(testset)
        rmse = evaluate_predictions(predictions, metric='rmse', verbose=True)
        mae = evaluate_predictions(predictions, metric='mae', verbose=True)
        results[name] = {
            'rmse': rmse,
            'mae': mae
        }
    # evaluate hit rate
    for name, model in models.items():
        print(f"---------- Evaluating hit rate for {name} ----------")
        hit_rate = get_hit_rate(model, train_loo, test_loo)
        results[name]['hit_rate'] = hit_rate



if __name__ == '__main__':
    RAW_DATA_PATHS = RawDataPaths(
        rating_path="data/raw/ml-1m/ratings.dat",
        movie_path="data/raw/ml-1m/movies.dat",
        user_path="data/raw/ml-1m/users.dat"
    )
    test_size = 0.2
    random_state = 17
    main(RAW_DATA_PATHS, test_size, random_state)