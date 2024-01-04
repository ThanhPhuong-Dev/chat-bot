from keras.models import load_model
import json
import regex as re
import numpy as np

# from nltk import word_tokenize
import underthesea
from underthesea import word_tokenize
import random
from keras.utils import to_categorical

# import nltk
# nltk.download('punkt')
# --------------Code các hàm tiền xử lí--------------


def loaddicchar():
    dic = {}
    char1252 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
        "|"
    )
    charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
        "|"
    )
    for i in range(len(char1252)):
        dic[char1252[i]] = charutf8[i]
    return dic


dicchar = loaddicchar()


# Đưa toàn bộ dữ liệu qua hàm này để chuẩn hóa lại
def convert_unicode(txt):
    return re.sub(
        r"à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ",
        lambda x: dicchar[x.group()],
        txt,
    )


def text_process(text):
    text = convert_unicode(text)
    text = text.lower()
    return text


def sen_to_vec(tokenized_sen, all_words):
    vec = np.zeros(len(all_words), dtype=np.float32)
    for index, w in enumerate(all_words):
        if w in tokenized_sen:
            vec[index] = 1.0
    return vec


with open("./database.json", "r", encoding="utf-8") as file:
    db = json.load(file)
with open("./intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)
with open("./state_vector.json", "r", encoding="utf-8") as file:
    states = json.load(file)

# --------------Chuẩn bị data train bag_word & bag_word_state--------------
list_key_db = list(
    db.keys()
)  # hiện tại có (học phí, giới thiệu chung, điểm chuẩn, tổ hợp xét tuyển)
list_key_intent = []
for intent in intents["intents"]:
    list_key_intent.append(intent["tag"])
all_words = []
tags = []
pat_tag = []

for intent in intents["intents"]:
    tag = intent["tag"]
    tags.append(tag)
    for pattern in intent["patterns"]:
        pattern = text_process(pattern)
        w = word_tokenize(pattern)
        all_words.extend(w)
        pat_tag.append((w, tag))

ignore_char = [
    "?",
    "!",
    ".",
    ",",
    "ad",
    "ạ",
    "ơi",
    "cho",
    "hỏi",
    "về",
    "làm",
    "thế",
    "nào",
    "có",
    "của",
    "cho",
    "ở",
    "và",
    "có",
    "không",
    "này",
    "khi",
    "để",
    "đi",
    "em",
    "mình",
    "bạn",
    "có",
    "gì",
    "nhé",
    "được",
    "ra",
    "sao",
    "mấy",
    "đó",
    "người",
    "như",
    "từ",
    "là",
    "cách",
    "nhưng",
    "theo",
    "hay",
    "với",
    "nên",
    "sẽ",
    "những",
    "làm",
    "nói",
    "được",
    "nếu",
    "đã",
]
bag_word = [word for word in all_words if word not in ignore_char]
bag_word = sorted(set(bag_word))
tags = sorted(set(tags))

all_words_state = []
state_tags = []
pat_tag_state = []
for state in states["state_vector"]:
    state_tag = state["tag"]
    state_tags.append(state_tag)
    for pattern in state["patterns"]:
        pattern = text_process(pattern)
        w = word_tokenize(pattern)
        all_words_state.extend(w)
        pat_tag_state.append((w, state_tag))


ignore_char = ["?", "!", ".", ","]
bag_word_state = [word for word in all_words_state if word not in ignore_char]
bag_word_state = sorted(set(bag_word_state))
state_tags = sorted(set(state_tags))

# --------------Load model--------------


model = load_model("./model.h5")
model_state = load_model("./model_state.h5")
bot_name = "DANANG TOURIST"


def get_pred_intent(chat, bag_word):
    chat = text_process(chat)
    w = np.array(word_tokenize(chat))
    vec = sen_to_vec(w, bag_word).reshape(1, -1)
    pred = model.predict(vec)
    prob = pred[0, pred.argmax(axis=-1)[0]]
    tag = tags[pred.argmax(axis=-1)[0]]
    return prob, tag


def get_pred_state(chat, bag_word):
    chat = text_process(chat)
    w = np.array(word_tokenize(chat))
    vec = sen_to_vec(w, bag_word).reshape(1, -1)
    pred = model_state.predict(vec)
    prob_state = pred[0, pred.argmax(axis=-1)[0]]
    state = state_tags[pred.argmax(axis=-1)[0]]
    return prob_state, state


def get_response(chat, slots, count):
    if chat.lower() == "không" or chat.lower() == "có":
        for intent in intents["intents"]:
            if intent["tag"] == "goodbye":
                return f"{random.choice(intent['responses'])}"
    prob_intent, tag = get_pred_intent(chat, bag_word)
    print(prob_intent, tag)
    prob_state, state = get_pred_state(chat, bag_word_state)
    print(prob_state, state)
    if prob_state > 0.75 and count[0] == 0:
        count[0] = 1
        slots.insert(1, state)
    elif prob_state > 0.75 and count[0] == 1:
        slots.clear()
        slots.insert(1, state)
    if (
        len(slots) == 1
        and tag != "greeting"
        and prob_intent > 0.75
        and slots[0] in list_key_intent
    ):
        slots.clear()
    if prob_intent > 0.75:  # du doan intent dung nen them vao slot
        slots.insert(0, tag)
    if (
        len(slots) == 3 and slots[0] == "greeting"
    ):  # khi chi nhap ten nganh, mac dinh intent = greeting duoc them vao bi du nen phai xoa
        slots.pop(0)
    print(slots)
    if len(slots) == 1:  # thieu state hoặc intent
        if slots[0] in state_tags:  # thieu intent
            return f"Bạn cần hỏi thông tin tour {slots[0]}?"
        elif (
            slots[0] in list_key_db
        ):  # thieu state, intent (học phí, giới thiệu chung, điểm chuẩn, tổ hợp xét tuyển)
            return "Bạn cần hỏi thông tin tour nào?"
        else:  # thiếu state, intent không phải (học phí, giới thiệu chung, điểm chuẩn, tổ hợp xét tuyển)
            for intent in intents["intents"]:
                if tag == intent["tag"]:
                    slots.pop(0)
                    return f"{random.choice(intent['responses'])}"
    else:  # len = 2
        if (
            slots[0] in list_key_db
        ):  # intent (học phí, giới thiệu chung, điểm chuẩn, tổ hợp xét tuyển)
            if slots[1] in db[slots[0]].keys():  # slot 2 la state
                for intent in intents["intents"]:
                    if slots[0] == intent["tag"]:
                        res = intent["responses"][0].format(
                            slots[1], db[slots[0]][slots[1]]
                        )
                        slots.pop(0)
                        return res
            else:  # slot 2 khong phai state
                slots.pop(0)
                return "Bạn nên cung cấp thông tin đầy đủ hơn để nhận được thông tin chính xác hơn"
        elif (
            slots[0] == "greeting" and slots[1] in state_tags
        ):  # khi chi nhap ten nganh, mac dinh intent: greeting
            str = f"Bạn cần hỏi thông tin nào của ngành {slots[1]}?"
            slots.pop(0)
            return str
        elif (
            slots[0] not in list_key_db and slots[1] in state_tags
        ):  # intent không phải (học phí, giới thiệu chung, điểm chuẩn, tổ hợp xét tuyển), slot 2 khong phai state
            for intent in intents["intents"]:
                if slots[0] == intent["tag"]:
                    slots.pop(0)
                    return f"{random.choice(intent['responses'])}"
        else:
            for intent in intents["intents"]:
                if slots[0] == intent["tag"]:
                    slots.pop(0)
                    return f"{random.choice(intent['responses'])}"
