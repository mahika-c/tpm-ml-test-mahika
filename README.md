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

> Troth et al. and West et al. talk about positivity measures in teams. Specifically, in the diagram on page 701 of Troth et al., we can see the classification of individual versus team based emotional awareness and control. In the task that I completd, I focused more on the chat-level sentiment analysis, which would relate more to the individual metrics mentioned in Troth et al. Later on page 708, we see that inability to control one's emotions, such as when feeling frustrated, correlated to more negative sentiments. This is reflected by the Twitter-trained model I used; as you can see in the csv, in line 237, the chat message "what are you doing our score is lower now" correlates to a negativity score of 0.84 due to the frustrated tone. The model I used also relates to the measures of positivity in team communications mentioned in West et al.: Team optimism, team efficacy, and team resilience (page 256). The model I used looks for words that are associated with optimisim to provide higher positive probabilities, such as the message "very good" in line 184 being assigned a positive probability of 0.94.

1d. Compared to how Troth et al. and West et al. measured positivity, what are some strengths and weaknesses of your approach?

> Compared to Troth et al. and West et al.'s methodologies for measuring positivity in team communications, my approach analyzes sentiment at the chat level more (I analyzed the chat level csv primarily), providing a more granular understanding of individual interactions. Using ML models allows for automated processing of large datasets efficiently, reducing manual effort. However, my approach might lack contextual understanding and domain-specific knowledge, potentially leading to misinterpretations of sentiment nuances within CSOP conversations. The methods discussed in the papers, on the other hand, are more survey and human-based, so they are fine tuned to the exact context. While flexible and adaptable to different language styles, my model might struggle to capture multimodal cues in team interactions, like tone or emoticons. Despite these limitations, its scalability and automation make it a good tool for analyzing extensive text data, allowing for insights into overall sentiment dynamics within teams.

## 2. Method evaluation
Next, we would like you to consider how you would evaluate your method. How do you know the classification or quantification of emotion is “right?” Try to think critically!

2a. Open up your output CSV and look at the columns you generated. Do the values “make sense” intuitively? Why or why not?

> Looking at the output csv for the chat-level, the values do make sense intuitively. As a first check, the probabilities across positive, neutral, and negative do sum to 1 for each row. Further, based on inuition, I evaluated specific rows that have fairly skewed values, and the all mostly make sense. For instance, row 184 "541 very good" has a positive probability of 0.94, which makes sense. For a negative example, line 237 "what are you doing our score is lower now" clearly shows a tone of frustration or anger, which is captured by the negative probability sentiment score of 0.84. Lastly, for a neutral example, in line 241 "that work?", a very neutral statement with no strong sentiment, the model outputted 0.63 for the neutral classification, which makes sense. Many other examples throughout the CSV support this notion that the model generated values that make sense.

2b. Propose an evaluation mechanism for your method(s). What metric would you use (e.g., F1, AUC, Accuracy, Precision, Recall)?

> For evaluating the sentiment analysis method, I would propose using a combination of precision, recall, and F1-score. These metrics provide a comprehensive view of the model's performance across different aspects of sentiment classification. Along with these, another useful metric would be accuracy. Accuracy measures the overall correctness of the model across all classes, giving a general understanding of its performance. However, accuracy alone might not be enough, especially in cases of class imbalance where one sentiment class dominates the dataset. Therefore, precision, recall, and F1-score offer a more nuanced evaluation by considering true positives, false positives, and false negatives individually for each sentiment class (positive, neutral, negative). Combining these metrics, you can better assess the model's ability to correctly classify instances across all sentiment categories. This would provide a comprehensive evaluation of how effective the model is.

2c. Describe the steps you would take in evaluating this method. Be as specific as possible.

> (1) Data Preparation: Make sure that the evaluation dataset is separate from the training & testing datasets (avoids data leakage). Each observation should be matched with a ground truth label for sentiment (positive, neutral, or negative).

> (2) Prediction Generation: Run the trained sentiment analysis model on the evaluation dataset. This will generate predicted sentiment labels for each observation.

> (3) Evaluation Metrics Calculation to Analyze the Model:

> Precision: Calculate the proportion/percentage of correctly predicted positive instances out of all instances predicted as positive. You should do this for neutral and negative as well.
> Recall: Compute the proportion of correctly predicted positive instances out of all actual positive instances. Again, you should do this for neutral and negative as well.
> F1-score: Find the harmonic mean of precision and recall, which thus provides a balanced evaluation metric.
Confusion Matrix: You can also make a confusion matrix to visualize the models' performance across the 3 sentiment classes to see where the model performs well or struggles.

> (4) Analyzing Errors: Look into misclassified instances to see patterns or frequent mistakes for the model to know what areas to target for improvement.

> (5) Cross-validation: You could also use k-fold cross-validation to more robustly evaluate the results. This randomly splits the data and into k groups and iteratively uses different partitions as the training vs testing data, calculating the errors for each iteration.

> (6) Compare with Baselines/Other Models: Compare the performance of our sentiment analysis model with baseline models to get a better understanding of its effectiveness.

> (7) Documentation: Document the evaluation results and methodology followed. Also write down any observations made during the evaluation process. This can help with future improvements and analyses, and will document the problem areas of the model.

2d. Given the nature of these datasets, what challenges do you anticipate that you may encounter during evaluation? How would you go about resolving them?

> Given the nature of the CSOP dataset, various challenges can arise during evaluation. One challenge might be the use of nuanced and context-dependent language within the conversations, which could make sentiment classification subjective and lead to interpretation errors. Also, the dataset might have class imbalance, with certain sentiment classes being more represented than others. This can skew the evaluation metrics and affect the model's performance evaluation. Further, since the dataset has a conversational nature, this can introduce noise/ambiguity, so the sentiment analysis model might have trouble accurately categorizing the underlying sentiment.
>
> To resolve these challenges, the code would need careful preprocessing of the text to handle noise and context. There might need to be model training for emojis/emoticons and punctuation, since omitting punctuation altogether might get rid of the sentiment intended by the person. The code would also need to ensure balanced sampling strategies for evaluation, and might be able to use domain-specific features to improve the model's understanding of the CSOP conversations. Additionally, using qualitative analysis alongside quantitative evaluation can provide deeper insights into the model's performance, including any inherent biases or limitations in the dataset.

## 3. Overall reflection
3a. How much time did it take you to complete this task? (Please be honest; we are looking for feedback to make sure the task is scoped appropriately, as this is one of the first times we’re using this task.)

> This took me about 5 hours (1 hour for reading, 2 hours for choosing a sentiment analysis model, implementing it, and obtaining the csv output), and 2 hours for Part 3).

3b. Finally, provide an overall reflection of your experience. How did you approach this task? What challenge(s) did you encounter? If you had more time, what are additional extensions, improvements, or tests that you would want to implement?

> I started my approach of this task by first reading the literature provided the outlines some of the metrics and factors that impact conversation level and chat level analyses. By internalizing this information, I could better handle the task with the proper background knowledge. Through these readings, I learned about what measures sociologists/psychologists/researchers use to evaluate the positive/neutral/negative sentiments of interactions in teams, as well as personal metrics as well. Then, I looked into hugging face to find a sentiment analysis model that aligned with some of these ideas from the reading to start to implement my feature. I looked into some of the example code provided on the website for the specific Twitter model I ended up using. In this process, one challenge I faced was making sure the sentiment analysis model was robust across various conversational contexts included in the CSOP dataset. Since the dataset could have a wide range of conversational styles, tones, and topics, it was challenging to find a one-size-fits-all sentiment analysis solution. Also, accurately capturing the sentiment in short, informal messages in chat conversations is inherently challenging because of the lack of explicit sentiment cues and the presence of sarcasm, humor, and ambiguity. Given more time, I would want to implement many different extensions, improvements, and tests to improve the sentiment analysis model's performance and make the model more generalizable. One thing that can be done is using domain experts to verify the true sentiments of different messages to evaluate against the model's generated sentiments, thus allowing for iterative improvements and human-based training processes. Further, I could explore multimodal sentiment analysis by including other features like images, emojis, or user metadata for additional context and cues for sentiment classification. Another extension would be to incorporate domain-specific sentiment lexicons, specifically for the CSOP conversations, to better understand domain-specific sentiment nuances. Further, I could try leveraging the strengths of multiple models for a sentiment analysis model for the CSOP dataset. Lastly, I could iteratively label the most informative observations from the dataset for manual annotation to improve the model's performance with minimal manual effort. Overall, these efforts can fine tune the model for improved sentiment analysis performance with a better understanding of non-text-based sentiment (emojis, etc.), domain-specifc context for the CSOP dataset, sentiment nuance, and human-based model training.
