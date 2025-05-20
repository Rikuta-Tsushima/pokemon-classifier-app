#streamlit run main.py

import streamlit as st
import pickle

# タイトル
st.title("伝説ポケモン分類器")
st.markdown("ポケモンのステータスを入力すると、それが伝説かどうかを判定します。")

# 入力フォーム
hp = st.slider("HP", 1, 255, 80)
attack = st.slider("Attack", 1, 255, 80)
defense = st.slider("Defense", 1, 255, 80)
sp_atk = st.slider("Sp. Atk", 1, 255, 80)
sp_def = st.slider("Sp. Def", 1, 255, 80)
speed = st.slider("Speed", 1, 255, 80)

# モデルを読み込み
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# 判定
if st.button("伝説か判定！"):
    features = [[hp, attack, defense, sp_atk, sp_def, speed]]
    prediction = model.predict(features)[0]
    if prediction:
        st.success("🎉 このポケモンは伝説です！")
    else:
        st.info("これは伝説ではないようです。")
