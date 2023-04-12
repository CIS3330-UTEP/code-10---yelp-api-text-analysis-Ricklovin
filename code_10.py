
from yelpapi import YelpAPI
import pandas as pd


api_key = "_2OMY6ojK2plDlNROhYCdsB86PRF-n31bxsn7JpOXLg2bu10nl8R1hm67ImVfuatWcNYKay4mdi6lEIiNJ3Zw4QzQxxEL3cxO2XaqJWipDnk5I7nwxq-ylsJi4YzZHYx"
yelp_api = YelpAPI(api_key)

search_term = "sushi"
search_location = "El Paso, TX"
search_sort_by = 'rating'#best_mstch, rating, review_count, distance
search_limit = 20


search_results = yelp_api.search_query(term=search_term, location=search_location,sort_by = search_sort_by, limit=search_limit, offset = 0)

result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df['alias'])
#result_df.to_csv("inclass_yelpapi.csv")

#reviews_query
id_for_reviews = 'matsuharu-japanese-restaurant-el-paso','tsunami-sushi-el-paso', 'kaizen-sushi-el-paso','aki-sushi-el-paso','hamachi-sushi-el-paso','riyoma-el-paso','koze-el-paso'
reviews_result = yelp_api.reviews_query(id=id_for_reviews)
print(reviews_result)

reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df['text'])
reviews_df.to_csv(f"{id_for_reviews}_reviews_")


