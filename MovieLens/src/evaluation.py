from collections import defaultdict
from surprise import accuracy
def evaluate_predictions(predictions, metric, verbose=False):
    """
    :param predictions: the prediction object
    :param metric: the metric to evaluate the prediction, including rmse, mae
    :param verbose: If true, print the evaluation result.
    :return: the evaluation result
    """
    if metric == 'rmse':
        result = accuracy.rmse(predictions, verbose=verbose)
    elif metric == 'mae':
        result = accuracy.mae(predictions, verbose=verbose)
    else:
        raise ValueError(f"Invalid metric: {metric}")
    return result
def get_top_n(predictions, n=5, threshold=4):
    """
    Return the top N recommendations for each user above a specified rating threshold.
    :return: A dict where keys are user (raw) ids and values are list of tuples [(raw item id, estimated rating), ...]
    """
    top_n = defaultdict(list)
    for uid, iid, ture_r, est, _ in predictions:
        if est >= threshold:
            top_n[uid].append((iid, est))
    # Then sort the predictions for each user and retrieve the N highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

def hit_rate(top_n, left_out_prediction):
    """
    :param top_n: the top N recommendation for each user
    :param left_out_prediction: prediction object, the left out prediction of leave-one-out test
    :return: the hit rate, which is the proportion of the top N recommendation contains the left out prediction
    """
    n_hit = 0
    n_total = 0
    for left_out in left_out_prediction:
        user_top_n = top_n.get(left_out.uid, [])
        if any(item for item, _ in user_top_n if item == left_out.iid):
            n_hit += 1
    return n_hit / len(left_out_prediction) if len(left_out_prediction) > 0 else 0

def get_hit_rate(model, train_loo, test_loo):
    """
    :param model: the model to evaluate
    :param train_loo: the training set of leave-one-out
    :param test_loo: the testing set of leave-one-out

    :return: the hit rate of the model
    """
    model.fit(train_loo)
    left_anti_testset = train_loo.build_anti_testset()
    left_out_predictions = model.test(test_loo)
    predictions_anti_testset = model.test(left_anti_testset)
    top_n = get_top_n(predictions_anti_testset)
    return hit_rate(top_n, left_out_predictions)


