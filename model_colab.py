import json
#import nltk
import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
from keras.utils import to_categorical
#from nltk.tokenize import word_tokenize
import underthesea
from underthesea import word_tokenize
import regex as re
import random
# --------------Code các hàm tiền xử lí--------------
with open('./intents.json','r', encoding='utf-8') as file:
    intents = json.load(file)
with open('./state_vector.json','r', encoding='utf-8') as file:
    states = json.load(file)
    


def loaddicchar():
    dic = {}
    char1252 = 'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ'.split(
        '|')
    charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
        '|')
    for i in range(len(char1252)):
        dic[char1252[i]] = charutf8[i]
    return dic


dicchar = loaddicchar()

# Đưa toàn bộ dữ liệu qua hàm này để chuẩn hóa lại
def convert_unicode(txt):
    return re.sub(
        r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',
        lambda x: dicchar[x.group()], txt)
def text_process(text):
    text = convert_unicode(text)
    text = text.lower()
    return text
def sen_to_vec(tokenized_sen,all_words):
    vec = np.zeros(len(all_words),dtype=np.float32)
    for index,w in enumerate(all_words):
        if w in tokenized_sen:
            vec[index] = 1.0
    return vec

# --------------Chuẩn bị data train bag_word & bag_word_state--------------
all_words = []
tags = []
pat_tag = []
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        pattern = text_process(pattern)
        w = word_tokenize(pattern)
        all_words.extend(w)
        pat_tag.append((w,tag))
        
ignore_char = ['?','!','.',',',"ad", "ạ", "ơi", "cho", "hỏi", "về", "làm", "thế", "nào", "có",
    "của", "cho", "ở", "và", "có", "không", "này", "khi", "để", "đi",
    "em", "mình", "bạn", "có", "gì", "nhé", "được", "ra", "sao", "mấy",
    "đó", "người", "như", "từ", "là", "cách", "nhưng", "theo", "hay",
    "với", "nên", "sẽ", "những", "làm", "nói", "được", "nếu", "đã"]

bag_word = [word for word in all_words if word not in ignore_char]
bag_word = sorted(set(bag_word))
tags = sorted(set(tags))

all_words_state = []
state_tags = []
pat_tag_state = []
for state in states['state_vector']:
    state_tag = state['tag']
    state_tags.append(state_tag)
    for pattern in state['patterns']:
        pattern = text_process(pattern)
        w = word_tokenize(pattern)
        all_words_state.extend(w)
        pat_tag_state.append((w,state_tag))

ignore_char = ['?','!','.',',']
bag_word_state = [word for word in all_words_state if word not in ignore_char]
bag_word_state = sorted(set(bag_word_state))
state_tags = sorted(set(state_tags))

# --------------Chuẩn bị data train và train--------------

X_train = []
y_train = []

for (pattern_sen,tag) in pat_tag:
    vec = sen_to_vec(pattern_sen,bag_word)
    X_train.append(vec)
    label = tags.index(tag)
    y_train.append([label])

X_train = np.array(X_train)
y_train = np.array(y_train)
y_train = to_categorical(y_train, len(tags))

model = Sequential()
model.add(Dense(len(bag_word), input_shape=(len(X_train[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(tags), activation='softmax'))
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.fit(X_train, y_train, epochs=200, batch_size=5, verbose=1)






X_train_state = []
y_train_state = []
for (pattern_sen,tag) in pat_tag_state:
    vec = sen_to_vec(pattern_sen,bag_word_state)
    X_train_state.append(vec)
    label = state_tags.index(tag)
    y_train_state.append([label])
X_train_state = np.array(X_train_state)
y_train_state = np.array(y_train_state)
y_train_state = to_categorical(y_train_state, len(state_tags))


model_state= Sequential()
model_state.add(Dense(len(bag_word_state), input_shape=(len(X_train_state[0]),), activation='relu'))
model_state.add(Dropout(0.25))
model_state.add(Dense(64, activation='relu'))
model_state.add(Dropout(0.25))
model_state.add(Dense(len(state_tags), activation='softmax'))

sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

model_state.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model_state.fit(X_train_state, y_train_state, epochs=200, batch_size=5, verbose=1)

model.save('model.h5')
model_state.save('model_state.h5')



