import streamlit as str

# Configuração da página para um visual limpo
str.set_page_config(page_title="D", page_icon="💖", layout="centered")

# Estilização básica com CSS para deixar mais romântico
str.markdown("""
    <style>
    .big-title { font-size: 30px; font-weight: bold; color: #ff4b7d; text-align: center; }
    .subtitle { font-size: 18px; color: #555555; text-align: center; }
    .success-box { background-color: #ffe6ec; padding: 20px; border-radius: 10px; border: 1px solid #ffb3c6; }
    </style>
""", unsafe_allow_html=True)

# Gerenciamento de estado para controlar as etapas do formulário
if 'etapa' not in str.session_state:
    str.session_state.etapa = 1
if 'data' not in str.session_state:
    str.session_state.data = None
if 'hora' not in str.session_state:
    str.session_state.hora = None
if 'comida' not in str.session_state:
    str.session_state.comida = None

# --- ETAPA 1: O convite inicial ---
if str.session_state.etapa == 1:
    str.markdown('<p class="big-title">Quer sair comigo? 💖</p>', unsafe_allow_html=True)
    str.write("")
    
    col1, col2, col3 = str.columns([1, 2, 1])
    with col2:
        if str.button("SIM!", use_container_width=True):
            str.session_state.etapa = 2
            str.rerun()

# --- ETAPA 2: Escolha da Data e Hora ---
elif str.session_state.etapa == 2:
    str.markdown('<p class="big-title">Então, quando você está livre? 📅✨</p>', unsafe_allow_html=True)
    
    str.subheader("Escolha um dia:")
    data_escolhida = str.date_input("Selecione a data")
    
    str.subheader("Que horas?")
    # Lista de horários simulando o layout do vídeo
    horarios = ["12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
    hora_escolhida = str.select_slider("Arraste para escolher o horário", options=horarios)
    
    str.write("")
    if str.button("Definir Data ❤️", use_container_width=True):
        str.session_state.data = data_escolhida.strftime("%d/%m/%Y")
        str.session_state.hora = hora_escolhida
        str.session_state.etapa = 3
        str.rerun()

# --- ETAPA 3: Escolha da Comida (Com espaço para fotos) ---
elif str.session_state.etapa == 3:
    str.markdown('<p class="big-title">O que estamos a fim de fazer? </p>', unsafe_allow_html=True)
    str.write("Escolha uma das opções abaixo:")

    # Monte as colunas para exibir as fotos lado a lado
    col1, col2 = str.columns(2)

    with col1:
        # --- SUBISTITUA O CAMINHO COM AS SUAS FOTOS ABAIXO ---
        # Exemplo: str.image("pizza.jpg", caption="Pizza")
        str.image("jantar.jpg", caption="Sair para comer alguma besteirinha (ou não)", use_container_width=True)
        opcao_1 = str.button("essaaa", use_container_width=True)
        
        str.write("")
        str.image("unf.jpg", caption="um date cheio de bobeirinhas bobas e alguns unfollows ", use_container_width=True)
        opcao_3 = str.button("se liga em", use_container_width=True)

    with col2:
        str.image("cult.jpg", caption="um rolêzinho mais cult como de praxe e amamos", use_container_width=True)
        opcao_2 = str.button("ebaaaa", use_container_width=True)
        
        str.write("")
        str.image("tudo.jpg", caption="todas as outras opções num date só!", use_container_width=True)
        opcao_4 = str.button("old que esse", use_container_width=True)

    # Verifica qual botão de comida foi clicado
    if opcao_1: str.session_state.comida = "Opção 1"; str.session_state.etapa = 4; str.rerun()
    if opcao_2: str.session_state.comida = "Opção 2"; str.session_state.etapa = 4; str.rerun()
    if opcao_3: str.session_state.comida = "Opção 3"; str.session_state.etapa = 4; str.rerun()
    if opcao_4: str.session_state.comida = "Opção 4"; str.session_state.etapa = 4; str.rerun()

# --- ETAPA 4: Tela Final de Confirmação ---
elif str.session_state.etapa == 4:
    str.markdown('<p class="big-title" style="font-size: 40px; margin-bottom: 25px;">EBA!! 💕</p>', unsafe_allow_html=True)
    
    # Cartão de confirmação estilizado com alto contraste e sombras
    str.markdown(f"""
    <div style="
        background-color: #ffe6ec; 
        padding: 30px; 
        border-radius: 15px; 
        border: 2px solid #ffb3c6;
        box-shadow: 0px 4px 15px rgba(255, 75, 125, 0.15);
        max-width: 450px;
        margin: 0 auto;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    ">
        <div style="font-size: 20px; color: #2c2c2c; margin-bottom: 12px; display: flex; align-items: center;">
            <span style="margin-right: 15px; font-size: 24px;">📅</span> 
            <strong>Data:</strong> <span style="margin-left: 8px; color: #ff4b7d; font-weight: bold;">{str.session_state.data}</span>
        </div>
        <div style="font-size: 20px; color: #2c2c2c; margin-bottom: 12px; display: flex; align-items: center;">
            <span style="margin-right: 15px; font-size: 24px;">⏰</span> 
            <strong>Horário:</strong> <span style="margin-left: 8px; color: #ff4b7d; font-weight: bold;">{str.session_state.hora}</span>
        </div>
        <div style="font-size: 20px; color: #2c2c2c; display: flex; align-items: center;">
            <span style="margin-right: 15px; font-size: 24px;">💕</span> 
            <strong>Escolha:</strong> <span style="margin-left: 8px; color: #ff4b7d; font-weight: bold;">{str.session_state.comida}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    str.write("")
    str.write("")
    str.markdown('<p style="font-size: 22px; color: #ffb3c6; text-align: center; font-style: italic; font-weight: 500;">nem acredito que minha namorada aceitou, eba! ✨🥂</p>', unsafe_allow_html=True)
    str.markdown('<p style="font-size: 14px; color: #888888; text-align: center; margin-top: 20px;">(meio que tô morrendo de saudade de você)</p>', unsafe_allow_html=True)

