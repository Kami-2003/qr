import streamlit as st

# Streamlitページの基本設定
st.set_page_config(
    page_title="テイクアウト弁当「学食＋」アンケート",
    page_icon="🍱",
    layout="centered"
)

# --- サイトの目的と導入メッセージ ---
st.title("🍱 学食＋感想アンケート")
st.markdown("""
本日は「学食＋」をご利用いただき、誠にありがとうございます！
より良いサービスと、皆様に喜んでいただけるお弁当を提供するために、ぜひご意見をお聞かせください。
約3分で完了します。ご協力をお願いいたします。
""")

st.markdown("---")

# --- アンケートフォーム ---
with st.form(key='bento_survey_form'):
    st.header("1. 今回のお弁当について")

    # 満足度
    satisfaction = st.slider(
        "今回の**お弁当の満足度**はいかがでしたか？",
        min_value=1,
        max_value=5,
        value=3,
        help="1:非常に不満, 2:不満, 3:普通, 4:満足, 5:非常に満足"
    )

    # 特に良かった点
    good_points_options = [
        "味付け", "ボリューム", "彩り", "容器",
        "受け取りやすさ", "価格", "その他"
    ]
    good_points = st.multiselect(
        "今回の**お弁当で特に良かった点**は何ですか？（複数選択可）",
        options=good_points_options
    )
    if "その他" in good_points:
        good_points_other = st.text_area("「その他」の良かった点をご記入ください", key="good_other")
    else:
        good_points_other = ""

    # 改善してほしい点
    improvement_points_options = [
        "味付け", "ボリューム", "彩り", "容器",
        "受け取りやすさ", "価格", "その他"
    ]
    improvement_points = st.multiselect(
        "今回の**お弁当で改善してほしい点**は何ですか？（複数選択可）",
        options=improvement_points_options
    )
    if "その他" in improvement_points:
        improvement_points_other = st.text_area("「その他」の改善点をご記入ください", key="improvement_other")
    else:
        improvement_points_other = ""

    st.markdown("---")

    st.header("2. ご利用頻度とメニューの希望")

    # 利用頻度
    frequency = st.radio(
        "今後、このお弁当を**どれくらいの頻度で利用したいですか？**",
        options=[
            "毎日","週に3回以上", "週に1～2回", "月に2～3回", "月に1回程度",
            "不定期に利用したい", "利用しない"
        ]
    )

    # メニューの希望
    menu_wish_options = [
        "和食（魚メイン）", "和食（肉メイン）", "洋食（ハンバーグ、チキンなど）",
        "中華", "アジアン", "野菜たっぷり", "ガッツリ系", "ヘルシー系",
        "季節限定メニュー", "その他"
    ]
    menu_wish = st.multiselect(
        "今後、どのような**メニューのお弁当が欲しいですか？**（複数選択可）",
        options=menu_wish_options
    )
    if "その他" in menu_wish:
        menu_wish_other = st.text_area("「その他」の欲しいメニューをご記入ください", key="menu_other")
    else:
        menu_wish_other = ""

    # 希望価格帯
    price_range = st.radio(
        "お弁当に希望する**価格帯はどのくらいですか？**",
        options=[
            "～600円", "601円～700円", "701円～800円", "801円～900円",
            "901円～1,000円", "1,001円～"
        ]
    )

    # 自由記述
    general_feedback = st.text_area(
        "他に、お弁当サービス全般に関するご要望やご意見があればご自由にご記入ください。"
    )

    st.markdown("---")

    st.header("3. お客様の情報（任意）")

    # 性別
    gender = st.radio(
        "性別",
        options=["男性", "女性", "その他", "回答しない"],
        horizontal=True
    )

    # 学年
    age_group = st.radio(
        "学年",
        options=["1年", "2年", "3年", "4年", "修士","教員", "回答しない"],
        horizontal=True
    )


    # --- 送信ボタン ---
    submit_button = st.form_submit_button(label='アンケートを送信する')

    if submit_button:
        # ここにアンケートデータを保存する処理を記述します。
        # 例: CSVファイルに保存、データベース（Firestoreなど）に送信、Google Sheetsに連携など
        # プロトタイプのため、ここでは送信された内容をコンソールに表示するだけです。
        st.success("貴重なご意見ありがとうございます！")
        st.balloons() # お祝いのアニメーション

        st.markdown("皆様の声をもとに、さらに魅力的なお弁当をお届けできるよう努めてまいります。")
