from surprise import KNNBasic, SVD
from tqdm.notebook import tqdm

class KNNRecommender(KNNBasic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def fit(self, trainset):
        pass

    def predict(self, testset):
        pass

class SVDRecommender(SVD):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def fit(self, trainset):
        pass

    def predict(self, testset):
        pass