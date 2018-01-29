from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import colorama
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

text = open('./input/text/input-text', 'rt')
data = text.read()
# print(data)
sentenses = sent_tokenize(data)

print(sent_tokenize(data))

lemmatizer = WordNetLemmatizer()

def filter_sentence(question):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(question)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(lemmatizer.lemmatize(w))
    # print(word_tokens)
    print ('filtered sentence')
    print(filtered_sentence)
    return filtered_sentence


def process_questions(question):
    filtered_q  = filter_sentence(question)
    for sentense in sentenses:
        words_found = 0
        for word in filtered_q:
            if word in sentense.lower():
                words_found +=1
        if words_found == len(filtered_q):
            return sentense

def question_is_invalid (question):
    words = word_tokenize(question)
    tagged = nltk.pos_tag(words)
    if len(tagged)<2:
        return True
    for item in tagged :
        word = item[0]
        print(word)
        tag = item[1]
        first_letter = tag[0]
        print(tag)
        if (first_letter == 'W') or (tag == 'VBZ'):
            return False
    return True

def get_score(user_answer, machine_answer):
    filtered_machine_answer = filter_sentence(machine_answer)
    filtered_user_answer = filter_sentence(user_answer)

    remained_machine_answer = []
    remained_user_answer = []

    similar_words = 0
    for word_u in filtered_user_answer:
        for word_m in filtered_machine_answer:
            if word_u != word_m:

                w1 = wordnet.synsets(word_m)
                if len(w1) > 0 :
                    w1 = w1[0]
                    # print(w1)
                    remained_machine_answer.append(w1)
                w2 = wordnet.synsets(word_u)
                if len(w2) > 0:
                    w2 = w2[0]
                    # .lemmas()[0].name()
                    # print(w2)
                    remained_user_answer.append(w2)
            else:
                similar_words += 1

    similarity = 0

    for word_u in remained_user_answer:
        for word_m in remained_machine_answer:
            similarity = word_m.wup_similarity(word_u)

    return similar_words/len(filtered_machine_answer) + similarity/(len(remained_machine_answer)+len(remained_user_answer))


while True:
    question = input(colorama.Fore.WHITE + "\n Question > ")
    if question is '':
        print(colorama.Fore.RED + "! Question can't be empty")
    elif question_is_invalid(question):
        print(colorama.Fore.MAGENTA + "! Question is not clear")
    else:
        user_answer = input(colorama.Fore.WHITE + "\n User Answer > ")
        if user_answer is '':
            print(colorama.Fore.RED + "! Answer can't be empty")
        else:
            machine_answer = process_questions(question)
            if machine_answer is None:
                print(colorama.Fore.YELLOW + "Machine Answer > ! Could not find an answer")
            else:
                print(get_score(user_answer, machine_answer))
                print(colorama.Fore.BLUE + "\n Machine Answer > "+ machine_answer)


