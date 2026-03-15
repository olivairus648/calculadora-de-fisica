import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Física - Mateus",
    layout="centered",
    initial_sidebar_state="expanded",
    page_icon="🚀"
)

# CSS moderno: dark purple gradiente, glassmorphism cards, hover effects, fonte Inter
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        * {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: linear-gradient(135deg, #2c0e4e 0%, #4b0082 100%);
            color: #e0d4ff;
        }

        .stSidebar {
            background: #1a0b2e !important;
            border-right: 1px solid #5a3f7d;
        }

        h1, h2, h3 {
            color: #d4bfff !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.4);
        }

        .stButton > button {
            background: linear-gradient(90deg, #7c3aed, #a78bfa);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }

        .stButton > button:hover {
            background: linear-gradient(90deg, #6d28d9, #8b5cf6);
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        }

        .stNumberInput > div > div > input,
        .stRadio > div {
            background: #3a1a5e;
            color: #e0d4ff;
            border: 1px solid #6d28d9;
            border-radius: 10px;
        }

        .card {
            background: rgba(90, 63, 125, 0.25);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(125, 95, 180, 0.3);
            border-radius: 16px;
            padding: 1.8rem;
            margin: 1.5rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }

        .result-box {
            background: rgba(124, 58, 237, 0.18);
            border-left: 5px solid #7c3aed;
            padding: 1.2rem;
            border-radius: 10px;
            margin: 1rem 0;
            font-weight: 500;
        }

        hr {
            border-color: #5a3f7d;
            margin: 2rem 0;
        }

        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("Calculadora de Física - Mateus 🚀")
st.markdown("Escolha uma fórmula, veja a ilustração e calcule! Unidades em SI (m, m/s, s, kg, etc.)")

# Função auxiliar para inputs
def ler_float(label, key, value=0.0, step=0.1, min_value=None):
    return st.number_input(
        label,
        value=value,
        step=step,
        format="%.2f",
        key=key,
        min_value=min_value
    )

# Sidebar
opcao = st.sidebar.selectbox(
    "Escolha o cálculo",
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
        "Potência Mecânica (P = τ / t ou P = F · v)"
    ]
)

st.markdown("---")

with st.container():
    if opcao == "Velocidade média":
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Velocidade Média (Vm = Δs / Δt)")
            st.image("https://s2.static.brasilescola.uol.com.br/img/2018/09/movimento-uniforme-be(6).jpeg",
                     caption="Ilustração clássica de movimento uniforme", use_column_width=True)
            
            col1, col2 = st.columns(2)
            with col1:
                ds = ler_float("Deslocamento (Δs) [m]", "vm_ds")
            with col2:
                dt = ler_float("Tempo (Δt) [s]", "vm_dt")  # ← corrigido: sem min_value > value
            
            if st.button("Calcular Vm", key="btn_vm"):
                if dt > 0:
                    vm = ds / dt
                    st.markdown(f'<div class="result-box">Velocidade média = **{vm:.2f} m/s** ≈ **{vm*3.6:.1f} km/h**</div>', unsafe_allow_html=True)
                else:
                    st.error("Tempo deve ser maior que zero!")
            st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Posição em MRU (S = v · t)":
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Posição em MRU (S = v · t)")
            st.image("https://mentalmapsbrasil.com.br/wp-content/uploads/2024/11/movimento-retilineo-uniforme-MRU-mapa-mental.webp",
                     caption="Mapa mental completo de MRU", use_column_width=True)
            st.info("Se S₀ = 0, simplifica para S = v · t.")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                s0 = ler_float("Posição inicial (S₀) [m]", "mru_s0")
            with col2:
                v = ler_float("Velocidade (v) [m/s]", "mru_v")
            with col3:
                t = ler_float("Tempo (t) [s]", "mru_t", min_value=0.0)
            
            if st.button("Calcular Posição S", key="btn_mru_s"):
                if t >= 0:
                    s = s0 + v * t
                    st.markdown(f'<div class="result-box">Posição final S = **{s:.2f} m**</div>', unsafe_allow_html=True)
                    if s0 == 0:
                        st.info(f"Simplificado: S = v · t = {v:.2f} × {t:.2f} = {s:.2f} m")
                    else:
                        st.info(f"Completo: S = S₀ + v · t = {s0:.2f} + {v:.2f} × {t:.2f} = {s:.2f} m")
                    if v == 0:
                        st.warning("Velocidade zero → objeto parado!")
                else:
                    st.error("Tempo não pode ser negativo!")
            st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Aceleração":
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Aceleração (a = Δv / Δt)")
            st.image("https://br.neurochispas.com/wp-content/uploads/2023/06/Grafico-de-velocidade-vs-tempo-con-declive-e-area.png",
                     caption="Gráfico v vs t: declive = aceleração", use_column_width=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                v0 = ler_float("Velocidade inicial (v₀) [m/s]", "a_v0")
            with col2:
                vf = ler_float("Velocidade final (vf) [m/s]", "a_vf")
            with col3:
                t = ler_float("Tempo (Δt) [s]", "a_t", min_value=0.0)
            
            if st.button("Calcular a", key="btn_aceleracao"):
                if t > 0:
                    a = (vf - v0) / t
                    st.markdown(f'<div class="result-box">Aceleração a = **{a:.2f} m/s²**</div>', unsafe_allow_html=True)
                    if a > 0:
                        st.info("→ Acelerando")
                    elif a < 0:
                        st.info("→ Desacelerando")
                    else:
                        st.info("→ Velocidade constante")
                else:
                    st.error("Tempo deve ser maior que zero!")
            st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Queda Livre / Lançamento Vertical":
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Queda Livre / Lançamento Vertical para Cima")
            st.image("https://i.ytimg.com/vi/gWpTBwtWymA/maxresdefault.jpg",
                     caption="Lançamento vertical: sobe, para e cai", use_column_width=True)
            st.info("v₀ positiva = para cima. g = 9.8 m/s² fixo.")
            
            v0 = ler_float("Velocidade inicial (v₀) [m/s]", "queda_v0", min_value=0.0)
            
            if st.button("Calcular Queda Livre", key="btn_queda_livre"):
                if v0 >= 0:
                    tempo_subida = v0 / 9.8
                    altura_max = (v0 ** 2) / (2 * 9.8)
                    tempo_total = 2 * tempo_subida
                    st.markdown(f'<div class="result-box">Altura máxima: **{altura_max:.2f} m**  \nTempo total: **{tempo_total:.2f} s**  \nVel. impacto: **{-v0:.2f} m/s**</div>', unsafe_allow_html=True)
                else:
                    st.error("Velocidade inicial ≥ 0!")
            st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Lançamento Oblíquo (Projétil)":
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Lançamento Oblíquo – Movimento de Projétil")
            st.image("https://ciencia-cultura.com/Fisica/3_0_vetores_html_files/17667@2x.png",
                     caption="Trajetória parabólica", use_column_width=True)
            
            col1, col2 = st.columns(2)
            with col1:
                v0 = ler_float("Velocidade inicial (v₀) [m/s]", "proj_v0", min_value=0.0)
            with col2:
                theta = ler_float("Ângulo θ [°]", "proj_theta", value=45.0)
            
            if st.button("Calcular Projétil", key="btn_projetil"):
                if v0 > 0 and 0 < theta <= 90:
                    theta_rad = math.radians(theta)
                    vx = v0 * math.cos(theta_rad)
                    vy = v0 * math.sin(theta_rad)
                    tempo_voo = (2 * vy) / 9.8
                    alcance = vx * tempo_voo
                    altura_max = (vy ** 2) / (2 * 9.8)
                    st.markdown(f'<div class="result-box">Alcance: **{alcance:.2f} m**  \nAltura máx: **{altura_max:.2f} m**  \nTempo voo: **{tempo_voo:.2f} s**</div>', unsafe_allow_html=True)
                    
                    t = np.linspace(0, tempo_voo, 100)
                    x = vx * t
                    y = vy * t - 0.5 * 9.8 * t**2
                    fig, ax = plt.subplots()
                    ax.plot(x, y, color='#a78bfa', linewidth=2.5)
                    ax.set_xlabel("Alcance (m)")
                    ax.set_ylabel("Altura (m)")
                    ax.set_title("Trajetória Parabólica")
                    ax.grid(True, alpha=0.3)
                    ax.set_facecolor('#2c0e4e')
                    fig.patch.set_facecolor('#1a0b2e')
                    st.pyplot(fig)
                else:
                    st.error("Velocidade > 0 e ângulo entre 0° e 90°!")
            st.markdown('</div>', unsafe_allow_html=True)

    # Adicione aqui os outros cálculos (Energia cinética, Força, Lei de Hooke, Potência Mecânica, etc.)
    # seguindo o mesmo padrão: .card, colunas quando possível, .result-box no sucesso

# Rodapé
st.markdown("---")
st.caption("Feito por Mateus | Python + Streamlit | Imagens educativas | 2026")
