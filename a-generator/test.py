from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

print(sent_tokenize(EXAMPLE_TEXT))

print(word_tokenize(EXAMPLE_TEXT))


print('\n')

from nltk.corpus import stopwords

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

print('\n')
#***********************************************************
from nltk.stem import PorterStemmer

ps = PorterStemmer()
new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))

# ***********************************************************
print('\n')
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer  # machine learning sentence tokenizer

train_text = state_union.raw("2005-GWBush.txt")
# print(train_text)
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# print(custom_sent_tokenizer)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
def process_content():
    try:
        for i in tokenized[1:3]:
            print(i)
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

            # get chunks as in the regular expression
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            # get chunks that are not in the regex in second line. you can specify both what you want and what you need to remove
            # chunkGram = r"""Chunk: {<.*>+}
            #                                     }<VB.?|IN|DT|TO>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)
            chunked.draw()

    except Exception as e:
            print(str(e))

# process_content()

def process_contents():
    try:
        for i in tokenized[1:3]:
            print(i)
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # specify the type of NE
            namedEnt = nltk.ne_chunk(tagged)
            # do not specify the type of NE
            # namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
    except Exception as e:
        print(str(e))


# process_contents()

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))