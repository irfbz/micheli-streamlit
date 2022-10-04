import streamlit as st


st.title('MICHELI FUNCTIONAL SCALE')


with st.form(key= 'profile_form'):
    id = st.text_input("Your ID number", key = "id")
    name = st.text_input("Your name", key = "name")

    submit_btn = st.form_submit_button('入力')


st.write('(A) 症状')
symptom_options = ['痛みは無い','痛みがスポーツ活動に与える影響はわずかである','痛みはスポーツ活動に中程度の影響がある','痛みはスポーツ活動に深刻な影響がある','痛くてスポーツができない']
symptom = st.radio(label='1. 痛みはスポーツ活動にどの程度影響を与えますか？',
                options=(symptom_options[0],
                        symptom_options[1],
                        symptom_options[2],
                        symptom_options[3],
                        symptom_options[4]))

if symptom == symptom_options[0]:
    symptom_score = 0
elif symptom == symptom_options[1]:
    symptom_score = 1
elif symptom == symptom_options[2]:
    symptom_score = 2
elif symptom == symptom_options[3]:
    symptom_score = 3
elif symptom == symptom_options[4]:
    symptom_score = 4



st.write(' ')
st.write('(B) 日常活動動作')
ADL1_options = ['全力疾走や限界まで体幹伸展ができる','走れるが体幹伸展でいくらか痛みが出る','ランニングと体幹伸展で疼痛が出る','体幹伸展はできない','ランあるいは体幹伸展はできない']
ADL1 = st.radio(label='1. 背中を伸ばしたり（後ろに曲げる）、直立姿勢で、どの程度の痛みが伴いますか？',
                options=(ADL1_options[0],
                        ADL1_options[1],
                        ADL1_options[2],
                        ADL1_options[3],
                        ADL1_options[4]))

if ADL1 == ADL1_options[0]:
    ADL1_score = 0
elif ADL1 == ADL1_options[1]:
    ADL1_score = 1
elif ADL1 == ADL1_options[2]:
    ADL1_score = 2
elif ADL1 == ADL1_options[3]:
    ADL1_score = 3
elif ADL1 == ADL1_options[4]:
    ADL1_score = 4

ADL2_options = ['座ることと前屈を制限なく行える','座れるが前屈でいくらか痛みがある','着座と前屈で痛みがある','座れないあるいは前屈の負荷がかけられない']
ADL2 = st.radio(label='2. 座ったりかがんだりする動作にどの程度関係していますか？',
                options=(ADL2_options[0],
                        ADL2_options[1],
                        ADL2_options[2],
                        ADL2_options[3]))

if ADL2 == ADL2_options[0]:
    ADL2_score = 0
elif ADL2 == ADL2_options[1]:
    ADL2_score = 1
elif ADL2 == ADL2_options[2]:
    ADL2_score = 2
elif ADL2 == ADL2_options[3]:
    ADL2_score = 3

ADL3_options = ['痛みなくジャンプできる','ジャンプでいくらか痛みが出る','ジャンプで痛烈な痛みが出る','痛くてジャンプができない']
ADL3 = st.radio(label='3. ジャンプと痛みの関連はどの程度ですか',
                options=(ADL3_options[0],
                        ADL3_options[1],
                        ADL3_options[2],
                        ADL3_options[3]))

if ADL3 == ADL3_options[0]:
    ADL3_score = 0
elif ADL3 == ADL3_options[1]:
    ADL3_score = 1
elif ADL3 == ADL3_options[2]:
    ADL3_score = 2
elif ADL3 == ADL3_options[3]:
    ADL3_score = 3


st.write('(C) Visual Analogue Scale による痛みの評価')
VAS = st.slider('1. 線の左端が痛みなし、右端が仕事や学校に行けないほどの激しい痛みを示している場合、あなたの経験に最も一致する線の部分にX印を付けて、あなたの痛みの強さを評価してください。',  
                0, 100, 100, 1)
VAS = VAS*0.1

st.write('0 痛みなし・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・最も深刻な痛み 10')


st.write('【SCORE】A1', symptom_score, 'B1', ADL1_score, 'B2', ADL2_score, 'B3', ADL3_score, 'C1', VAS)
total_score = (symptom_score + ADL1_score + ADL2_score + ADL3_score + VAS)*4
st.write('【TOTAL_SCORE】 (A1+B1+B2+B3+C1)× 4 =', '《',str(total_score), '》')

st.button(label= '送信')

#img = Image.open('/Users/D-yamane/Desktop/スクリーンショット 2019-09-22 21.27.08.png')
#st.image(img, caption='ASC', use_column_width=True)

