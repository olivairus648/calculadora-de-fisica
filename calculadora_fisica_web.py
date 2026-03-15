import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Calculadora de Física - Mateus", layout="centered")

# Fundo roxo suave + estilos
st.markdown(
    """
    <style>
        .stApp {
            background-color: #4B0082; /* Cor indigo */
        }
        .stButton > button {
            background-color: #6a4c93;
            color: white;
        }
        .stButton > button:hover {
            background-color: #5a3f7d;
        }
        h1, h2, h3 {
            color: #4a148c;
        }
        .stSuccess {
            background-color: #e8daf5 !important;
            color: #4a148c !important;
        }
        .stInfo, .stWarning, .stError {
            background-color: #f3e8ff !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Calculadora de Física - Mateus 🚀")
st.markdown("Escolha uma fórmula, veja a ilustração e calcule! Unidades: m, m/s, s, kg, etc.")

# Função auxiliar para inputs numéricos
def ler_float(label, key, value=0.0, step=0.1):
    return st.number_input(label, value=value, step=step, format="%.2f", key=key)

# Menu lateral com todas as opções
opcao = st.sidebar.selectbox(
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
        "Potência Mecânica (P = τ / t ou P = F · v)"
    ]
)

st.markdown("---")

# 1. Velocidade média
if opcao == "Velocidade média":
    st.subheader("Velocidade Média (Vm = Δs / Δt)")
    st.image("https://s2.static.brasilescola.uol.com.br/img/2018/09/movimento-uniforme-be(6).jpeg",
             caption="Ilustração clássica de movimento uniforme e velocidade média",
             use_column_width=True)
    ds = ler_float("Deslocamento (Δs) em metros", "vm_ds")
    dt = ler_float("Tempo (Δt) em segundos", "vm_dt")
   
    if st.button("Calcular Vm", key="btn_vm"):
        if dt > 0:
            vm = ds / dt
            st.success(f"Velocidade média = **{vm:.2f} m/s**")
            st.info(f"(≈ {vm * 3.6:.1f} km/h)")
        else:
            st.error("Tempo deve ser maior que zero!")

# 2. Posição em MRU
elif opcao == "Posição em MRU (S = v · t)":
    st.subheader("Posição em MRU (S = v · t)")
    st.image("https://mentalmapsbrasil.com.br/wp-content/uploads/2024/11/movimento-retilineo-uniforme-MRU-mapa-mental.webp",
             caption="Mapa mental completo de MRU",
             use_column_width=True)
    st.info("Se S₀ = 0, simplifica para S = v · t.")
   
    s0 = ler_float("Posição inicial (S₀) em metros", "mru_s0")
    v = ler_float("Velocidade constante (v) em m/s", "mru_v")
    t = ler_float("Tempo (t) em segundos", "mru_t")
   
    if st.button("Calcular Posição S", key="btn_mru_s"):
        if t >= 0:
            s = s0 + v * t
            st.success(f"Posição final S = **{s:.2f} metros**")
            if s0 == 0:
                st.info(f"(Simplificado: S = v · t = {v:.2f} × {t:.2f} = {s:.2f} m)")
            else:
                st.info(f"(Completo: S = S₀ + v · t = {s0:.2f} + {v:.2f} × {t:.2f} = {s:.2f} m)")
            if v == 0:
                st.warning("Velocidade zero → objeto parado!")
        else:
            st.error("Tempo não pode ser negativo!")

# 3. Aceleração
elif opcao == "Aceleração":
    st.subheader("Aceleração (a = Δv / Δt)")
    st.image("https://br.neurochispas.com/wp-content/uploads/2023/06/Grafico-de-velocidade-vs-tempo-con-declive-e-area.png",
             caption="Gráfico v vs t: declive = aceleração",
             use_column_width=True)
    v0 = ler_float("Velocidade inicial (v₀) em m/s", "a_v0")
    vf = ler_float("Velocidade final (vf) em m/s", "a_vf")
    t = ler_float("Tempo (Δt) em segundos", "a_t")
   
    if st.button("Calcular a", key="btn_aceleracao"):
        if t > 0:
            a = (vf - v0) / t
            st.success(f"Aceleração a = **{a:.2f} m/s²**")
            if a > 0: st.info("→ Acelerando")
            elif a < 0: st.info("→ Desacelerando")
            else: st.info("→ Velocidade constante")
        else:
            st.error("Tempo deve ser maior que zero!")

# (continua com as demais originais de forma similar - para não estender demais aqui, mas no código real mantenha todas)

# 8. Queda Livre / Lançamento Vertical
elif opcao == "Queda Livre / Lançamento Vertical":
    st.subheader("Queda Livre / Lançamento Vertical para Cima")
    st.image("https://i.ytimg.com/vi/gWpTBwtWymA/maxresdefault.jpg",
             caption="Lançamento vertical: sobe, para e cai (g = 9,8 m/s²)",
             use_column_width=True)
    st.info("v₀ positiva = para cima. g = 9.8 m/s² fixo.")

    v0 = ler_float("Velocidade inicial (v₀) em m/s", "queda_v0")
    g = 9.8

    if st.button("Calcular Queda Livre", key="btn_queda_livre"):
        if v0 >= 0:
            tempo_subida = v0 / g
            altura_max = (v0 ** 2) / (2 * g)
            tempo_total = 2 * tempo_subida
            st.success(f"**Altura máxima:** {altura_max:.2f} metros")
            st.info(f"Tempo de subida: **{tempo_subida:.2f} s**")
            st.info(f"Tempo total de voo: **{tempo_total:.2f} s**")
            st.info(f"Velocidade ao atingir o solo: **{-v0:.2f} m/s** (para baixo)")
        else:
            st.error("Velocidade inicial ≥ 0 para lançamento para cima!")

# 9. Lançamento Oblíquo (Projétil)
elif opcao == "Lançamento Oblíquo (Projétil)":
    st.subheader("Lançamento Oblíquo – Movimento de Projétil")
    st.image("https://ciencia-cultura.com/Fisica/3_0_vetores_html_files/17667@2x.png",
             caption="Trajetória parabólica do projétil",
             use_column_width=True)

    v0 = ler_float("Velocidade inicial (v₀) em m/s", "proj_v0")
    theta = ler_float("Ângulo de lançamento (θ) em graus", "proj_theta")
    g = 9.8

    if st.button("Calcular Projétil", key="btn_projetil"):
        if v0 > 0 and 0 < theta <= 90:
            theta_rad = math.radians(theta)
            vx = v0 * math.cos(theta_rad)
            vy = v0 * math.sin(theta_rad)
            tempo_voo = (2 * vy) / g
            alcance = vx * tempo_voo
            altura_max = (vy ** 2) / (2 * g)

            st.success(f"**Alcance máximo:** {alcance:.2f} metros")
            st.success(f"**Altura máxima:** {altura_max:.2f} metros")
            st.info(f"Tempo de voo total: **{tempo_voo:.2f} s**")
            st.info(f"Velocidade horizontal constante: **{vx:.2f} m/s**")

            # Gráfico da trajetória
            t = np.linspace(0, tempo_voo, 100)
            x = vx * t
            y = vy * t - 0.5 * g * t**2
            fig, ax = plt.subplots()
            ax.plot(x, y, color='blue')
            ax.set_xlabel("Alcance (m)")
            ax.set_ylabel("Altura (m)")
            ax.set_title("Trajetória Parabólica")
            ax.grid(True)
            st.pyplot(fig)
        else:
            st.error("Velocidade > 0 e ângulo entre 0° e 90°!")

# 10. Lei de Hooke (Mola)
elif opcao == "Lei de Hooke (Mola)":
    st.subheader("Lei de Hooke – Força em Mola")
    st.image("https://i.ytimg.com/vi/Ulg1uoXmz-o/maxresdefault.jpg",
             caption="Força restauradora em mola deformada",
             use_column_width=True)

    k = ler_float("Constante elástica (k) em N/m", "hooke_k")
    x = ler_float("Deformação (x) em metros", "hooke_x")

    if st.button("Calcular Mola", key="btn_hooke"):
        if k > 0:
            forca = -k * x
            energia = 0.5 * k * (x ** 2)
            st.success(f"Força restauradora: **{forca:.2f} N** (oposta à deformação)")
            st.success(f"Energia potencial elástica: **{energia:.2f} J**")
            if x == 0:
                st.info("Mola em repouso → sem força nem energia.")
        else:
            st.error("Constante k deve ser positiva!")

# 11. Potência Mecânica
elif opcao == "Potência Mecânica (P = τ / t ou P = F · v)":
    st.subheader("Potência Mecânica")
    st.image("https://image.slidesharecdn.com/trabalhoepotncia-131003153056-phpapp01/75/Trabalho-e-potencia-3-2048.jpg",
             caption="Potência = trabalho por unidade de tempo",
             use_column_width=True)

    modo = st.radio("Modo de cálculo:", ["Trabalho e Tempo", "Força e Velocidade"], key="pot_modo")

    if modo == "Trabalho e Tempo":
        trabalho = ler_float("Trabalho (τ) em Joules", "pot_trabalho")
        tempo = ler_float("Tempo (t) em segundos", "pot_tempo")
        if st.button("Calcular Potência", key="btn_pot_trab"):
            if tempo > 0:
                potencia = trabalho / tempo
                st.success(f"**Potência:** {potencia:.2f} W")
                st.info(f"≈ {potencia / 735.5:.2f} cv")
            else:
                st.error("Tempo deve ser maior que zero!")
    else:
        forca = ler_float("Força (F) em Newtons", "pot_forca")
        velocidade = ler_float("Velocidade (v) em m/s", "pot_vel")
        if st.button("Calcular Potência", key="btn_pot_fv"):
            potencia = forca * velocidade
            st.success(f"**Potência:** {potencia:.2f} W")
            st.info(f"≈ {potencia / 735.5:.2f} cv")

# Rodapé
st.markdown("---")
st.caption("Feito por Mateus com Python + Streamlit | Fundo roxo suave | Imagens educativas")
