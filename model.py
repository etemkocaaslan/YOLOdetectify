import argparse
from ultralytics import YOLO

class Model:
    def __init__(self, model_name='yolov8m.pt', data='data.yaml', epochs=30, imgsz=640):
        self.model_name = model_name
        self.data = data
        self.epochs = epochs
        self.imgsz = imgsz

    def train_model(self):
        model = YOLO(self.model_name)
        model.train(data=self.data, epochs=self.epochs, imgsz=self.imgsz,conf = 0.8)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train YOLO Model with Custom Parameters', epilog='Developed by Etem Kocaaslan.')
    parser.add_argument('--model_name', default='yolov8m.pt', help='Path to the model file.')
    parser.add_argument('--data', default='data.yaml', help='Path to the data configuration file.')
    parser.add_argument('--epochs', type=int, default=30, help='Number of training epochs.')
    parser.add_argument('--imgsz', type=int, default=640, help=f'Image size for training.')


    args = parser.parse_args()

    custom_model = Model(args.model_name, args.data, args.epochs, args.imgsz)
    custom_model.train_model()

