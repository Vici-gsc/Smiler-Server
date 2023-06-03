import numpy as np
import timm
import torch
import torchvision.transforms as transforms
from facenet_pytorch.models.mtcnn import MTCNN


class FaceEmotionRecognition:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, model_name='convnext_tiny_384_in22ft1k', model_path='/home/jiyun/mount/Smiler-Server/services/model_best.pth', gpu=True):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.model_name = model_name
            self.model_path = model_path
            self.device = 'cuda' if gpu else 'cpu'

            self.model = self.load_model()
            self.detector = MTCNN(image_size=224, post_process=False, device=self.device)
            self.transform = get_transform()
            self.labels = ['natural', 'angry', 'embarrass', 'happy', 'sad']
            cls._init = True

    def __call__(self, img, *args, **kwargs):
        face = self.detector(img)
        if face is not None:
            img = face.permute(1, 2, 0).detach().cpu().numpy().astype(np.uint8)
        else:
            img = np.array(img)
        img = self.transform(img).unsqueeze(0)
        prob = self.model(img.to(self.device))
        predict = torch.argmax(prob)
        return self.labels[predict]

    def load_model(self):
        model = timm.create_model('convnext_tiny_384_in22ft1k', num_classes=5)
        model.load_state_dict(torch.load(self.model_path)['state_dict'])
        model.to(self.device)
        return model


def get_transform():
    # interpolation = transforms.functional.InterpolationMode('bicubic')
    return transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize(384),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])
