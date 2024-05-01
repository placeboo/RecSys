from surprise import KNNBasic, SVD
from tqdm.notebook import tqdm

class RecommenderBase:
    """base class for all recommender"""
    def fit(self, trianset):
        raise NotImplementedError
    def predict(self, uid, iid, r_ui=None, verbose=False):
        raise NotImplementedError
    def test(self, testset):
        raise NotImplementedError

class KNNRecommender(RecommenderBase):
    def __init__(self, *args, **kwargs):
        self.model = KNNBasic(*args, **kwargs)
    def fit(self, trainset):
        self.model.fit(trainset)
    def predict(self, uid, iid, r_ui=None, verbose=False):
        return self.model.predict(uid=uid, iid=iid, r_ui=r_ui, verbose=verbose)
    def test(self, testset):
        return self.model.test(testset, verbose=False)

class EmbeddingRecommender(RecommenderBase):
    def __init__(self, *args, **kwargs):
        pass
    def fit(self, trainset):
        pass
    def predict(self, uid, iid, r_ui=None, verbose=False):
        pass
    def test(self, testset):
        pass

