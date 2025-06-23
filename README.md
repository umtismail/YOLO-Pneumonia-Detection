# 🫁 YOLO-Pneumonia-Detection

This project focuses on detecting pneumonia in chest X-ray images using the YOLO (You Only Look Once) object detection algorithm. The model is trained to distinguish between two types of pneumonia: **bacterial pneumonia** and **viral pneumonia**.

---

## 🔍 Project Objective

The goal of this project is to automate the detection of pneumonia in chest X-ray images to assist radiologists and accelerate the diagnostic process. Thanks to the YOLO architecture, the system can provide real-time predictions with high accuracy.

---

## 🧠 Technologies Used

- Python
- YOLOv5 (Ultralytics)
- OpenCV
- PyTorch
- Matplotlib
- NumPy
- Google Colab (optional)

---

## 📁 Dataset

Dataset used: **Chest X-Ray Images (Pneumonia)**  
Source: [Mendeley Data - Chest X-Ray Images for Classification](https://data.mendeley.com/datasets/rscbjbr9sj/2)

The dataset consists of 3 main folders:
- `NORMAL`
- `PNEUMONIA/Bacterial`
- `PNEUMONIA/Viral`

> ⚠️ Note: The model was trained only on **bacterial** and **viral** pneumonia images.

---

## 🏗️ Model Training

The model was trained using YOLOv5. Images were labeled in `YOLO format` and split into training and validation sets.

**Training Configuration:**
- Epochs: 100  
- Batch Size: 16  
- Image Size: 640x640  
- Optimizer: SGD / Adam  
- Loss: Default YOLO loss function

---

## 📈 Performance Metrics

| Metric         | Value  |
|----------------|--------|
| Precision      | 91.3%  |
| Recall         | 89.7%  |
| mAP@0.5        | 90.5%  |
| mAP@0.5:0.95   | 83.2%  |

> Note: Metrics are based on validation set performance.

---

## 🖼️ Sample Predictions

Below are some example predictions made by the model on test images:

![image](https://github.com/user-attachments/assets/10a56926-59ee-4bb4-91b9-730010f78483)

---
