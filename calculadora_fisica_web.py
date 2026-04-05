import streamlit as st
import math
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Calculadora de Física - Mateus",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🚀"
)

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
    .stButton > button:hover { transform: translateY(-3px); }
    .result-box {
        background: rgba(199, 21, 133, 0.2);
        border-left: 5px solid #C71585;
        padding: 1.2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .stSidebar { background: #1F002E !important; }
</style>
""", unsafe_allow_html=True)

# ===================== MENU LATERAL =====================
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

# ===================== CÁLCULOS COM ABAS =====================
if opcao == "Velocidade média":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Velocidade Média")
        col1, col2 = st.columns(2)
        with col1: ds = ler_float("Deslocamento Δs (m)", 100.0)
        with col2: dt = ler_float("Tempo Δt (s)", 10.0, min_value=0.01)
        if st.button("Calcular"):
            vm = ds / dt
            st.markdown(f'<div class="result-box">Vm = **{vm:.2f} m/s** ≈ **{vm*3.6:.1f} km/h**</div>', unsafe_allow_html=True)
    with tab2:
        st.subheader("Resolução Passo a Passo")
        st.latex(r"V_m = \frac{\Delta s}{\Delta t}")
        st.write("1. Identifique o deslocamento total (Δs)")
        st.write("2. Identifique o tempo gasto (Δt)")
        st.write("3. Divida o deslocamento pelo tempo")

elif opcao == "Posição em MRU":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Posição em MRU")
        col1, col2, col3 = st.columns(3)
        with col1: s0 = ler_float("Posição inicial S₀ (m)", 0.0)
        with col2: v = ler_float("Velocidade v (m/s)", 20.0)
        with col3: t = ler_float("Tempo t (s)", 5.0, min_value=0.0)
        if st.button("Calcular Posição"):
            s = s0 + v * t
            st.markdown(f'<div class="result-box">S = **{s:.2f} m**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"S = S_0 + v \cdot t")
        st.write("• MRU: Movimento Retilíneo Uniforme")
        st.write("• Velocidade constante")

elif opcao == "Aceleração":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Aceleração")
        col1, col2, col3 = st.columns(3)
        with col1: v0 = ler_float("v₀ (m/s)", 0.0)
        with col2: vf = ler_float("vf (m/s)", 20.0)
        with col3: t = ler_float("Δt (s)", 4.0, min_value=0.01)
        if st.button("Calcular"):
            a = (vf - v0) / t
            st.markdown(f'<div class="result-box">a = **{a:.2f} m/s²**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"a = \frac{\Delta v}{\Delta t} = \frac{v_f - v_0}{t}")

elif opcao == "Posição final (MRUV)":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Posição final em MRUV")
        col1, col2 = st.columns(2)
        with col1:
            s0 = ler_float("s₀ (m)", 0.0)
            v0 = ler_float("v₀ (m/s)", 10.0)
        with col2:
            a = ler_float("a (m/s²)", 2.0)
            t = ler_float("t (s)", 5.0, min_value=0.0)
        if st.button("Calcular"):
            s = s0 + v0 * t + 0.5 * a * t**2
            st.markdown(f'<div class="result-box">s = **{s:.2f} m**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"s = s_0 + v_0 t + \frac{1}{2} a t^2")

elif opcao == "Velocidade final (MRUV)":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Velocidade final em MRUV")
        col1, col2, col3 = st.columns(3)
        with col1: v0 = ler_float("v₀ (m/s)", 10.0)
        with col2: a = ler_float("a (m/s²)", 2.0)
        with col3: t = ler_float("t (s)", 5.0, min_value=0.0)
        if st.button("Calcular"):
            v = v0 + a * t
            st.markdown(f'<div class="result-box">v = **{v:.2f} m/s**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"v = v_0 + a \cdot t")

elif opcao == "Energia cinética":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Energia Cinética")
        col1, col2 = st.columns(2)
        with col1: m = ler_float("Massa m (kg)", 2.0, min_value=0.001)
        with col2: v = ler_float("Velocidade v (m/s)", 10.0)
        if st.button("Calcular"):
            ec = 0.5 * m * v**2
            st.markdown(f'<div class="result-box">Ec = **{ec:.2f} J**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"E_c = \frac{1}{2} m v^2")

elif opcao == "Força (F = m·a)":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Força")
        col1, col2 = st.columns(2)
        with col1: m = ler_float("Massa m (kg)", 10.0, min_value=0.001)
        with col2: a = ler_float("Aceleração a (m/s²)", 5.0)
        if st.button("Calcular"):
            f = m * a
            st.markdown(f'<div class="result-box">F = **{f:.2f} N**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"F = m \cdot a")

elif opcao == "Trabalho Mecânico":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Trabalho Mecânico")
        col1, col2 = st.columns(2)
        with col1: f = ler_float("Força F (N)", 100.0)
        with col2: d = ler_float("Deslocamento d (m)", 10.0)
        theta = st.number_input("Ângulo θ entre F e d (°)", value=0.0)
        if st.button("Calcular Trabalho"):
            w = f * d * math.cos(math.radians(theta))
            st.markdown(f'<div class="result-box">Trabalho W = **{w:.2f} J**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"W = F \cdot d \cdot \cos\theta")

elif opcao == "Impulso e Quantidade de Movimento":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Impulso e Quantidade de Movimento")
        col1, col2 = st.columns(2)
        with col1: m = ler_float("Massa m (kg)", 5.0)
        with col2: delta_v = ler_float("Variação de velocidade Δv (m/s)", 10.0)
        if st.button("Calcular"):
            impulso = m * delta_v
            st.markdown(f'<div class="result-box">Impulso I = **{impulso:.2f} N·s**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"I = \Delta p = m \cdot \Delta v")

elif opcao == "Pressão":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Pressão")
        col1, col2 = st.columns(2)
        with col1: f = ler_float("Força F (N)", 500.0)
        with col2: a = ler_float("Área A (m²)", 0.1, min_value=0.001)
        if st.button("Calcular"):
            p = f / a
            st.markdown(f'<div class="result-box">Pressão P = **{p:.2f} Pa**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"P = \frac{F}{A}")

elif opcao == "Calor Sensível":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Calor Sensível")
        col1, col2 = st.columns(2)
        with col1: m = ler_float("Massa m (kg)", 1.0)
        with col2: c = st.number_input("Calor específico c (J/kg·°C)", value=4186.0)  # água
        delta_t = ler_float("Variação de temperatura ΔT (°C)", 10.0)
        if st.button("Calcular Calor"):
            q = m * c * delta_t
            st.markdown(f'<div class="result-box">Q = **{q:.2f} J**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"Q = m \cdot c \cdot \Delta T")

elif opcao == "Queda Livre / Lançamento Vertical":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Queda Livre / Lançamento Vertical")
        v0 = ler_float("Velocidade inicial v₀ (m/s)", 0.0)
        if st.button("Calcular"):
            g = 9.8
            h_max = v0**2 / (2 * g)
            t_total = 2 * v0 / g if v0 > 0 else 0
            st.markdown(f'<div class="result-box">Altura máxima: **{h_max:.2f} m**<br>Tempo total: **{t_total:.2f} s**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"h_{max} = \frac{v_0^2}{2g}")
        st.latex(r"t_{total} = \frac{2v_0}{g}")

elif opcao == "Lançamento Oblíquo (Projétil)":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução + Gráfico"])
    with tab1:
        st.subheader("Lançamento Oblíquo")
        col1, col2 = st.columns(2)
        with col1: v0 = ler_float("v₀ (m/s)", 50.0)
        with col2: theta = st.number_input("Ângulo θ (°)", value=45.0)
        if st.button("Calcular"):
            theta_rad = math.radians(theta)
            vx = v0 * math.cos(theta_rad)
            vy = v0 * math.sin(theta_rad)
            g = 9.8
            t_voo = 2 * vy / g
            alcance = vx * t_voo
            h_max = vy**2 / (2 * g)
            st.markdown(f'<div class="result-box">Alcance: **{alcance:.2f} m**<br>Altura máx: **{h_max:.2f} m**<br>Tempo voo: **{t_voo:.2f} s**</div>', unsafe_allow_html=True)
            
            # Gráfico
            t = np.linspace(0, t_voo, 200)
            x = vx * t
            y = vy * t - 0.5 * g * t**2
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#FF69B4', width=4)))
            fig.update_layout(title="Trajetória do Projétil", xaxis_title="Alcance (m)", yaxis_title="Altura (m)", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.subheader("Resolução Passo a Passo")
        st.latex(r"v_x = v_0 \cos\theta \quad v_y = v_0 \sin\theta")
        st.latex(r"t_{voo} = \frac{2 v_y}{g}")
        st.latex(r"Alcance = v_x \cdot t_{voo}")

elif opcao == "Lei de Hooke (Mola)":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Lei de Hooke")
        k = ler_float("Constante k (N/m)", 200.0)
        x = ler_float("Deformação x (m)", 0.05)
        if st.button("Calcular"):
            f = -k * x
            e = 0.5 * k * x**2
            st.markdown(f'<div class="result-box">F = **{f:.2f} N**<br>Energia = **{e:.2f} J**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"F = -k x")
        st.latex(r"E = \frac{1}{2} k x^2")

elif opcao == "Potência Mecânica":
    tab1, tab2 = st.tabs(["🧮 Calculadora", "📖 Resolução"])
    with tab1:
        st.subheader("Potência Mecânica")
        modo = st.radio("Escolha o modo:", ["Trabalho / Tempo", "Força × Velocidade"])
        if modo == "Trabalho / Tempo":
            trabalho = ler_float("Trabalho (J)", 1000.0)
            tempo = ler_float("Tempo (s)", 10.0, min_value=0.001)
            if st.button("Calcular"):
                p = trabalho / tempo
                st.markdown(f'<div class="result-box">P = **{p:.2f} W**</div>', unsafe_allow_html=True)
        else:
            f = ler_float("Força (N)", 500.0)
            v = ler_float("Velocidade (m/s)", 10.0)
            if st.button("Calcular"):
                p = f * v
                st.markdown(f'<div class="result-box">P = **{p:.2f} W**</div>', unsafe_allow_html=True)
    with tab2:
        st.latex(r"P = \frac{W}{t} \quad \text{ou} \quad P = F \cdot v")

st.caption("✅ Calculadora de Física com abas de Resolução | Feito para Mateus")
