import time
import datetime
import streamlit as st

file = 'message.txt'

t = time.localtime()
y = t.tm_year
mon = t.tm_mon
d = t.tm_mday
h = t.tm_hour + 9
if h >= 24:
    h -= 24
min = t.tm_min
s = t.tm_sec

tt = time.time()
ml = int(1000*(tt - int(tt)))
ml = ("0"*(3-len(str(ml)))) + str(ml)
mil = int(1000*(int(tt+1) - tt))
mil = ("0"*(3-len(str(mil)))) + str(mil)

datetime.datetime.now()
start_time = datetime.datetime.now()
end_time = datetime.datetime(2022, 12, 31, 15)
how_long = end_time - start_time
days = how_long.days
hours = how_long.seconds // 3600
minutes = how_long.seconds // 60 - hours * 60
seconds = how_long.seconds - hours * 3600 - minutes * 60


if days < 0:
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    mil = 0
    st.balloons()

st.title("새해까지 남은시간 : {}일 {}시간 {}분 {}초 {}밀리초".format(days, hours, minutes, seconds, mil))
st.header("현재시각 : {}년 {}월 {}일 {}시 {}분 {}초 {}밀리초".format(y, mon, d, h, min, s, ml))


my_bar = st.progress(0)

if days >= 0:

    st.text(str(round((min*60 + s) /36, 2)) + "%")
    my_bar.progress(float((min*60 + s) /3600))

else:
    my_bar.progress(100)

with st.sidebar:
    st.header("채팅")

    inflobj = open(file, 'r', encoding='utf-8')
    output = inflobj.read()
    inflobj.close()
    chat = st.code(output)

    box = st.text_input(label="닉네임을 입력해주세요")
    message = st.text_area(label="내용")

    if st.button("보내기") and message.replace(" ", "") != "":
        t = time.localtime()
        y = t.tm_year
        mon = t.tm_mon
        d = t.tm_mday
        h = t.tm_hour + 9
        min = t.tm_min
        s = t.tm_sec


        datetime.datetime.now()
        start_time = datetime.datetime.now()
        end_time = datetime.datetime(2023, 1, 1)
        how_long = end_time - start_time
        days = how_long.days
        hours = how_long.seconds // 3600
        minutes = how_long.seconds // 60 - hours * 60
        seconds = how_long.seconds - hours * 3600 - minutes * 60

        if days < 0:
            days = 0
            hours = 0
            minutes = 0
            seconds = 0
            mil = 0

        if box.replace(" ", "") == "":
            nick = "(익명)"
        else:
            nick = box



        wri = ("{} : {} -({}시 {}분 {}, 새해까지 {}시 {}분 {}초)").format(box, message, h, min, s, hours, minutes, seconds)

        inflobj = open(file, 'a', encoding='utf-8')


        inflobj.write(wri + '\n')
        inflobj.close()

        inflobj = open(file, 'r', encoding='utf-8')
        output = inflobj.read()
        inflobj.close()

        chat.text(output)
        chat.code(output)
        #st.info(output, icon="ℹ️")
        #a = st.caption("-------------------------\n총" + str(output.count("\n")) + "명이 설문조사에 참여했습니다")
        #chart(output)
        #chartb(output)

        st.snow()

time.sleep(0.5)
st.experimental_rerun()
