from collections import defaultdict

def get_top_n(predictions, n=5, threshold=4):
    """
    Get top N recommendation for each user.
    :param predictions: A list of prediction object from surprise. The prediction object is a tuple containing:
        uid: raw user id
        iid: raw item id
        r_ui: (float) true rating
        est: (float) estimated rating
        details: (dict) details of prediction
    :param n: int, default 5, top N recommendation.
    :param threshold: int, default 4, threshold rating for recommendation.

    :return: A dict where keys are user (raw) ids and values are list of tuples [(raw item id, estimated rating), ...]
    """
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        if est >= threshold:
            top_n[uid].append((iid, est))
    # Then sort the predictions for each user and retrieve the N highest ones.

    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n
