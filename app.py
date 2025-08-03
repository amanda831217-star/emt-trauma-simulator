import streamlit as st
import pandas as pd
import random

# 載入題庫資料
@st.cache_data
def load_cases():
    return pd.read_csv("trauma_cases.csv", encoding="utf-8-sig")

# 載入資料
cases = load_cases()

# 介面標題
st.title("🚑 EMT 創傷模擬器：隨機情境題庫（含危急判斷與SBAR）")

# 顯示總題數
st.markdown(f"📦 目前題庫共：**{len(cases)} 題**")

# 按鈕操作：隨機抽一題
if st.button("🔁 抽出一題"):
    case = cases.sample(1).iloc[0]

    # 顯示題號與資訊
    st.subheader(f"{case['題號']} {'（危及生命！）' if case['是否危及生命']=='✅ 是' else '（穩定）'}")
    st.markdown(f"**創傷機轉：** {case['創傷機轉']}")
    st.markdown(f"**主訴：** {case['主訴']}")
    st.markdown(f"**意識狀態：** {case['意識狀態']}")
    st.markdown(f"**血壓：** {case['血壓']}")
    st.markdown(f"**血氧（SpO₂）：** {case['血氧']}")
    st.markdown(f"**心跳（HR）：** {case['心跳']}")
    st.markdown(f"**呼吸頻率（RR）：** {case['呼吸頻率']}")
    st.markdown(f"**膚色與狀況：** {case['膚色與狀況']}")
    st.markdown(f"**病史：** {case['病史']}")
    st.markdown(f"**危及判斷：** {case['是否危及生命']}")

    # 顯示 SBAR
    with st.expander("📋 SBAR 交接範例"):
        st.code(case["SBAR 報告"], language="markdown")