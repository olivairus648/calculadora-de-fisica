import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Calculadora de Física - Mateus",
    layout="centered",
    initial_sidebar_state="expanded",
    page_icon="🚀"
)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        * { font-family: 'Inter', sans-serif; }
        .stApp { background: linear-gradient(135deg, #2c0e4e 0%, #4b0082 100%); color: #e0d4ff; }
        .stSidebar { background: #1a0b2e !important; border-right: 1px solid #5a3f7d; }
        h1, h2, h3 { color: #d4bfff !important; text-shadow: 0 2px 4px rgba(0,0,0,0.4); }
        .stButton > button {
            background: linear-gradient(90deg, #7c3aed, #a78bfa);
            color: white; border: none; border-radius: 12px;
            padding: 0.6rem 1.2rem; font-weight: 600;
            transition: all 0.3s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #6d28d9, #8b5cf6);
            transform: translateY(-3px); box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        }
        .stNumberInput > div > div > input, .stRadio > div {
            background: #3a1a5e; color: #e0d4ff;
            border: 1px solid #6d28d9; border-radius: 10px;
        }
        .card {
            background: rgba(90, 63, 125, 0.25);
            backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(125, 95, 180, 0.3); border-radius: 16px;
            padding: 1.8rem; margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }
        .result-box {
            background: rgba(124, 58, 237, 0.18); border-left: 5px solid #7c3aed;
            padding: 1.2rem; border-radius: 10px; margin: 1rem 0; font-weight: 500;
        }
        hr { border-color: #5a3f7d; margin: 2rem 0; }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("Calculadora de Física - Mateus 🚀")
st.markdown("Escolha uma fórmula, veja a ilustração e calcule! Unidades em SI.")

def ler_float(label, key, value=0.0, step=0.1, min_value=None):
    return st.number_input(label, value=value, step=step, format="%.2f", key=key, min_value=min_value)

opcao = st.sidebar.selectbox("Escolha o cálculo", [
    "Velocidade média", "Posição em MRU (S = v · t)", "Aceleração",
    "Posição final (MRUV)", "Velocidade final (MRUV)",
    "Energia cinética", "Força (F = m·a)",
    "Queda Livre / Lançamento Vertical", "Lançamento Oblíquo (Projétil)",
    "Lei de Hooke (Mola)", "Potência Mecânica (P = τ / t ou P = F · v)"
])

st.markdown("---")

if opcao == "Velocidade média":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Velocidade Média (Vm = Δs / Δt)")
    st.image("https://s2.static.brasilescola.uol.com.br/img/2018/09/movimento-uniforme-be(6).jpeg", use_column_width=True)
    col1, col2 = st.columns(2)
    ds = col1.number_input("Δs [m]", value=0.0, step=0.1, key="vm_ds")
    dt = col2.number_input("Δt [s]", value=0.0, step=0.1, key="vm_dt")
    if st.button("Calcular", key="vm_calc"):
        if dt > 0:
            vm = ds / dt
            st.markdown(f'<div class="result-box">Vm = **{vm:.2f} m/s** ≈ **{vm*3.6:.1f} km/h**</div>', unsafe_allow_html=True)
        else:
            st.error("Tempo deve ser > 0")
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Posição em MRU (S = v · t)":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Posição em MRU")
    st.image("https://mentalmapsbrasil.com.br/wp-content/uploads/2024/11/movimento-retilineo-uniforme-MRU-mapa-mental.webp", use_column_width=True)
    col1, col2, col3 = st.columns(3)
    s0 = col1.number_input("s₀ [m]", value=0.0, key="mru_s0")
    v = col2.number_input("v [m/s]", value=0.0, key="mru_v")
    t = col3.number_input("t [s]", value=0.0, min_value=0.0, key="mru_t")
    if st.button("Calcular", key="mru_calc"):
        if t >= 0:
            s = s0 + v * t
            st.markdown(f'<div class="result-box">S = **{s:.2f} m**</div>', unsafe_allow_html=True)
        else:
            st.error("Tempo ≥ 0")
    st.markdown('</div>', unsafe_allow_html=True)

# ... (outras opções semelhantes)

elif opcao == "Força (F = m·a)":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Força (F = m · a)")
    col1, col2 = st.columns(2)
    m = col1.number_input("Massa m [kg]", value=0.0, step=0.1, key="f_m")
    a = col2.number_input("Aceleração a [m/s²]", value=0.0, step=0.1, key="f_a")
    if st.button("Calcular", key="forca_calc"):
        if m > 0:
            f = m * a
            st.markdown(f'<div class="result-box">F = **{f:.2f} N**</div>', unsafe_allow_html=True)
        else:
            st.error("Massa deve ser > 0")
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Energia cinética":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Energia Cinética (½mv²)")
    col1, col2 = st.columns(2)
    m = col1.number_input("Massa m [kg]", value=0.0, step=0.1, key="ec_m")
    v = col2.number_input("Velocidade v [m/s]", value=0.0, key="ec_v")
    if st.button("Calcular", key="ec_calc"):
        if m > 0:
            ec = 0.5 * m * v**2
            st.markdown(f'<div class="result-box">Ec = **{ec:.2f} J**</div>', unsafe_allow_html=True)
        else:
            st.error("Massa deve ser > 0")
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Queda Livre / Lançamento Vertical":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Queda Livre / Lançamento Vertical")
    v0 = st.number_input("Velocidade inicial v₀ [m/s]", value=0.0, min_value=0.0, key="queda_v0")
    if st.button("Calcular", key="queda_calc"):
        if v0 >= 0:
            g = 9.8
            h_max = v0**2 / (2*g)
            t_total = 2 * (v0 / g)
            st.markdown(f'<div class="result-box">h_max = **{h_max:.2f} m**  \nt_total = **{t_total:.2f} s**</div>', unsafe_allow_html=True)
        else:
            st.error("v₀ ≥ 0")
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Lei de Hooke (Mola)":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Lei de Hooke")
    k = st.number_input("Constante k [N/m]", value=0.0, min_value=0.0, key="hooke_k")
    x = st.number_input("Deformação x [m]", value=0.0, key="hooke_x")
    if st.button("Calcular", key="hooke_calc"):
        if k > 0:
            F = -k * x
            E = 0.5 * k * x**2
            st.markdown(f'<div class="result-box">F = **{F:.2f} N**  \nE_pot = **{E:.2f} J**</div>', unsafe_allow_html=True)
        else:
            st.error("k > 0")
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Potência Mecânica (P = τ / t ou P = F · v)":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Potência Mecânica")
    modo = st.radio("Modo", ["Trabalho / Tempo", "Força × Velocidade"])
    if modo == "Trabalho / Tempo":
        tau = st.number_input("Trabalho τ [J]", value=0.0, key="pot_tau")
        t = st.number_input("Tempo t [s]", value=0.0, min_value=0.001, key="pot_t")
        if st.button("Calcular", key="pot1"):
            if t > 0:
                p = tau / t
                st.markdown(f'<div class="result-box">P = **{p:.2f} W**</div>', unsafe_allow_html=True)
            else:
                st.error("Tempo > 0")
    else:
        f = st.number_input("Força F [N]", value=0.0, key="pot_f")
        v = st.number_input("Velocidade v [m/s]", value=0.0, key="pot_v")
        if st.button("Calcular", key="pot2"):
            p = f * v
            st.markdown(f'<div class="result-box">P = **{p:.2f} W**</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Feito por Mateus • Python + Streamlit")
