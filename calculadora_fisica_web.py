import streamlit as st
import math
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Calculadora de Física - Mateus", layout="wide", page_icon="🚀")

# CSS Moderno (mesmo do MathCloud)
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

# ===================== FUNÇÃO PARA MOSTRAR RESOLUÇÃO DINÂMICA =====================
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
            
            # Resolução dinâmica
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
    
    if st.button("Calcular Posição"):
        s = s0 + v * t
        st.markdown(f'<div class="result-box">Posição final S = **{s:.2f} m**</div>', unsafe_allow_html=True)
        mostrar_resolucao("Cálculo de Posição em MRU", [
            "S = S₀ + v · t",
            f"S = {s0} + {v} · {t}",
            f"S = **{s:.2f} m**"
        ])

elif opcao == "Aceleração":
    st.subheader("Aceleração (a = Δv / Δt)")
    col1, col2, col3 = st.columns(3)
    with col1: v0 = ler_float("v₀ (m/s)", 0.0)
    with col2: vf = ler_float("vf (m/s)", 20.0)
    with col3: t = ler_float("Δt (s)", 4.0, min_value=0.01)
    
    if st.button("Calcular Aceleração"):
        a = (vf - v0) / t
        st.markdown(f'<div class="result-box">a = **{a:.2f} m/s²**</div>', unsafe_allow_html=True)
        mostrar_resolucao("Cálculo de Aceleração", [
            "a = (vf - v₀) / Δt",
            f"a = ({vf} - {v0}) / {t}",
            f"a = **{a:.2f} m/s²**"
        ])

elif opcao == "Posição final (MRUV)":
    st.subheader("Posição final em MRUV")
    col1, col2 = st.columns(2)
    with col1:
        s0 = ler_float("s₀ (m)", 0.0)
        v0 = ler_float("v₀ (m/s)", 10.0)
    with col2:
        a = ler_float("a (m/s²)", 2.0)
        t = ler_float("t (s)", 5.0, min_value=0.0)
    
    if st.button("Calcular Posição"):
        s = s0 + v0 * t + 0.5 * a * t**2
        st.markdown(f'<div class="result-box">s = **{s:.2f} m**</div>', unsafe_allow_html=True)
        mostrar_resolucao("Cálculo de Posição em MRUV", [
            "s = s₀ + v₀t + ½at²",
            f"s = {s0} + {v0}×{t} + 0.5×{a}×{t}²",
            f"s = **{s:.2f} m**"
        ])

elif opcao == "Velocidade final (MRUV)":
    st.subheader("Velocidade final em MRUV")
    col1, col2, col3 = st.columns(3)
    with col1: v0 = ler_float("v₀ (m/s)", 10.0)
    with col2: a = ler_float("a (m/s²)", 2.0)
    with col3: t = ler_float("t (s)", 5.0, min_value=0.0)
    
    if st.button("Calcular Velocidade Final"):
        v = v0 + a * t
        st.markdown(f'<div class="result-box">v = **{v:.2f} m/s**</div>', unsafe_allow_html=True)
        mostrar_resolucao("Cálculo de Velocidade Final", [
            "v = v₀ + a·t",
            f"v = {v0} + {a} × {t}",
            f"v = **{v:.2f} m/s**"
        ])

elif opcao == "Energia cinética":
    st.subheader("Energia Cinética")
    col1, col2 = st.columns(2)
    with col1: m = ler_float("Massa m (kg)", 2.0, min_value=0.001)
    with col2: v = ler_float("Velocidade v (m/s)", 10.0)
    
    if st.button("Calcular Ec"):
        ec = 0.5 * m * v**2
        st.markdown(f'<div class="result-box">Ec = **{ec:.2f} J**</div>', unsafe_allow_html=True)
        mostrar_resolucao("Cálculo de Energia Cinética", [
            "Ec = ½ m v²",
            f"Ec = 0.5 × {m} × {v}²",
            f"Ec = **{ec:.2f} J**"
        ])

elif opcao == "Força (F = m·a)":
    st.subheader("Força")
    col1, col2 = st.columns(2)
    with col1: m = ler_float("Massa m (kg)", 10.0, min_value=0.001)
    with col2: a = ler_float("Aceleração a (m/s²)", 5.0)
    
    if st.button("Calcular Força"):
        f = m * a
        st.markdown(f'<div class="result-box">F = **{f:.2f} N**</div>', unsafe_allow_html=True)
        mostrar_resolucao("Cálculo de Força", [
            "F = m · a",
            f"F = {m} × {a}",
            f"F = **{f:.2f} N**"
        ])

elif opcao == "Trabalho Mecânico":
    st.subheader("Trabalho Mecânico")
    col1, col2 = st.columns(2)
    with col1: f = ler_float("Força F (N)", 100.0)
    with col2: d = ler_float("Deslocamento d (m)", 10.0)
    theta = st.number_input("Ângulo θ (°)", value=0.0)
    
    if st.button("Calcular Trabalho"):
        w = f * d * math.cos(math.radians(theta))
        st.markdown(f'<div class="result-box">Trabalho W = **{w:.2f} J**</div>', unsafe_allow_html=True)
        mostrar_resolucao("Cálculo de Trabalho", [
            "W = F · d · cosθ",
            f"W = {f} × {d} × cos({theta}°)",
            f"W = **{w:.2f} J**"
        ])

elif opcao == "Impulso e Quantidade de Movimento":
    st.subheader("Impulso e Quantidade de Movimento")
    col1, col2 = st.columns(2)
    with col1: m = ler_float("Massa m (kg)", 5.0)
    with col2: delta_v = ler_float("Variação de velocidade Δv (m/s)", 10.0)
    
    if st.button("Calcular Impulso"):
        i = m * delta_v
        st.markdown(f'<div class="result-box">Impulso I = **{i:.2f} N·s**</div>', unsafe_allow_html=True)
        mostrar_resolucao("Cálculo de Impulso", [
            "I = m · Δv",
            f"I = {m} × {delta_v}",
            f"I = **{i:.2f} N·s**"
        ])

elif opcao == "Pressão":
    st.subheader("Pressão")
    col1, col2 = st.columns(2)
    with col
