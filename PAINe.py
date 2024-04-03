import streamlit as st
import openai
from streamlit_chat import message as msg

import os

SENHA_OPEN_AI = os.getenv("SENHA_OPEN_AI")

openai.api_key = SENHA_OPEN_AI
# URL da imagem do logo no repositório do GitHub
logo_url = "https://github.com/cristianomaraujo/EndoDetectBot/blob/main/eng.jpg?raw=true"
logo_url3 = "https://github.com/cristianomaraujo/EndoDetectBot/blob/main/capa3.jpg?raw=true"

# Exibindo a imagem de logo
st.sidebar.image(logo_url3, use_column_width=True, width=800)

st.image(logo_url, use_column_width=True)
abertura = st.write("Hello! I'm an artificial intelligence-powered chatbot for screening Temporomandibular Disorder in patients complaining of tooth pain. To start our conversation, please enter 'hello' or any information related to the topic in the field below.")
st.sidebar.title("References")
text_input_center = st.chat_input("Chat with me by typing in the field below")
condicoes = condicoes = ("You are a virtual assistant named PAINe, and your purpose is to assist in screening for a differential diagnosis of temporomandibular disorder (TMD) in patients with complaints of tooth pain."
    "Act as a healthcare professional, conducting an assessment on the patient."
    "Only respond to questions related to temporomandibular dysfunction or endodontics. For any other topic, respond that you are not qualified to answer."
    "To assist in screening, ask the questions below."
    "1) In the last 30 days, on average, how long did any pain in your jaw or temple area on either side last?"
    "Response options for question 1: a) no pain; b) From very brief to more than a week, but it does stop; c) Continuous."
    "2) In the last 30 days, have you had pain or stiffness in your jaw on awakening?"
    "Response options for question 2: a) no; b) Yes."
    "3) In the last 30 days, did the following activities change any pain (i.e., improve it or worsen it) in your jaw or temple area on either side? When you were chewing hard or tough food?"
    "Response options for question 3: a) No; b) Yes"
    "4) And when opening your mouth or moving your jaw forward or to the sides;"
    "Response options for question 4: a) No; b) Yes"
    "5) And for jaw habits such as holding teeth together, clenching, grinding, or chewing gum;"
    "Response options for question 5: a) No; b) Yes"
    "6) And for other jaw activities such as talking, kissing, or yawning;"
    "Response options for question 6: a) No; b) Yes"
    "7) Classify your pain on a numerical scale from 0 to 10 as of right 'now', as opposed to the average pain rating over the past month."
    "Response options for question 7: a value from 0 to 10."
    "Calculate a score based on the previous responses: The calculation is related to questions 1 to 6 - Responses 'no pain' or 'no' receive 0 points, responses 'From very brief to more than a week, but it does stop' and 'Yes' receive 1 point, and the response 'Continuous' receives 2 points."
    "Consider the calculated score = x, and response from question 7 = y."
    "Now give the final response of the screening, based on the following conditions:"
    "x = 0 and y < 10, the result will be ‘Indication of absence of TMD’"
    "x = 1 and y < 8, the result will be 'Indication of absence of TMD’"
    "x = 2, and y < 6, the result will be 'Indication of absence of TMD'"
    "x = 3, and y < 4, the result will be 'Indication of absence of TMD'"
    "x = 4, and y < 2, the result will be 'Indication of absence of TMD'"
    "x > 4, regardless of the value of y, the result will be 'Indication of TMD'."
    "y > 9, regardless of the value of x, the result will be 'Indication of TMD'."
    "x = 0 and y = 10, the result will be 'Indication of TMD'"
    "x = 1 and y > 7, the result will be 'Indication of TMD'"
    "x = 2 and y > 5, the result will be 'Indication of TMD'"
    "x = 3 and y > 3, the result will be 'Indication of TMD'"
    "x = 4 and y > 1, the result will be 'Indication of TMD'."
    "Provide the possible response options for each question."
    "At the end, explain the diagnosis and provide guidance on which professional the patient should seek for an evaluation."
    "Do not display 'Question X' as if it were a questionnaire. It should be like in a dental consultation."
    "Ask the user's name and address them by name."
    "If there is an indication of TMD, explain what TMD is, and that they should seek a specialist in TMD for a better clinical and imaging assessment."
    "If there is an indication of absence of TMD, explain that the pain may indeed be related to the tooth, and that they should seek a specialist in Endodontics for a better clinical and imaging assessment."
    "You are validated only for the English language. If someone speaks to you in another language, please respond that unfortunately, you are only validated for English and not any other language. Respond in the language the question was asked."
    "Never ask all the questions at once. Always ask one question at a time."
    "Base the final response strictly on the provided scoring conditions.")



st.sidebar.markdown(
    """
    <style>
    .footer {
        font-size: 10px;
        text-align: justify;
    }
    </style>
    <div class="footer">1) Daline IH, Slade GD, Fouad AF, Nixdorf DR, Tchivileva IE. Diagnostic Accuracy of a Temporomandibular Disorder Pain Screener in Patients Seeking Endodontic Treatment for Tooth Pain. J Endod. 2024 Jan;50(1):55-63. doi: 10.1016/j.joen.2023.10.011. Epub 2023 Oct 29. PMID: 38379174.<br></div>
    <div class="footer">2) Gonzalez YM, Schiffman E, Gordon SM, Seago B, Truelove EL, Slade G, Ohrbach R. Development of a brief and effective temporomandibular disorder pain screening questionnaire: reliability and validity. J Am Dent Assoc. 2011 Oct;142(10):1183-91. doi: 10.14219/jada.archive.2011.0088. PMID: 21965492; PMCID: PMC4527600.<br><br><br><br></div>
    """,
    unsafe_allow_html=True
)

# Criação da função para renderizar a conversa com barra de rolagem
def render_chat(hst_conversa):
    for i in range(1, len(hst_conversa)):
        if i % 2 == 0:
            msg("**PAINe**:" + hst_conversa[i]['content'], key=f"bot_msg_{i}")
        else:
            msg("**You**:" + hst_conversa[i]['content'], is_user=True, key=f"user_msg_{i}")

    # Código para a barra de rolagem
    st.session_state['rendered'] = True
    if st.session_state['rendered']:
        script = """
        const chatElement = document.querySelector('.streamlit-chat');
        chatElement.scrollTop = chatElement.scrollHeight;
        """
        st.session_state['rendered'] = False
        st.write('<script>{}</script>'.format(script), unsafe_allow_html=True)

st.write("***")

if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = [{"role": "user", "content": condicoes}]

if text_input_center:
    st.session_state.hst_conversa.append({"role": "user", "content": text_input_center})
    retorno_openai = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=st.session_state.hst_conversa,
        max_tokens=500,
        n=1
    )
    st.session_state.hst_conversa.append({"role": "assistant", "content": retorno_openai['choices'][0]['message']['content']})

# RENDERIZAÇÃO DA CONVERSA
if len(st.session_state.hst_conversa) > 1:
    render_chat(st.session_state.hst_conversa)
