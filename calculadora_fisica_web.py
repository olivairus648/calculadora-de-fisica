import streamlit as st
import math
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Calculadora de Física - Mateus", layout="wide", page_icon="🚀")

# ===================== CSS MODERNO =====================
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #1F002E, #4A0B6B); }
    .stApp, p, span, div, label { color: #F0E6FF !important; }
    h1, h2, h3 { color: #E0B0FF !important; }
    div[data-testid="stVerticalBlock"] > div > div {
        background: rgba(30, 10, 50, 0.92) !important;
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(200, 150, 255, 0.25);
    }
    .stButton > button {
        background: linear-gradient(90deg, #C71585, #E1306C);
        color: white;
        border-radius: 12px;
        font-weight: 600;
    }
    .result-box {
        background: rgba(199, 21, 133, 0.25);
        border-left: 5px solid #C71585;
        padding: 1.2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .resolution {
        background: rgba(30, 10, 50, 0.8);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #8B5CF6;
    }
    .stSidebar { background: #1F002E !important; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🚀 Física - Mateus")
opcao = st.sidebar.radio(
    "Escolha o cálculo:",
    [
        "Velocidade média",
        "Posição em MRU",
        "Aceleração",
        "Posição final (MRUV)",
        "Velocidade final (MRUV)",
        "Energia cinética",
        "Força (F = m·a)",
        "Trabalho Mecânico",
        "Impulso e Quantidade de Movimento",
        "Pressão",
        "Calor Sensível",
        "Queda Livre / Lançamento Vertical",
        "Lançamento Oblíquo (Projétil)",
        "Lei de Hooke (Mola)",
        "Potência Mecânica"
    ]
)

st.title("Calculadora de Física - Mateus 🚀")

def ler_float(label, value=0.0, step=0.1, min_value=None):
    return st.number_input(label, value=value, step=step, format="%.2f", min_value=min_value)

def mostrar_resolucao(titulo, passos):
    st.subheader("📖 Resolução Passo a Passo")
    st.markdown('<div class="resolution">', unsafe_allow_html=True)
    st.write(f"**{titulo}**")
    for passo in passos:
        st.write(passo)
    st.markdown('</div>', unsafe_allow_html=True)

# ===================== CÁLCULOS =====================
if opcao == "Velocidade média":
    st.subheader("Velocidade Média (Vm = Δs / Δt)")
    col1, col2 = st.columns(2)
    with col1: ds = ler_float("Deslocamento Δs (m)", 100.0)
    with col2: dt = ler_float("Tempo Δt (s)", 10.0, min_value=0.01)
    
    if st.button("Calcular Velocidade Média"):
        if dt > 0:
            vm = ds / dt
            st.markdown(f'<div class="result-box">Velocidade média = **{vm:.2f} m/s**</div>', unsafe_allow_html=True)
            mostrar_resolucao("Cálculo de Velocidade Média", [
                f"Vm = Δs / Δt",
                f"Vm = {ds} / {dt}",
                f"Vm = **{vm:.2f} m/s**"
            ])
        else:
            st.error("Tempo deve ser maior que zero!")

elif opcao == "Posição em MRU":
    st.subheader("Posição em MRU (S = S₀ + v · t)")
    col1, col2, col3 = st.columns(3)
    with col1: s0 = ler_float("Posição inicial S₀ (m)", 0.0)
    with col2: v = ler_float("Velocidade v (m/s)", 20.0)
    with col3: t = ler_float("Tempo t (s)", 5.0, min_value=0.0)
