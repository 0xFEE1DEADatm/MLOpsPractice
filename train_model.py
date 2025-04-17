import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Пример обучающих данных 
X_train = [
    "I love this product", "This is amazing", "Fantastic experience",
    "I hate this", "This is terrible", "Awful and bad"
]
y_train = [1, 1, 1, 0, 0, 0]  # 1 – положительный, 0 – отрицательный

# Создание пайплайна: векторизация + модель
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Обучение
pipeline.fit(X_train, y_train)

# Сохранение модели
joblib.dump(pipeline, 'text_classifier.joblib')
print(" Model saved to text_classifier.joblib")
