!pip install streamlit
!pip install pyngrok


%%writefile app.py
import streamlit as st

st.title("Hello from Streamlit")
st.write("This is the text you wanted to display.")

# Ngrok을 사용하여 Streamlit 앱 외부 접근 설정
from pyngrok import ngrok

# Ngrok 터널 생성
public_url = ngrok.connect(port='8501')
print(f'Public URL: {public_url}')

time.sleep(5)

!streamlit run app.py &
