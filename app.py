import streamlit as st
import pandas as pd

def main():
    tab = st.sidebar.radio("選擇頁籤：", ["租金公共帳戶", "水錶度數記錄"])
# 根據選項顯示不同內容
    if tab == "租金公共帳戶":
        # st.header("章士祺租金公共帳戶")
        df = pd.read_csv("data/租金公共帳戶113年.csv")
        st.markdown('### 租金公共帳戶')
        df = df.iloc[::-1]
        df = df.fillna("")
        st.markdown('#### 113年')
        st.dataframe(df, use_container_width=True)
        # st.dataframe(df)
        # st.table(df)
        df = pd.read_csv("data/租金公共帳戶112年.csv")
        df = df.iloc[::-1]
        df = df.fillna("")
        st.markdown('#### 112年')
        st.dataframe(df, use_container_width=True)
        # st.dataframe(df)
        # st.table(df)
    elif tab == "水錶度數記錄":
        df = pd.read_csv("data/水錶度數記錄113年.csv")
        st.markdown('### 水錶度數記錄')
        df = df.round(1)
        print(df)
        df = df.iloc[::-1]
        df = df.fillna("")
        st.markdown('#### 113年')
        st.dataframe(df, use_container_width=True)
        # st.dataframe(df)
        # st.table(df)
    # elif tab == "Tab 3":
    #     st.header("這是 Tab 3 的內容")
    #     st.write("內容 C")
    pass

if __name__ == '__main__':
    main()