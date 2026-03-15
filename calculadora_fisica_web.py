import streamlit as st
import math

# Configuração da página
st.set_page_config(page_title="Calculadora de Física - Mateus", layout="centered")

# Fundo roxo suave
st.markdown(
    """
    <style>
        .stApp {
            background-color: #4B0082;  /* Cor indigo */
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

# Função auxiliar para inputs
def ler_float(label, key):
    return st.number_input(label, value=0.0, step=0.1, format="%.2f", key=key)

# Menu lateral
opcao = st.sidebar.selectbox(
    "Escolha o cálculo:",
    [
        "Velocidade média",
        "Posição em MRU (S = v · t)",
        "Aceleração",
        "Posição final (MRUV)",
        "Velocidade final (MRUV)",
        "Energia cinética",
        "Força (F = m·a)"
    ]
)

st.markdown("---")

if opcao == "Velocidade média":
    st.subheader("Velocidade Média (Vm = Δs / Δt)")
    st.image("https://s2.static.brasilescola.uol.com.br/img/2018/09/movimento-uniforme-be(6).jpeg", 
             caption="Ilustração clássica de movimento uniforme e velocidade média (carro percorrendo distâncias iguais em tempos iguais)", 
             use_column_width=True)
    ds = ler_float("Deslocamento (Δs) em metros", "vm_ds")
    dt = ler_float("Tempo (Δt) em segundos", "vm_dt")
    
    if st.button("Calcular Vm") and dt > 0:
        vm = ds / dt
        st.success(f"Velocidade média = **{vm:.2f} m/s**")
        st.info(f"(≈ {vm * 3.6:.1f} km/h)")
    elif dt <= 0 and st.button("Calcular Vm"):
        st.error("Tempo deve ser maior que zero!")

elif opcao == "Posição em MRU (S = v · t)":
    st.subheader("Posição em MRU (S = v · t)")
    st.image("https://mentalmapsbrasil.com.br/wp-content/uploads/2024/11/movimento-retilineo-uniforme-MRU-mapa-mental.webp", 
             caption="Mapa mental completo de MRU: S = S₀ + v t, gráficos e exemplos", 
             use_column_width=True)
    st.info("Se S₀ = 0, simplifica para S = v · t (velocidade constante).")
    
    s0 = ler_float("Posição inicial (S₀) em metros (0 se não souber)", "mru_s0")
    v = ler_float("Velocidade constante (v) em m/s", "mru_v")
    t = ler_float("Tempo (t) em segundos", "mru_t")
    
    if st.button("Calcular Posição S") and t >= 0:
        s = s0 + v * t
        st.success(f"Posição final S = **{s:.2f} metros**")
        
        if s0 == 0:
            st.info(f"(Simplificado: S = v · t = {v:.2f} × {t:.2f} = {s:.2f} m)")
        else:
            st.info(f"(Completo: S = S₀ + v · t = {s0:.2f} + {v:.2f} × {t:.2f} = {s:.2f} m)")
        
        if v == 0:
            st.warning("Velocidade zero → o objeto está parado!")
    elif t < 0 and st.button("Calcular Posição S"):
        st.error("Tempo não pode ser negativo!")

elif opcao == "Aceleração":
    st.subheader("Aceleração (a = Δv / Δt)")
    st.image("https://br.neurochispas.com/wp-content/uploads/2023/06/Grafico-de-velocidade-vs-tempo-con-declive-e-area.png", 
             caption="Gráfico velocidade vs tempo: declive = aceleração, área = deslocamento", 
             use_column_width=True)
    v0 = ler_float("Velocidade inicial (v₀) em m/s", "a_v0")
    vf = ler_float("Velocidade final (v) em m/s", "a_vf")
    t = ler_float("Tempo (Δt) em segundos", "a_t")
    
    if st.button("Calcular a") and t > 0:
        a = (vf - v0) / t
        st.success(f"Aceleração a = **{a:.2f} m/s²**")
        if a > 0:
            st.info("→ Acelerando")
        elif a < 0:
            st.info("→ Desacelerando")
        else:
            st.info("→ Velocidade constante")
    elif t <= 0 and st.button("Calcular a"):
        st.error("Tempo deve ser maior que zero!")

elif opcao == "Posição final (MRUV)":
    st.subheader("Posição final (s = s₀ + v₀t + ½at²)")
    st.image("https://i.ytimg.com/vi/nRbb6c2I1lk/sddefault.jpg", 
             caption="Equações do MRUV: posição final e velocidade final com aceleração constante", 
             use_column_width=True)
    s0 = ler_float("Posição inicial (s₀) em metros", "mruv_s0")
    v0 = ler_float("Velocidade inicial (v₀) em m/s", "mruv_v0")
    a = ler_float("Aceleração (a) em m/s²", "mruv_a")
    t = ler_float("Tempo (t) em segundos", "mruv_t")
    
    if st.button("Calcular s") and t >= 0:
        s = s0 + v0 * t + 0.5 * a * t**2
        st.success(f"Posição final s = **{s:.2f} metros**")
    elif t < 0 and st.button("Calcular s"):
        st.error("Tempo não pode ser negativo!")

elif opcao == "Velocidade final (MRUV)":
    st.subheader("Velocidade final (v = v₀ + at)")
    st.image("https://i.ytimg.com/vi/6YBsPJtNoQI/maxresdefault.jpg", 
             caption="Gráfico de velocidade no MRUV: v = v₀ + at (área = deslocamento médio)", 
             use_column_width=True)
    v0 = ler_float("Velocidade inicial (v₀) em m/s", "vf_v0")
    a = ler_float("Aceleração (a) em m/s²", "vf_a")
    t = ler_float("Tempo (t) em segundos", "vf_t")
    
    if st.button("Calcular v") and t >= 0:
        v = v0 + a * t
        st.success(f"Velocidade final v = **{v:.2f} m/s**")
    elif t < 0 and st.button("Calcular v"):
        st.error("Tempo não pode ser negativo!")

elif opcao == "Energia cinética":
    st.subheader("Energia Cinética (Ec = ½ m v²)")
    st.image("https://i.ytimg.com/vi/tO3ieXbaS60/maxresdefault.jpg", 
             caption="Dedução da fórmula de energia cinética Ec = ½mv²", 
             use_column_width=True)
    m = ler_float("Massa (m) em kg", "ec_m")
    v = ler_float("Velocidade (v) em m/s", "ec_v")
    
    if st.button("Calcular Ec") and m > 0:
        ec = 0.5 * m * v**2
        st.success(f"Energia cinética Ec = **{ec:.2f} J**")
    elif m <= 0 and st.button("Calcular Ec"):
        st.error("Massa deve ser positiva!")

elif opcao == "Força (F = m·a)":
    st.subheader("Força – 2ª Lei de Newton (F = m · a)")
    st.image("https://thumbs.dreamstime.com/z/nova-segunda-lei-do-diagrama-infogr%C3%A1fico-de-movimento-como-empurrar-um-carro-e-caminh%C3%A3o-exemplo-empurrando-aplicando-for%C3%A7as-245887162.jpg", 
             caption="Ilustração da 2ª Lei de Newton: F = m × a (maior massa → menor aceleração com mesma força)", 
             use_column_width=True)
    m = ler_float("Massa (m) em kg", "f_m")
    a = ler_float("Aceleração (a) em m/s²", "f_a")
    
    if st.button("Calcular F") and m > 0:
        f = m * a
        st.success(f"Força F = **{f:.2f} N**")
    elif m <= 0 and st.button("Calcular F"):
        st.error("Massa deve ser positiva!")

st.markdown("---")
st.caption("Feito por Mateus com Python + Streamlit | Fundo roxo suave | Imagens educativas para ajudar nos estudos!")
