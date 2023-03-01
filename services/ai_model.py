import torch
import torchvision.transforms as transforms
import timm


class FaceEmotionRecognition:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, model_name='efficientnet_b0', model_path='./services/model_best.pth', gpu=False):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.model_name = model_name
            self.model_path = model_path
            self.gpu = gpu

            self.model = self.load_model()
            self.transform = get_transform()
            self.labels = ['natural', 'angry', 'embarrass', 'fear', 'happy', 'hurt', 'sad']
            cls._init = True

    def __call__(self, img, *args, **kwargs):
        img = self.transform(img).unsqueeze(0)
        prob = self.model(img)
        predict = torch.argmax(prob)
        return self.labels[predict]

    def load_model(self):
        model = timm.create_model('efficientnet_b0', num_classes=7)
        model.load_state_dict(torch.load(self.model_path)['state_dict'])
        model.to('cuda' if self.gpu else 'cpu')
        return model


def get_transform():
    interpolation = transforms.functional.InterpolationMode('bicubic')
    return transforms.Compose([
        transforms.Resize(256, interpolation=interpolation),
        transforms.CenterCrop((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])
