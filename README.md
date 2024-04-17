# RecSys Study Collection

This repo serves as a study collection of resources for the Recommender System.

## Table of Contents

- [Papers](#papers)
- [Blogs](#blogs)
  - [Deep Learning based Recommender System](#deep-learning-based-recommender-system)
  - [Debias](#debias)
- [Other techniques](#other-techniques)
    - [Embedding](#embedding)

## Papers

### Deep Learning based Recommender System
- Zhang, S., Yao, L., Sun, A., & Tay, Y. (2019). Deep Learning based Recommender System: A Survey and New Perspectives. https://doi.org/10.1145/3285029
- Covington, P., Adams, J., & Sargin, E. (2016). Deep neural networks for youtube recommendations. RecSys 2016 - Proceedings of the 10th ACM Conference on Recommender Systems, 191–198. https://doi.org/10.1145/2959100.2959190
>This paper introduces a deep neural network architecture for YouTube recommendations, which is a large-scale and real-world recommendation system. The architecture consists of two components: candidate generation and ranking. The candidate generation component is responsible for selecting a small set of videos from a large pool of candidates, while the ranking component ranks these candidates to generate the final recommendations. The candidate generation component uses a deep neural network to predict the probability of a user watching a video, while the ranking component uses another deep neural network to predict the click-through rate of the videos. The paper demonstrates that the proposed architecture significantly improves the performance of the YouTube recommendation system compared to traditional methods.
- Yi, X., Yang, J., Hong, L., Cheng, D. Z., Heldt, L., Kumthekar, A., Zhao, Z., Wei, L., & Chi, E. (2019). Sampling-bias-corrected neural modeling for large corpus item recommendations. RecSys 2019 - 13th ACM Conference on Recommender Systems, 269–277. https://doi.org/10.1145/3298689.3346996
- Guo, H., Yu, J., Liu, Q., Tang, R., & Zhang, Y. (2019). PAL: A position-bias aware learning framework for CTR prediction in live recommender systems. RecSys 2019 - 13th ACM Conference on Recommender Systems, 452–456. https://doi.org/10.1145/3298689.3347033

## Blogs
### Deep Learning based Recommender System
- [Deep Learning in Recommender Systems: A Primer](https://towardsdatascience.com/deep-learning-in-recommender-systems-a-primer-96e4b07b54ca)
> This blog gives a tour of the most import modeling breakthrough. Papers also cited, which are worth reading.
- [Candidate Generation Using a Two Tower Approach With Expedia Group Traveler Data](https://medium.com/expedia-group-tech/candidate-generation-using-a-two-tower-approach-with-expedia-group-traveler-data-ca6a0dcab83e)
>This blog post, brought by Expedia Group Tech, introduces an innovative two-tower approach for candidate generation within recommendation systems. The two-tower architecture is widely utilized in recommendation systems, comprising a neural network structure consisting of two key components: the query tower and the candidate tower. The query tower encodes the user's query, while the candidate tower encodes the candidate items. These towers are then integrated to generate a score reflecting the relevance of the candidate items to the user's query. Demonstrated to be highly effective across various recommendation tasks such as click prediction, item recommendation, and ranking, the two-tower approach offers promising results. Additionally, the blog provides insightful implementation details along with dataset and code samples. [Repo](https://github.com/ExpediaGroup/two-tower-lodging-candidate-generation)

### Debias
- [Correct Sampling Bias for Recommender Systems](https://medium.com/towards-data-science/correct-sampling-bias-for-recommender-systems-d2f6d9fdddec)
> A high level explanation of method in Paper " Sampling-bias-corrected neural modeling for large corpus item recommendations."
- [The Rise of Two-Tower Models in Recommender Systems](https://medium.com/towards-data-science/the-rise-of-two-tower-models-in-recommender-systems-be6217494831) 
> A high level explanation of debias method in Paper "PAL: A position-bias aware learning framework for CTR prediction in live recommender systems"
## Other techniques

### Embedding
- [Neural Network Embeddings Explained](https://towardsdatascience.com/neural-network-embeddings-explained-4d028e6f0526)
> This blog explains the concept of neural network embeddings, their importance, and the process of learning them. It uses a practical example to illustrate these concepts: creating a book recommendation system by representing all books on Wikipedia as vectors.
- [Practical Recommendation System 01 : Embedding Techniques](https://medium.com/數學-人工智慧與蟒蛇/推薦系統實務-一-embedding-技巧-a4cc69775b18)
