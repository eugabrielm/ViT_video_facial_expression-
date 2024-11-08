import os
import json
import argparse
import cv2
from transformers import AutoModelForImageClassification, AutoImageProcessor
import torch
from PIL import Image

parser = argparse.ArgumentParser(description="Fazer predições de um vídeo")
parser.add_argument("video_path", type=str, help="Caminho para o vídeo de entrada")
parser.add_argument("output_json", type=str, help="Caminho para salvar os resultados das predições em formato JSON")
args = parser.parse_args()

# Função para fazer predição com ViT
def predict_frame(frame, model, image_processor, labels):
    # Convertendo o frame do OpenCV (BGR) para PIL (RGB)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(frame)
    inputs = image_processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1).squeeze()  # Calcula as probabilidades
        
        # Ordena as classes por probabilidade em ordem decrescente
        sorted_probs = sorted(
            [(labels[i], probabilities[i].item()) for i in range(len(labels))],
            key=lambda x: x[1], reverse=True
        )
        
    # Retorna uma lista de rótulos e probabilidades em ordem decrescente
    return {"probabilities": sorted_probs}

# Carregar o modelo ViT e o image processor
model_name = "motheecreator/vit-Facial-Expression-Recognition"
model = AutoModelForImageClassification.from_pretrained(model_name)
image_processor = AutoImageProcessor.from_pretrained(model_name)

# Carregar os rótulos das classes do modelo
labels = model.config.id2label

# Capturar frames do vídeo usando OpenCV
cap = cv2.VideoCapture(args.video_path)
fps = cap.get(cv2.CAP_PROP_FPS)  # Captura a taxa de quadros do vídeo
frame_interval = int(fps)  # Captura um frame por segundo

predictions = {
    "framerate": fps,  # Adiciona a taxa de quadros ao dicionário
    "frames": []       # Inicializa uma lista para armazenar as predições de cada frame
}

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Realiza a predição no frame atual
    if frame_count % frame_interval == 0:
        prediction = predict_frame(frame, model, image_processor, labels)
        # Adiciona a predição do frame à lista
        predictions["frames"].append({
            "frame_number": frame_count // frame_interval,
            "prediction": prediction
        })

    frame_count += 1

cap.release()

# Salvar as predições em um arquivo JSON
with open(args.output_json, "w") as f:
    json.dump(predictions, f, indent=4)

print(f"Predições salvas em {args.output_json}")
