# 🧠 Pokémon Classifier App

このアプリは、ポケモンのステータス（HP・攻撃・防御など）から  
そのポケモンが「伝説」かどうかを判定します。

---

## 🚀 機能一覧

- ポケモンの6つのステータスを入力  
- 機械学習（ランダムフォレスト）による分類モデルで判定  
- Streamlit製のシンプルなWebアプリ  
- GitHubでコード公開済み

---

## 📊 精度・評価
- 使用モデル：ランダムフォレスト（sklearn）
- 分類精度：約 92%
- データ：ポケモンの種族値（HP, Attack, Defense, Sp. Atk, Sp. Def, Speed）とラベル（伝説かどうか）

---

## 🖼 サンプル画面
<img width="1035" alt="screenshot" src="https://github.com/user-attachments/assets/fbcfd0c8-90ca-475f-84e6-de6d742dc600" />

---

## 📦 使い方（ローカル実行）

以下のコマンドで必要なライブラリをインストールし、アプリを起動できます。

```bash
pip install -r requirements.txt
streamlit run main.py
