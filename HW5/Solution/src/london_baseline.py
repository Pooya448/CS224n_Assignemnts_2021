# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import utils

eval_corpus_path = "./birth_dev.tsv"

corpus = open(eval_corpus_path).readlines()
n_tokens = len(corpus)
predictions = ['London'] * n_tokens

total, correct = utils.evaluate_places(eval_corpus_path, predictions)
if total > 0:
        print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
