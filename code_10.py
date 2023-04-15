from yelpapi import YelpAPI
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = "_2OMY6ojK2plDlNROhYCdsB86PRF-n31bxsn7JpOXLg2bu10nl8R1hm67ImVfuatWcNYKay4mdi6lEIiNJ3Zw4QzQxxEL3cxO2XaqJWipDnk5I7nwxq-ylsJi4YzZHYx"
yelp_api = YelpAPI(api_key)
search_term = "sushi"
search_location = "El Paso, TX"
search_sort_by = 'rating'#best_mstch, rating, review_count, distance
search_limit = 20
search_results = yelp_api.search_query(term=search_term, location=search_location,sort_by = search_sort_by, limit=search_limit, offset = 20)
result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df['alias'])
#result_df.to_csv("inclass_yelpapi.csv")

analyzer = SentimentIntensityAnalyzer()

#reviews_query   'matsuharu-japanese-restaurant-el-paso'
print('Sample 1')
print('matsuharu')
id_for_reviews1 = 'matsuharu-japanese-restaurant-el-paso'
reviews_result = yelp_api.reviews_query(id=id_for_reviews1)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df['text'])
reviews_df.to_csv(f"{id_for_reviews1}_reviews_")
print('\n')

for reviews in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(reviews)
    print('Review')
    print(reviews)
    print('Setimenet Score')
    print(sentiment_score)
    print('\n')

print('\n\n')
#reviews_query  'nomi-el-paso'
print('Sample 2')
print('nomi')
id_for_reviews2 = 'nomi-el-paso'
reviews_result = yelp_api.reviews_query(id=id_for_reviews2)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df['text'])
reviews_df.to_csv(f"{id_for_reviews2}_reviews_")
print('\n')

for reviews in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(reviews)
    print('Review')
    print(reviews)
    print('Setimenet Score')
    print(sentiment_score)
    print('\n')

print('\n\n')
#reviews_query 'kaizen-sushi-el-paso'
print('Sample 3')
print('kaizen')
id_for_reviews3 = 'kaizen-sushi-el-paso'
reviews_result = yelp_api.reviews_query(id=id_for_reviews3)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df['text'])
reviews_df.to_csv(f"{id_for_reviews3}_reviews_")
print('\n')

for reviews in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(reviews)
    print('Review')
    print(reviews)
    print('Setimenet Score')
    print(sentiment_score)
    print('\n')

print('\n\n')
#reviews_query   'aki-sushi-el-paso'
print('Sample 4')
print('aki')
id_for_reviews4 = 'aki-sushi-el-paso'
reviews_result = yelp_api.reviews_query(id=id_for_reviews4)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df['text'])
reviews_df.to_csv(f"{id_for_reviews4}_reviews_")
print('\n')

for reviews in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(reviews)
    print('Review')
    print(reviews)
    print('Setimenet Score')
    print(sentiment_score)
    print('\n')

print('\n\n')
#reviews_query  'hamachi-sushi-el-paso'
print('Sample 5')
print('hamchi')
id_for_reviews5 = 'hamachi-sushi-el-paso'
reviews_result = yelp_api.reviews_query(id=id_for_reviews5)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df['text'])
reviews_df.to_csv(f"{id_for_reviews5}_reviews_")
print('\n')

for reviews in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(reviews)
    print('Review')
    print(reviews)
    print('Setimenet Score')
    print(sentiment_score)
    print('\n')

print('\n\n')

#reviews_query 'riyoma-el-paso'
print('Sample 6')
print('riyoma')
id_for_reviews6 = 'riyoma-el-paso'
reviews_result = yelp_api.reviews_query(id=id_for_reviews6)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df['text'])
reviews_df.to_csv(f"{id_for_reviews6}_reviews_")
print('\n')

for reviews in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(reviews)
    print('Review')
    print(reviews)
    print('Setimenet Score')
    print(sentiment_score)
    print('\n')
  
print('\n\n')

#reviews_query 'koze-el-paso'
print('Sample 7')
print('koze')
id_for_reviews7 = 'koze-el-paso'
reviews_result = yelp_api.reviews_query(id=id_for_reviews7)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df['text'])
reviews_df.to_csv(f"{id_for_reviews7}_reviews_")
print('\n')

for reviews in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(reviews)
    print('Review')
    print(reviews)
    print('Setimenet Score')
    print(sentiment_score)
    print('\n')

print('\n\n')










