from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
import re
from nltk import FreqDist
stop_words=set(stopwords.words("english"))
with open("random_paragraphs.txt","r") as file:
    content = file.read().replace('\n', '')
    text=content
nltk.download('stopwords')
nltk.download('punkt')
text_tokens = nltk.word_tokenize(text)
filtered_txt=[word for word in text_tokens if word.lower() not in stop_words]
# Join the words back into a single string
filtered_txt = ' '.join(filtered_txt)
# Split the filtered_text into a list of words based on the specified pattern
words_list = re.split(r'[ ,.?!\n\(\)\[\]]+', filtered_txt)

# Calculate the frequency distribution
freq_dist = FreqDist(words_list)

# Print the frequency of each word
for word, frequency in freq_dist.items():
    print(f"{word}: {frequency}")