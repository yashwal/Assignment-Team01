import sys
sys.path.append('..')

import numpy as np 
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer 
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from recommendations.dao.retrieve import *


def convert(obj):
        return [obj]

def tolist(obj):
    return obj.split()

def concat(obj):
    return ' '.join(obj)

def stemmer(text):
    ps = PorterStemmer()
    ret_list = []
    for i in text.split():
        ret_list.append(ps.stem(i))
    return " ".join(ret_list)

def recommend(prod,df,similarity):
    prod_index = df[df['uniqueID'] == prod].index[0]
    distance = similarity[prod_index]
    prod_list = sorted(list(enumerate(distance)),reverse = True,key = lambda x:x[1])[1:5]
    return prod_list

def pkldump():
    df = pd.DataFrame(columns=['uniqueID','title','price','description','catLevel1','catLevel2'])

    data = all_products()

    parent_id = {'0':'men','1':'women','2':'exp'}

    count = 0
    for i in data:
        product_id=str(i[0])
        title=str(i[1])
        price=float(i[2])
        description= i[3]
        cat1 = parent_id[i[4]]
        cat2 = i[5].replace(" ",'')
        temp_df = [product_id,title,price,description,cat1,cat2]
        df.loc[count] = temp_df
        count += 1

    print(df.head())
    df['catLevel1'] = df['catLevel1'].apply(convert)
    df['catLevel2'] = df['catLevel2'].apply(convert)
    
    df['description'] = df['description'].apply(tolist)
    df['title'] = df['title'].apply(tolist)

    df['tags'] = df['title'] + df['description'] + df['catLevel1'] + df['catLevel2']
    df['tags'] = df['tags'].apply(lambda x:[i.replace(" ","") for i in x])
    df['tags'] = df['tags'].apply(concat)
    df['title'] = (df['title'].apply(concat)).apply(lambda x:x.lower())
    new_df = df[['uniqueID','title','tags']]
   

    cv = CountVectorizer(max_features=5000,stop_words='english')
    vectors = cv.fit_transform(new_df['tags']).toarray()

    new_df['tags'] = new_df['tags'].apply(stemmer)

    similarity = cosine_similarity(vectors)
    pickle.dump(similarity,open('similarity_matrix.pkl','wb'))
    pickle.dump(new_df,open('data.pkl','wb'))

def getRecommendation(input_value):
    similarity = pickle.load(open('similarity_matrix.pkl','rb'))
    new_df = pickle.load(open('data.pkl','rb'))
    if(input_value not in new_df['uniqueID'].values):
        return []
    prods = recommend(input_value,new_df,similarity)
    res = []
    for i in prods:
        res.append(new_df.iloc[i[0]].uniqueID)
    return res

