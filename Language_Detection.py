import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Function to remove non-ASCII characters from text
def sanitize_text(text):
    return ''.join(char for char in text if ord(char) < 128)

def train_language_model():
    # Sample training data with only ASCII characters
    train_texts = [
        "This is an English sentence.",  # English
        "Another English sentence.",  # English
        "Ceci est une phrase francaise.",  # French
        "Une autre phrase francaise.",  # French
        "Dies ist ein deutscher Satz.",  # German
        "Ein weiterer deutscher Satz.",  # German
        "Esta es una oracion en espanol.",  # Spanish
        "Otra oracion en espanol."  # Spanish
    ]
    
    train_labels = ["English", "English", "French", "French", "German", "German", "Spanish", "Spanish"]
    
    # Create a vectorizer + classifier pipeline
    model = make_pipeline(CountVectorizer(analyzer='char', ngram_range=(3, 3)), MultinomialNB())
    
    # Train the model
    model.fit(train_texts, train_labels)
    
    return model

def main():
    # Train the model once
    model = train_language_model()
    
    # Read input
    input_text = sys.stdin.read().strip()
    
    # Sanitize input to remove non-ASCII characters
    sanitized_text = sanitize_text(input_text)
    
    # Predict the language
    language = model.predict([sanitized_text])[0]
    
    print(language)

if __name__ == '__main__':
    main()
