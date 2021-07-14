# Q1.1
# ------------------
# Write your implementation here.
list_1d = [word for page in corpus for word in page]
corpus_words = sorted(set(list_1d))
num_corpus_words = len(corpus_words)
# ------------------
# Q1.2
# ------------------
# Write your implementation here.
for i in range(num_words):
    word2ind[words[i]] = i

for f in corpus:
    for j, center_word in enumerate(f):
        ind = word2ind[center_word]

        win_slice = f[j - window_size : j] + f[j + 1: j + window_size + 1]

        for context_word in win_slice:
            ind_c = word2ind[context_word]
            M[ind, ind_c] += 1
# ------------------
# Q1.3
# ------------------
# Write your implementation here.
svd = TruncatedSVD(n_components=k, n_iter=n_iters)
M_reduced = svd.fit_transform(M)
# ------------------
# Q1.4
# ------------------
# Write your implementation here.
plt.figure(figsize=(6,6))
ys = []
xs = []

for word in words:
    ind = word2ind[word]
    x = M_reduced[ind, 0]
    y = M_reduced[ind, 1]

    xs.append(x)
    ys.append(y)
    # plt.text(x+0.1, y+0.1, word)

plt.scatter(xs, ys, edgecolors='k', c='r')

for i in range(len(xs)):
    plt.text(xs[i]+0.001, ys[i], words[i])
plt.show()
# ------------------
# Q1.5-Explanation
# Here words like petroleum, energy, barrels, bpd and oil must be closer to each other. Oil is a singular cluster which I think it shouldn't be.
# iraq, ecuador, and kuwait are clustered together, regarding that all three are countries.
# ------------------
# Q2.1-Explanation
# Here ecuador, iraq, and petroleum are clustered together, I think because they are related in a oil-business way!
# industry and energy are clustered also.
# I think Kuwait should have been clustred with iraq and ecuador because kuwait is also a major oil exporter country.
# The plots are different because in this method more attention is payed to the overall repeat count of the word, not repeating under a window.
# ------------------
# Q2.2
# ------------------
# Write your implementation here.
wv_from_bin.most_similar('mouse')
# ------------------
# Q2.2-Explanation
# I tried 'apple' and all the top 10 similar words were regarding the Apple Inc., not the apple fruit. I think because under the context that this model is trained, the word apple was most reffered to the company, not the fruit.
# ------------------
# Q2.3
# ------------------
# Write your implementation here.

w1 = 'good'
w2 = 'awesome'
w3 = 'bad'

w1w2 = wv_from_bin.distance(w1, w2)
print(w1w2)

w1w3 = wv_from_bin.distance(w1, w3)
print(w1w3)
# ------------------
# Q2.3-Explanation
# I think that the word good is the exact antonym for bad, they are very direct for each other, but something like awesome has a meaning close to good, but is not directly a synonym to good. Because of this the similarity probability is less for awesome.
# ------------------
# Q2.4-Explanation
# x = King - Man + Woman
# ------------------
# Q2.5
# ------------------
# Write your implementation here.
pprint.pprint(wv_from_bin.most_similar(positive=['usa', 'indian'], negative=['india']))
# ------------------
# Q2.5-Explanation
# indian : india  ::  american : usa
# x = Indian - India + USA
# ------------------
# Q2.6
# ------------------
# Write your implementation here.
pprint.pprint(wv_from_bin.most_similar(positive=['dislike', 'love'], negative=['like']))
# ------------------
# Q2.6-Explanation
# x = love - like + dislike
# like : love :: dislike : hate
# The right andswer is 'hate', but the prediction is 'affection' which is not right.
# ------------------
# Q2.7-Explanation
# The female list contains words like 'mother', 'nurse', 'homemaker', and 'pregnant!!' which are not related to working and jobs; on the contrary, the male list contains words which are very related to jobs and working.
# It reflects a gender bias of females not working in society, the traditional bias that women should work in homes and not work alongside men.
# ------------------
# Q2.8
# ------------------
# Write your implementation here.
pprint.pprint(wv_from_bin.most_similar(positive=['mother', 'doctor'], negative=['father']))
print()
pprint.pprint(wv_from_bin.most_similar(positive=['father', 'doctor'], negative=['mother']))
# ------------------
# Q2.8-Explanation
# father to doctor is similar to mother to nurse. It can reflect a gender bias in this way, women are nurses and men are doctors.
# I used example in "Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings" of Tolga Bolukbasi et al. paper, 2016.
# ------------------
# Q2.9-Explanation
# I think this models are traind on a text data in which some jobs or titles are more associated with men, rather than women. So when the model is trained on such corpus, it can have a gender bias on some topics (like jobs discussed above).
# ------------------
