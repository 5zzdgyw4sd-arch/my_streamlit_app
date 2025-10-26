import streamlit as st
from math import sqrt
from fractions import Fraction

st.title("🧮 二次方程式の解を求めるアプリ（ルート＋分数表示）")
st.write("二次方程式 ax² + bx + c = 0 の解を求めます。実数解のみ対応。")

# --- 入力 ---
a = st.number_input("a の値を入力", value=1, step=1)
b = st.number_input("b の値を入力", value=0, step=1)
c = st.number_input("c の値を入力", value=0, step=1)

# --- 計算ボタン ---
if st.button("解を求める"):
    if a == 0:
        st.error("a = 0 の場合は二次方程式ではありません。")
    else:
        # 判別式
        D = b**2 - 4*a*c
        st.write(f"判別式 D = {D}")

        if D > 0:
            # √Dが整数なら分数に組み込める
            sqrt_D_int = int(sqrt(D)) if sqrt(D).is_integer() else f"√{D}"
            denom = 2*a
            x1 = f"({-b} + {sqrt_D_int}) / {denom}"
            x2 = f"({-b} - {sqrt_D_int}) / {denom}"
            st.success(f"2つの実数解があります：\n x₁ = {x1}\n x₂ = {x2}")
        elif D == 0:
            x = Fraction(-b, 2*a)
            st.success(f"重解です： x = {x}")
        else:
            st.warning("判別式が負のため、実数解は存在しません。")
