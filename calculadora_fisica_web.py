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

# CSS moderno (dark purple theme, glassmorphism cards)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        * { font-family: 'Inter', sans-serif; }

        .stApp {
            background: linear-gradient(135deg, #2c0e4e 0%, #4b0082 100%);
            color: #e0d4ff;
        }

        .stSidebar {
            background: #1a0b2e !important;
            border-right: 1px solid #5a3f7d;
        }

        h1, h2, h3 { color: #d4bfff !important; text-shadow: 0 2px 4px rgba(0,0,0,0.4); }

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

        hr { border-color: #5a3f7d; margin: 2rem 0; }

        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("Calculadora de Física - Mateus 🚀")
st.markdown("Escolha uma fórmula, veja a ilustração e calcule! Unidades em SI (m, m/s, s, kg, etc.)")

def ler_float(label, key, value=0.0, step=0.1, min_value=None):
    return st.number_input(
        label,
        value=value,
        step=step,
        format="%.2f",
        key=key,
        min_value=min_value
    )

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
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Velocidade Média (Vm = Δs / Δt)")
        st.image("https://s2.static.brasilescola.uol.com.br/img/2018/09/movimento-uniforme-be(6).jpeg", use_column_width=True)
        col1, col2 = st.columns(2)
        with col1: ds = ler_float("Deslocamento (Δs) [m]", "vm_ds")
        with col2: dt = ler_float("Tempo (Δt) [s]", "vm_dt")
        if st.button("Calcular Vm", key="btn_vm"):
            if dt > 0:
                vm = ds / dt
                st.markdown(f'<div class="result-box">Velocidade média = **{vm:.2f} m/s** ≈ **{vm*3.6:.1f} km/h**</div>', unsafe_allow_html=True)
            else:
                st.error("Tempo deve ser maior que zero!")
        st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Posição em MRU (S = v · t)":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Posição em MRU (S = v · t)")
        st.image("https://mentalmapsbrasil.com.br/wp-content/uploads/2024/11/movimento-retilineo-uniforme-MRU-mapa-mental.webp", use_column_width=True)
        col1, col2, col3 = st.columns(3)
        with col1: s0 = ler_float("Posição inicial (S₀) [m]", "mru_s0")
        with col2: v = ler_float("Velocidade (v) [m/s]", "mru_v")
        with col3: t = ler_float("Tempo (t) [s]", "mru_t", min_value=0.0)
        if st.button("Calcular Posição S", key="btn_mru_s"):
            if t >= 0:
                s = s0 + v * t
                st.markdown(f'<div class="result-box">Posição final S = **{s:.2f} m**</div>', unsafe_allow_html=True)
                if s0 == 0: st.info(f"Simplificado: {v:.2f} × {t:.2f} = {s:.2f} m")
                if v == 0: st.warning("Objeto parado!")
            else:
                st.error("Tempo não pode ser negativo!")
        st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Aceleração":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Aceleração (a = Δv / Δt)")
        st.image("https://br.neurochispas.com/wp-content/uploads/2023/06/Grafico-de-velocidade-vs-tempo-con-declive-e-area.png", use_column_width=True)
        col1, col2, col3 = st.columns(3)
        with col1: v0 = ler_float("v₀ [m/s]", "a_v0")
        with col2: vf = ler_float("vf [m/s]", "a_vf")
        with col3: t = ler_float("Δt [s]", "a_t", min_value=0.0)
        if st.button("Calcular a", key="btn_aceleracao"):
            if t > 0:
                a = (vf - v0) / t
                st.markdown(f'<div class="result-box">a = **{a:.2f} m/s²**</div>', unsafe_allow_html=True)
                if a > 0: st.info("→ Acelerando")
                elif a < 0: st.info("→ Desacelerando")
            else:
                st.error("Tempo > 0")
        st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Posição final (MRUV)":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Posição final (s = s₀ + v₀ t + ½ a t²)")
        st.image("https://i.ytimg.com/vi/nRbb6c2I1lk/sddefault.jpg", use_column_width=True)
        col1, col2 = st.columns(2)
        with col1:
            s0 = ler_float("s₀ [m]", "mruv_s0")
            v0 = ler_float("v₀ [m/s]", "mruv_v0")
        with col2:
            a = ler_float("a [m/s²]", "mruv_a")
            t = ler_float("t [s]", "mruv_t", min_value=0.0)
        if st.button("Calcular s", key="btn_mruv_s"):
            if t >= 0:
                s = s0 + v0 * t + 0.5 * a * t**2
                st.markdown(f'<div class="result-box">s = **{s:.2f} m**</div>', unsafe_allow_html=True)
            else:
                st.error("Tempo ≥ 0")
        st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Velocidade final (MRUV)":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Velocidade final (v = v₀ + a t)")
        st.image("https://i.ytimg.com/vi/6YBsPJtNoQI/maxresdefault.jpg", use_column_width=True)
        col1, col2, col3 = st.columns(3)
        with col1: v0 = ler_float("v₀ [m/s]", "vf_v0")
        with col2: a = ler_float("a [m/s²]", "vf_a")
        with col3: t = ler_float("t [s]", "vf_t", min_value=0.0)
        if st.button("Calcular v", key="btn_mruv_v"):
            if t >= 0:
                v = v0 + a * t
                st.markdown(f'<div class="result-box">v = **{v:.2f} m/s**</div>', unsafe_allow_html=True)
            else:
                st.error("Tempo ≥ 0")
        st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Energia cinética":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Energia Cinética (Ec = ½ m v²)")
        st.image("https://i.ytimg.com/vi/tO3ieXbaS60/maxresdefault.jpg", use_column_width=True)
        col1, col2 = st.columns(2)
        with col1: m = ler_float("Massa (m) [kg]", "ec_m", min_value=0.001)
        with col2: v = ler_float("Velocidade (v) [m/s]", "ec_v")
        if st.button("Calcular Ec", key="btn_ec"):
            if m > 0:
                ec = 0.5 * m * v**2
                st.markdown(f'<div class="result-box">Ec = **{ec:.2f} J**</div>', unsafe_allow_html=True)
            else:
                st.error("Massa deve ser positiva!")
        st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Força (F = m·a)":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Força (F = m · a)")
        st.image("https://thumbs.dreamstime.com/z/nova-segunda-lei-do-diagrama-infogr%C3%A1fico-de-movimento-como-empurrar-um-carro-e-caminh%C3%A3o-exemplo-empurrando-aplicando-for%C3%A7as-245887162.jpg", use_column_width=True)
        col1, col2 = st.columns(2)
        with col1: m = ler_float("Massa (m) [kg]", "f_m", min_value=0.001)
        with col2: a = ler_float("Aceleração (a) [m/s²]", "f_a")
        if st.button("Calcular F", key="btn_forca"):
            if m > 0:
                f = m * a
                st.markdown(f'<div class="result-box">F = **{f:.2f} N**</div>', unsafe_allow_html=True)
            else:
                st.error("Massa deve ser positiva!")
        st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Queda Livre / Lançamento Vertical":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Queda Livre / Lançamento Vertical")
        st.image("https://i.ytimg.com/vi/gWpTBwtWymA/maxresdefault.jpg", use_column_width=True)
        v0 = ler_float("Velocidade inicial (v₀) [m/s]", "queda_v0", min_value=0.0)
        if st.button("Calcular Queda Livre", key="btn_queda_livre"):
            if v0 >= 0:
                g = 9.8
                t_sub = v0 / g
                h_max = v0**2 / (2 * g)
                t_total = 2 * t_sub
                st.markdown(f'<div class="result-box">Altura máxima: **{h_max:.2f} m**  \nTempo total: **{t_total:.2f} s**  \nVel. impacto: **{-v0:.2f} m/s**</div>', unsafe_allow_html=True)
            else:
                st.error("v₀ ≥ 0 para lançamento para cima")
        st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Lei de Hooke (Mola)":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Lei de Hooke – Força em Mola")
        st.image("https://i.ytimg.com/vi/Ulg1uoXmz-o/maxresdefault.jpg", use_column_width=True)
        k = ler_float("Constante k [N/m]", "hooke_k", min_value=0.001)
        x = ler_float("Deformação x [m]", "hooke_x")
        if st.button("Calcular Mola", key="btn_hooke"):
            if k > 0:
                forca = -k * x
                energia = 0.5 * k * x**2
                st.markdown(f'<div class="result-box">F = **{forca:.2f} N** (restauradora)  \nEnergia elástica = **{energia:.2f} J**</div>', unsafe_allow_html=True)
            else:
                st.error("k deve ser positiva!")
        st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Potência Mecânica (P = τ / t ou P = F · v)":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Potência Mecânica")
        st.image("https://image.slidesharecdn.com/trabalhoepotncia-131003153056-phpapp01/75/Trabalho-e-potencia-3-2048.jpg", use_column_width=True)
        modo = st.radio("Modo:", ["Trabalho e Tempo", "Força e Velocidade"], key="pot_modo")
        if modo == "Trabalho e Tempo":
            trabalho = ler_float("Trabalho τ [J]", "pot_trabalho")
            tempo = ler_float("Tempo t [s]", "pot_tempo", min_value=0.001)
            if st.button("Calcular Potência", key="btn_pot_trab"):
                if tempo > 0:
                    p = trabalho / tempo
                    st.markdown(f'<div class="result-box">P = **{p:.2f} W** ≈ **{p/735.5:.2f} cv**</div>', unsafe_allow_html=True)
                else:
                    st.error("Tempo > 0")
        else:
            forca = ler_float("Força F [N]", "pot_forca")
            vel = ler_float("Velocidade v [m/s]", "pot_vel")
            if st.button("Calcular Potência", key="btn_pot_fv"):
                p = forca * vel
                st.markdown(f'<div class="result-box">P = **{p:.2f} W** ≈ **{p/735.5:.2f} cv**</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif opcao == "Lançamento Oblíquo (Projétil)":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Lançamento Oblíquo – Projétil")
        st.image("https://ciencia-cultura.com/Fisica/3_0_vetores_html_files/17667@2x.png", use_column_width=True)
        col1, col2 = st.columns(2)
        with col1: v0 = ler_float("v₀ [m/s]", "proj_v0", min_value=0.0)
        with col2: theta = ler_float("θ [°]", "proj_theta", value=45.0)
        if st.button("Calcular Projétil", key="btn_projetil"):
            if v0 > 0 and 0 < theta <= 90:
                theta_rad = math.radians(theta)
                vx = v0 * math.cos(theta_rad)
                vy = v0 * math.sin(theta_rad)
                g = 9.8
                t_voo = 2 * vy / g
                alcance = vx * t_voo
                h_max = vy**2 / (2 * g)
                st.markdown(f'<div class="result-box">Alcance: **{alcance:.2f} m**  \nAltura máx: **{h_max:.2f} m**  \nTempo voo: **{t_voo:.2f} s**</div>', unsafe_allow_html=True)
                # Gráfico
                t = np.linspace(0, t_voo, 100)
                x = vx * t
                y = vy * t - 0.5 * g * t**2
                fig, ax = plt.subplots()
                ax.plot(x, y, color='#a78bfa')
                ax.set_xlabel("Alcance (m)")
                ax.set_ylabel("Altura (m)")
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
            else:
                st.error("v₀ > 0 e 0° < θ ≤ 90°")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Feito por Mateus | Python + Streamlit | 2026")
