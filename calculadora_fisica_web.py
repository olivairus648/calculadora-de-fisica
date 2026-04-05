import streamlit as st
import math
import numpy as np
import plotly.graph_objects as go

# ===================== CONFIGURAÇÃO =====================
st.set_page_config(
    page_title="Calculadora de Física - Mateus",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🚀"
)

# ===================== CSS MODERNO (igual ao MathCloud) =====================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1F002E, #4A0B6B);
    }
    .stApp, p, span, div, label {
        color: #F0E6FF !important;
    }
    h1, h2, h3 {
        color: #E0B0FF !important;
    }
    div[data-testid="stVerticalBlock"] > div > div {
        background: rgba(30, 10, 50, 0.92) !important;
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(200, 150, 255, 0.25);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
    }
    .stButton > button {
        background: linear-gradient(90deg, #C71585, #E1306C);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.7rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }
    .stSidebar {
        background: #1F002E !important;
    }
    .result-box {
        background: rgba(199, 21, 133, 0.2);
        border-left: 5px solid #C71585;
        padding: 1.2rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-weight: 500;
    }
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ===================== MENU LATERAL =====================
st.sidebar.title("🚀 Física - Mateus")
opcao = st.sidebar.radio(
    "Escolha o cálculo:",
    [
        "Velocidade média",
        "Posição em MRU (S = v · t)",
        "Aceleração",
        "Posição final (MRUV)",
        "Velocidade final (MRUV)",
        "Energia cinética",
        "Força (F = m·a)",
        "Queda Livre / Lançamento Vertical",
        "Lançamento Oblíquo (Projétil)",
        "Lei de Hooke (Mola)",
        "Potência Mecânica"
    ]
)

st.title("Calculadora de Física - Mateus 🚀")
st.markdown("Escolha uma fórmula no menu lateral e calcule!")

def ler_float(label, value=0.0, step=0.1, min_value=None):
    return st.number_input(label, value=value, step=step, format="%.2f", min_value=min_value)

# ===================== CÁLCULOS =====================
with st.container():
    if opcao == "Velocidade média":
        st.subheader("Velocidade Média (Vm = Δs / Δt)")
        col1, col2 = st.columns(2)
        with col1: ds = ler_float("Deslocamento (Δs) [m]", value=100.0)
        with col2: dt = ler_float("Tempo (Δt) [s]", value=10.0, min_value=0.01)
        if st.button("Calcular Velocidade Média"):
            if dt > 0:
                vm = ds / dt
                st.markdown(f'<div class="result-box">Velocidade média = **{vm:.2f} m/s** ≈ **{vm*3.6:.1f} km/h**</div>', unsafe_allow_html=True)
            else:
                st.error("Tempo deve ser maior que zero!")

    elif opcao == "Posição em MRU (S = v · t)":
        st.subheader("Posição em MRU (S = v · t)")
        col1, col2, col3 = st.columns(3)
        with col1: s0 = ler_float("Posição inicial (S₀) [m]", value=0.0)
        with col2: v = ler_float("Velocidade (v) [m/s]", value=20.0)
        with col3: t = ler_float("Tempo (t) [s]", value=5.0, min_value=0.0)
        if st.button("Calcular Posição"):
            s = s0 + v * t
            st.markdown(f'<div class="result-box">Posição final S = **{s:.2f} m**</div>', unsafe_allow_html=True)

    elif opcao == "Aceleração":
        st.subheader("Aceleração (a = Δv / Δt)")
        col1, col2, col3 = st.columns(3)
        with col1: v0 = ler_float("Velocidade inicial v₀ [m/s]", value=0.0)
        with col2: vf = ler_float("Velocidade final vf [m/s]", value=20.0)
        with col3: t = ler_float("Tempo Δt [s]", value=4.0, min_value=0.01)
        if st.button("Calcular Aceleração"):
            a = (vf - v0) / t
            st.markdown(f'<div class="result-box">Aceleração a = **{a:.2f} m/s²**</div>', unsafe_allow_html=True)

    elif opcao == "Posição final (MRUV)":
        st.subheader("Posição final (s = s₀ + v₀ t + ½ a t²)")
        col1, col2 = st.columns(2)
        with col1:
            s0 = ler_float("s₀ [m]", value=0.0)
            v0 = ler_float("v₀ [m/s]", value=10.0)
        with col2:
            a = ler_float("a [m/s²]", value=2.0)
            t = ler_float("t [s]", value=5.0, min_value=0.0)
        if st.button("Calcular Posição"):
            s = s0 + v0 * t + 0.5 * a * t**2
            st.markdown(f'<div class="result-box">Posição final s = **{s:.2f} m**</div>', unsafe_allow_html=True)

    elif opcao == "Velocidade final (MRUV)":
        st.subheader("Velocidade final (v = v₀ + a t)")
        col1, col2, col3 = st.columns(3)
        with col1: v0 = ler_float("v₀ [m/s]", value=10.0)
        with col2: a = ler_float("a [m/s²]", value=2.0)
        with col3: t = ler_float("t [s]", value=5.0, min_value=0.0)
        if st.button("Calcular Velocidade Final"):
            v = v0 + a * t
            st.markdown(f'<div class="result-box">Velocidade final v = **{v:.2f} m/s**</div>', unsafe_allow_html=True)

    elif opcao == "Energia cinética":
        st.subheader("Energia Cinética (Ec = ½ m v²)")
        col1, col2 = st.columns(2)
        with col1: m = ler_float("Massa (m) [kg]", value=2.0, min_value=0.001)
        with col2: v = ler_float("Velocidade (v) [m/s]", value=10.0)
        if st.button("Calcular Ec"):
            ec = 0.5 * m * v**2
            st.markdown(f'<div class="result-box">Energia Cinética Ec = **{ec:.2f} J**</div>', unsafe_allow_html=True)

    elif opcao == "Força (F = m·a)":
        st.subheader("Força (F = m · a)")
        col1, col2 = st.columns(2)
        with col1: m = ler_float("Massa (m) [kg]", value=10.0, min_value=0.001)
        with col2: a = ler_float("Aceleração (a) [m/s²]", value=5.0)
        if st.button("Calcular Força"):
            f = m * a
            st.markdown(f'<div class="result-box">Força F = **{f:.2f} N**</div>', unsafe_allow_html=True)

    elif opcao == "Queda Livre / Lançamento Vertical":
        st.subheader("Queda Livre / Lançamento Vertical")
        v0 = ler_float("Velocidade inicial (v₀) [m/s]", value=0.0, min_value=0.0)
        if st.button("Calcular"):
            g = 9.8
            h_max = v0**2 / (2 * g)
            t_total = 2 * v0 / g if v0 > 0 else 0
            st.markdown(f'<div class="result-box">Altura máxima: **{h_max:.2f} m**<br>Tempo total: **{t_total:.2f} s**</div>', unsafe_allow_html=True)

    elif opcao == "Lei de Hooke (Mola)":
        st.subheader("Lei de Hooke – Força em Mola")
        k = ler_float("Constante k [N/m]", value=200.0, min_value=0.001)
        x = ler_float("Deformação x [m]", value=0.05)
        if st.button("Calcular"):
            forca = -k * x
            energia = 0.5 * k * x**2
            st.markdown(f'<div class="result-box">Força = **{forca:.2f} N**<br>Energia elástica = **{energia:.2f} J**</div>', unsafe_allow_html=True)

    elif opcao == "Potência Mecânica":
        st.subheader("Potência Mecânica")
        modo = st.radio("Modo de cálculo:", ["Trabalho e Tempo", "Força e Velocidade"])
        if modo == "Trabalho e Tempo":
            trabalho = ler_float("Trabalho τ [J]", value=1000.0)
            tempo = ler_float("Tempo t [s]", value=10.0, min_value=0.001)
            if st.button("Calcular Potência"):
                p = trabalho / tempo
                st.markdown(f'<div class="result-box">Potência P = **{p:.2f} W**</div>', unsafe_allow_html=True)
        else:
            forca = ler_float("Força F [N]", value=500.0)
            vel = ler_float("Velocidade v [m/s]", value=10.0)
            if st.button("Calcular Potência"):
                p = forca * vel
                st.markdown(f'<div class="result-box">Potência P = **{p:.2f} W**</div>', unsafe_allow_html=True)

    elif opcao == "Lançamento Oblíquo (Projétil)":
        st.subheader("Lançamento Oblíquo – Projétil")
        col1, col2 = st.columns(2)
        with col1: v0 = ler_float("Velocidade inicial v₀ [m/s]", value=50.0, min_value=0.0)
        with col2: theta = ler_float("Ângulo θ [°]", value=45.0)
        if st.button("Calcular Projétil"):
            if v0 > 0 and 0 < theta <= 90:
                theta_rad = math.radians(theta)
                vx = v0 * math.cos(theta_rad)
                vy = v0 * math.sin(theta_rad)
                g = 9.8
                t_voo = 2 * vy / g
                alcance = vx * t_voo
                h_max = vy**2 / (2 * g)

                st.markdown(f'<div class="result-box">Alcance: **{alcance:.2f} m**<br>Altura máxima: **{h_max:.2f} m**<br>Tempo de voo: **{t_voo:.2f} s**</div>', unsafe_allow_html=True)

                # Gráfico interativo com Plotly
                t = np.linspace(0, t_voo, 200)
                x = vx * t
                y = vy * t - 0.5 * g * t**2
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#FF69B4', width=4), name='Trajetória'))
                fig.update_layout(title="Trajetória do Projétil", xaxis_title="Alcance (m)", yaxis_title="Altura (m)", template="plotly_dark", height=500)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("v₀ > 0 e 0° < θ ≤ 90°")

st.caption("Feito por Mateus | Versão atualizada | 2026")
