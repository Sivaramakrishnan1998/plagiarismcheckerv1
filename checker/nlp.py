from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# for stop words removal
def removestopwords(input_str):
	stop_words = nltk.corpus.stopwords.words('english')
	tokens = word_tokenize(input_str)
	result = [i for i in tokens if not i in stop_words]
	return result


def stemmedtext(input_str):
	stemmer= PorterStemmer()
	input_str=word_tokenize(input_str)
	stemmed_list = []
	for word in input_str:
	    stemmed_list(stemmer.stem(word))
	stemmedstr = ''.join(stemmed_list)
	return stemmedstr



def lemmatizertxt(input_str):
	lemmatizer=WordNetLemmatizer()
	input_str=word_tokenize(input_str)
	lemamtizer_list = []
	for word in input_str:
	    stemmed_list(lemmatizer.lemmatize(word))
	lemmatizerstr = ''.join(lemmatizer_list)
	return lemmatizerstr
	