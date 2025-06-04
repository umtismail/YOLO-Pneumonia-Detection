import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np
import tempfile
import os

# Başlık
st.title("🔍 YOLOv8 - Özel Model ile Nesne Tespiti")

# Modeli yükle (senin eğittiğin model: son.pt)
@st.cache_resource
def load_model():
    return YOLO('C:/Users/umtis/Downloads/son.pt')  # Eğittiğin özel modelin yolu

model = load_model()

# Görsel yükleme
uploaded_file = st.file_uploader("Bir görsel yükleyin", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Görseli göster
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Yüklenen Görsel", use_column_width=True)

    # Geçici dosya oluştur (YOLOv8 dosya yolu ister)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        image.save(temp.name)
        temp_path = temp.name

    # Tahmin yap
    st.write("📦 Nesneler tespit ediliyor...")
    results = model(temp_path)

    # Sonuçları görselleştir
    result_image = results[0].plot()
    st.image(result_image, caption="📌 Tespit Edilen Nesneler", use_column_width=True)

    # Etiketleri tablo olarak göster
    st.subheader("🧾 Tespit Edilen Etiketler")
    for box in results[0].boxes.data:
        cls_id = int(box[5].item())
        conf = float(box[4].item())
        cls_name = model.names[cls_id] if cls_id in model.names else f"Class {cls_id}"
        st.write(f"🔸 {cls_name} ({conf:.2%} güven)")

    # Geçici dosyayı sil
    os.remove(temp_path)
#python3 -m streamlit run C:/Users/umtis/OneDrive/Masaüstü/app.py