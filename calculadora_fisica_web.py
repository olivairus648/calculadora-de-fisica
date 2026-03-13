import streamlit as st

st.set_page_config(page_title="Calculadora de Física - Mateus", layout="centered")

st.title("Calculadora de Física - Mateus 🚀")
st.markdown("Escolha uma fórmula e preencha os valores. Tudo em m/s, m, kg, s, etc.")

# Menu lateral
opcao = st.sidebar.selectbox(
    "Escolha o cálculo:",
    [
        "Velocidade média",
        "Aceleração",
        "Posição final (MRUV)",
        "Velocidade final (MRUV)",
        "Energia cinética",
        "Força (F = m·a)"
    ]
)

st.markdown("---")

def ler_float(label, key):
    return st.number_input(label, value=0.0, step=0.1, format="%.2f", key=key)

if opcao == "Velocidade média":
    st.subheader("Velocidade Média (Vm = Δs / Δt)")
    ds = ler_float("Deslocamento (Δs) em metros", "vm_ds")
    dt = ler_float("Tempo (Δt) em segundos", "vm_dt")
    
    if st.button("Calcular Vm") and dt > 0:
        vm = ds / dt
        st.success(f"Velocidade média = **{vm:.2f} m/s**")
        st.info(f"(≈ {vm * 3.6:.1f} km/h)")
    elif dt <= 0 and st.button("Calcular Vm"):
        st.error("Tempo deve ser maior que zero!")

elif opcao == "Aceleração":
    st.subheader("Aceleração (a = Δv / Δt)")
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
    m = ler_float("Massa (m) em kg", "ec_m")
    v = ler_float("Velocidade (v) em m/s", "ec_v")
    
    if st.button("Calcular Ec") and m > 0:
        ec = 0.5 * m * v**2
        st.success(f"Energia cinética Ec = **{ec:.2f} J**")
    elif m <= 0 and st.button("Calcular Ec"):
        st.error("Massa deve ser positiva!")

elif opcao == "Força (F = m·a)":
    st.subheader("Força – 2ª Lei de Newton (F = m · a)")
    m = ler_float("Massa (m) em kg", "f_m")
    a = ler_float("Aceleração (a) em m/s²", "f_a")
    
    if st.button("Calcular F") and m > 0:
        f = m * a
        st.success(f"Força F = **{f:.2f} N**")
    elif m <= 0 and st.button("Calcular F"):
        st.error("Massa deve ser positiva!")

st.markdown("---")
st.caption("Feito por Mateus com Python + Streamlit | Use nas aulas de Física!")