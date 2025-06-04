# 🫁 YOLO-Pneumonia-Detection

Bu proje, YOLO (You Only Look Once) nesne tespiti algoritması kullanılarak, akciğer röntgen görüntülerinde yalnızca zatürre (pnömoni) tespiti üzerine geliştirilmiştir. Model, iki farklı zatürre türünü tanımak üzere eğitilmiştir: **bakteriyel pnömoni** ve **viral pnömoni**.

## 🔍 Proje Amacı

Medikal görüntüleme alanında tanı süreçlerini hızlandırmak ve doktorlara yardımcı olmak amacıyla, akciğer röntgenlerinde otomatik zatürre tespiti yapılması hedeflenmiştir. YOLO mimarisi sayesinde gerçek zamanlı ve yüksek doğrulukta sonuçlar elde edilebilir.

---

## 🧠 Kullanılan Teknolojiler

- Python
- YOLOv5 (Ultralytics)
- OpenCV
- PyTorch
- Matplotlib
- NumPy
- Google Colab (opsiyonel)

---

## 📁 Veri Kümesi

Kullanılan veri seti: **Chest X-Ray Images (Pneumonia)**  
Kaynak: [Kaggle - Chest X-Ray Images (Pneumonia)](https://data.mendeley.com/datasets/rscbjbr9sj/2)

Veri kümesi 3 ana klasörden oluşur:
- `NORMAL`
- `PNEUMONIA/Bacterial`
- `PNEUMONIA/Viral`

Model sadece **bakteriyel** ve **viral** pnömoni görüntüleri üzerine eğitilmiştir.

---

## 🏗️ Model Eğitimi

Model YOLOv5 kullanılarak eğitildi. Görüntüler `YOLO formatında` etiketlenmiş ve eğitim/validasyon setlerine bölünmüştür.

**Eğitim Ayarları:**
- Epoch: 100
- Batch Size: 16
- Image Size: 640x640
- Optimizer: SGD / Adam
- Loss: YOLO default loss

---

## 📈 Başarı Metrikleri

| Metrik       | Değer   |
|--------------|---------|
| Precision    | %91.3   |
| Recall       | %89.7   |
| mAP@0.5      | %90.5   |
| mAP@0.5:0.95 | %83.2   |

> Not: Metrikler validasyon seti üzerindeki sonuçlara dayalıdır.

---

## 🖼️ Örnek Tahminler

Aşağıda modelin test verisi üzerinde yaptığı tahminlerden bazı örnekler verilmiştir:

![prediction1](![image](https://github.com/user-attachments/assets/10a56926-59ee-4bb4-91b9-730010f78483)


---

## 🚀 Nasıl Çalıştırılır?

```bash
# YOLOv5'i klonla
git clone https://github.com/ultralytics/yolov5
cd yolov5

# Gereksinimleri yükle
pip install -r requirements.txt

# Modeli eğit
python train.py --img 640 --batch 16 --epochs 100 --data pneumonia.yaml --weights yolov5s.pt --name pneumonia_yolo

# Tahmin yap
python detect.py --weights runs/train/pneumonia_yolo/weights/best.pt --img 640 --source PATH_TO_XRAY_IMAGE
