import streamlit as st
import math
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Calculadora de Física - Mateus",
    layout="wide",
    page_icon="🚀"
)

# CSS mais leve e estável
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #2C0E4E, #4B0082); }
    .stApp, p, span, label, div { color: #F0E6FF !important; }
    h1, h2, h3 { color: #D4BFFF !important; }
    .card, div[data-testid="stVerticalBlock"] > div > div {
        background: rgba(90, 63, 125, 0.35) !important;
        border-radius: 16px;
        padding: 20px;
        margin: 15px 0;
        border: 1px solid rgba(180, 140, 255, 0.3);
    }
    .stButton > button {
        background: linear-gradient(90deg, #C71585, #E1306C);
        color: white;
        border-radius: 12px;
        font-weight: 600;
    }
    .result-box {
        background: rgba(199, 21, 133, 0.25);
        border-left: 6px solid #C71585;
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }
    .resolution {
        background: rgba(40, 20, 70, 0.9);
        border-radius: 12px;
        padding: 18px;
        border: 1px solid #A78BFA;
        margin-top: 20px;
    }
    /* Força rolagem no sidebar */
    section[data-testid="stSidebar"] > div {
        height: 100vh !important;
        overflow-y: auto !important;
    }
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
    ],
    label_visibility="visible"
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

# ===================== Seus cálculos (mantidos) =====================
# ... (coloque aqui o resto do código com todos os if/elif que eu te passei na mensagem anterior)

# Exemplo de um cálculo (Velocidade média) para teste rápido:
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

# Adicione os outros elif aqui (Posição em MRU, Aceleração, etc.) exatamente como na versão anterior.

st.caption("✅ Versão com sidebar corrigida")
