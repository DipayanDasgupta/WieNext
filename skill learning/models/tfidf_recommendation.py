import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class TFIDFRecommender:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.tfidf_matrix = None

    def train_model(self):
        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.data['description'])

    def recommend_courses(self, course_title):
        indices = pd.Series(self.data.index, index=self.data['title']).drop_duplicates()
        idx = indices[course_title]
        sim_scores = list(enumerate(linear_kernel(self.tfidf_matrix[idx], self.tfidf_matrix)[0]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        course_indices = [i[0] for i in sim_scores]
        return self.data['title'].iloc[course_indices].tolist()
