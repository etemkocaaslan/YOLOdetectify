import argparse
from ultralytics import YOLO

class Model:
    def __init__(self, model_name='yolov8m.pt', data='data.yaml', epochs=100, imgsz=640):
        self.model_name = model_name
        self.data = data
        self.epochs = epochs
        self.imgsz = imgsz

    def train_model(self):
        model = YOLO(self.model_name)
        model.train(data=self.data, epochs=self.epochs, imgsz=self.imgsz)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train YOLO Model with Custom Parameters')
    parser.add_argument('--model_name', default='yolov8m.pt', help='Path to the model file.')
    parser.add_argument('--data', default='data.yaml', help='Path to the data configuration file.')
    parser.add_argument('--epochs', type=int, default=100, help='Number of training epochs.')
    parser.add_argument('--imgsz', type=int, default=640, help='Image size for training.')

    args = parser.parse_args()

    custom_model = Model(args.model_name, args.data, args.epochs, args.imgsz)
    custom_model.train_model()

