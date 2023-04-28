import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def extract_keywords(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # Tag words with their part of speech
    tagged_words = nltk.pos_tag(words)

    # Extract technical keywords
    tech_keywords = [word for word, tag in tagged_words if tag.startswith('NN') or tag.startswith('JJ')]

    # Count the frequency of each technical keyword
    freq_dist = Counter(tech_keywords)

    # Get the 12 most common technical keywords
    # اینجا عدد رو تغییر بده
    top_tech_keywords = freq_dist.most_common(12)

    # Sort the keywords alphabetically
    top_tech_keywords = sorted(top_tech_keywords, key=lambda x: x[0])

    # Number the keywords from 1 to 12
    top_tech_keywords = [(i+1, word, freq) for i, (word, freq) in enumerate(top_tech_keywords)]

    return top_tech_keywords


# Read the job description from file
with open('jobdes.txt', 'r') as f:
    job_desc = f.read()

# Extract the keywords
keywords = extract_keywords(job_desc)

# Write the keywords to file
with open('jobkeys.txt', 'w') as f:
    for keyword in keywords:
        f.write(f"{keyword[0]}. {keyword[1]} ({keyword[2]} occurrences)\n")
#تعداد دفعات رو می زند.