# Team Process Mapping Take-Home Task: Mahika Calyanakoti.

Goal: In this pre-test, you will first read brief selections from two social science papers (Step 1). You will then go through an end-to-end implementation of a feature and apply it to a dataset of team conversations (Step 2). Finally, you will write a reflection on how well you think this feature extractor performed on the data, as well as how well it performs in operationalizing social science constructs (Step 3).

The idea behind this task is to give you a flavor of the scope of our work — to show how we take inspiration from social science, then apply these ideas in a computational way.

Please write your reflection in this README document.

## 1. High-Level Questions
1a. Which dataset did you choose?

> I used the CSOP dataset, which is the smaller dataset. As mentioned in the write up: "this is a (real) dataset of team conversations by Amazon Mechanical Turk workers. They are playing a game known as the ‘Constraint Satisfaction and Optimization Problem,’ or CSOP". There are about 5,000 observations in this dataset.

1b. What method(s) did you choose? In 1-2 sentences each, describe your sentiment analysis method(s).

> The sentiment analysis I used was Twitter-roBERTa-base for Sentiment Analysis. It was trained on 124 million Tweets from between 2018 and 2021. Based on page 17 of the paper describing this task, the model uses AvgRec (Average Recall) to take the average of the recall with respect to positive, neutral, and negative classes. Two secondary measures, accuracy and F1 PN, are also used, where F1 is a macro average of the positive and negative classes only.
>
> Paper: SemEval-2017 Task 4: Sentiment Analysis in Twitter
> @inproceedings{barbieri2020tweeteval,
  title={{TweetEval:Unified Benchmark and Comparative Evaluation for Tweet Classification}},
  author={Barbieri, Francesco and Camacho-Collados, Jose and Espinosa-Anke, Luis and Neves, Leonardo},
  booktitle={Proceedings of Findings of EMNLP},
  year={2020}
}

1c. Does your method capture any of the ideas from Troth et al. and West et al.? If so, which ones?

> [YOUR ANSWER]

1d. Compared to how Troth et al. and West et al. measured positivity, what are some strengths and weaknesses of your approach?

> [YOUR ANSWER]

## 2. Method evaluation
Next, we would like you to consider how you would evaluate your method. How do you know the classification or quantification of emotion is “right?” Try to think critically!

2a. Open up your output CSV and look at the columns you generated. Do the values “make sense” intuitively? Why or why not?

> Looking at the output csv for the chat-level, the values do make sense intuitively. As a first check, the probabilities across positive, neutral, and negative do sum to 1 for each row. Further, based on inuition, I evaluated specific rows that have fairly skewed values, and the all mostly make sense. For instance, row 184 "541 very good" has a positive probability of 0.94, which makes sense. For a negative example, line 237 "what are you doing our score is lower now" clearly shows a tone of frustration or anger, which is captured by the negative probability sentiment score of 0.84. Lastly, for a neutral example, in line 241 "that work?", a very neutral statement with no strong sentiment, the model outputted 0.63 for the neutral classification, which makes sense. Many other examples throughout the CSV support this notion that the model generated values that make sense.

2b. Propose an evaluation mechanism for your method(s). What metric would you use (e.g., F1, AUC, Accuracy, Precision, Recall)?

> For evaluating the sentiment analysis method, I would propose using a combination of precision, recall, and F1-score. These metrics provide a comprehensive view of the model's performance across different aspects of sentiment classification. Along with these, another useful metric would be accuracy. Accuracy measures the overall correctness of the model across all classes, giving a general understanding of its performance. However, accuracy alone might not be enough, especially in cases of class imbalance where one sentiment class dominates the dataset. Therefore, precision, recall, and F1-score offer a more nuanced evaluation by considering true positives, false positives, and false negatives individually for each sentiment class (positive, neutral, negative). Combining these metrics, you can better assess the model's ability to correctly classify instances across all sentiment categories. This would provide a comprehensive evaluation of how effective the model is.

2c. Describe the steps you would take in evaluating this method. Be as specific as possible.

> [YOUR ANSWER]

2d. Given the nature of these datasets, what challenges do you anticipate that you may encounter during evaluation? How would you go about resolving them?

> [YOUR ANSWER]

## 3. Overall reflection
3a. How much time did it take you to complete this task? (Please be honest; we are looking for feedback to make sure the task is scoped appropriately, as this is one of the first times we’re using this task.)

> This took me about 5 hours (1 hour for reading, 2 hours for choosing a sentiment analysis model, implementing it, and obtaining the csv output), and 2 hours for Part 3).

3b. Finally, provide an overall reflection of your experience. How did you approach this task? What challenge(s) did you encounter? If you had more time, what are additional extensions, improvements, or tests that you would want to implement?

> [YOUR ANSWER]
