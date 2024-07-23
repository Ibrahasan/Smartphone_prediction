import streamlit as st
from PIL import Image

# Səhifə konfiqurasiyasını təyin edin
st.set_page_config(layout="wide")

# Başlıq və məlumatlar
st.title("The Phone Price Predictive Model")

st.write("""
         The model predicts the phone prices according to the different parameters of the given one. 
         The used algorithms are Random Forest Regressor and KNN Algorithms.""")

# Kompüterinizdə olan şəkilin yolunu təyin edin
image_path = r"C:\Users\ibrah\Downloads\smartphone_pict.jpg"  # Raw string istifadə edin

# Şəkili oxuyun
image = Image.open(image_path)

# Şəkili göstərin
st.image(image, use_column_width=True)
