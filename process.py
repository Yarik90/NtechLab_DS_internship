import torch
from torchvision import transforms
from PIL import Image
import sys
import os
import json

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Загрузка чекпоинта модели
checkpoint = 'checkpoint_resnet50.pth.tar'
checkpoint = torch.load(checkpoint)

model = checkpoint['model']
model = model.to(device)
model.eval()

resize = transforms.Resize((224, 224))
to_tensor = transforms.ToTensor()
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

def recog(image):
  image = normalize(to_tensor(resize(image)))
  image = image.to(device)
  with torch.set_grad_enabled(False):
    output = model(image.unsqueeze(0))
    _, preds = torch.max(output, 1)
  return 'male' if preds[0].to('cpu').item() == 0 else 'female'


if __name__ == '__main__':
  if len(sys.argv) > 1:
    data = {name : recog(Image.open(sys.argv[1] + name, mode='r').convert('RGB')) for name in os.listdir(sys.argv[1])}
    with open('process_results.json', 'w') as f:
      json.dump(data, f)
  else:
    print('Укажите папку с изображениями')


