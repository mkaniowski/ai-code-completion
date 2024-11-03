
# Ai Code Completion

A brief description of what this project does and who it's for


## Introduction

This project aims to evaluate the performance of an AI model for code completion. The model is tested on a dataset of code snippets, and its performance is measured using various metrics to determine its accuracy and effectiveness.
## Dataset creation

The dataset is created by scraping code files from a specified source directory. The code is split into three parts: prefix, middle, and suffix. The middle part is the target for the code completion task.

Steps:

    1. Scrape Files: Code files are scraped from the source directory.
    2. Split Code: The code is split into prefix, middle, and suffix.
    3. Select Examples: A subset of examples is selected for evaluation.
    4. Generate Completions: The AI model generates completions for the selected examples.
    5. Label Completions: The completions are labeled as correct or incorrect based on a comparison with the middle part.
## Metrics used

The following metrics are used to evaluate the performance of the AI model:

**Exact Match Score:** Measures the percentage of completions that exactly match the middle part.

**chrF Score:** Measures the character n-gram F-score between the completion and the middle part.

**BLEU Score:** Measures the precision of n-grams in the completion compared to the middle part.

**ROUGE-L Score:** Measures the longest common subsequence (LCS) between the completion and the middle part.
## Metrics explanation

**Exact Match Score:** This metric is straightforward and indicates the proportion of completions that are identical to the target middle part.

**chrF Score:** This metric evaluates the similarity between the completion and the target based on character n-grams, providing a finer-grained assessment than exact match.

**BLEU Score:** This metric is commonly used in machine translation and measures how many n-grams in the completion appear in the target.

**ROUGE-L Score:** This metric focuses on the longest common subsequence, which helps in understanding the structural similarity between the completion and the target.
## Findings

The evaluation results are as follows:  
 - Exact Match Score: `0.0800`
- Average chrF Score: `0.1905`
- Average BLEU Score: `0.0270`
- Average ROUGE-L Score: `0.1062`

These scores indicate that the AI model has limited success in generating completions that exactly match the target middle part. However, the chrF, BLEU, and ROUGE-L scores suggest that the completions have some degree of similarity to the target, even if they are not exact matches.
## Conclusion

The AI model for code completion shows potential but requires further improvement to achieve higher accuracy and better performance. The current evaluation metrics provide a comprehensive understanding of the model's strengths and weaknesses. Future work should focus on enhancing the model's ability to generate more accurate and contextually appropriate code completions.