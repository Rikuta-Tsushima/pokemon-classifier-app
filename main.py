#streamlit run main.py

import streamlit as st
import pickle
import pandas as pd
import numpy as np

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

# モデル読み込み
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# データ読み込み & 日本語名マッピング
@st.cache_data
def load_data():
    df = pd.read_csv("pokemon.csv")
    jp_df = pd.read_csv("pokedex_(Update_05.20).csv")

    # 英語名 → 日本語名（読み付き）の辞書を作成
    name_ja_dict = dict(zip(jp_df["name"], jp_df["japanese_name"]))

    # 対応があるものだけ日本語名に変換、なければ英語名のまま
    df["Name_JA"] = df["Name"].map(name_ja_dict).fillna(df["Name"])
    return df

df = load_data()

# 類似ポケモンを探す関数
def find_closest_pokemon(user_input):
    features = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
    pokemon_stats = df[features].values
    user_array = np.array(user_input)

    distances = np.linalg.norm(pokemon_stats - user_array, axis=1)
    closest_index = np.argmin(distances)
    closest_row = df.iloc[closest_index]
    return closest_row["Name_JA"], closest_row["Legendary"]

# 判定ボタン
if st.button("伝説か判定！"):
    features = [[hp, attack, defense, sp_atk, sp_def, speed]]
    prediction = model.predict(features)[0]

    # 判定結果
    if prediction:
        st.success("🎉 このポケモンは伝説です！")
    else:
        st.info("これは伝説ではないようです。")

    # 類似ポケモン表示（日本語）
    closest_name, is_legendary = find_closest_pokemon(features[0])
    st.write(f"🧭 入力に近いポケモンは **{closest_name}** です。")
