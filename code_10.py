import ssl
import nltk 


ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

reviews = open('tacos_reviews.txt')

for review in reviews:
    tokens = nltk.word_tokenize(review)
    print(tokens)

    pos_tags = nltk.pos_tag(tokens)
    print(pos_tags)

    for token in tokens:
        if token[1] == 'JJ' or token[1] == 'JJS':
         #print(token[0])
         print(token)