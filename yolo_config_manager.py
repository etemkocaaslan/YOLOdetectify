import argparse
import yaml

class YOLOConfig:
    def __init__(self, train_path='/home/etem/Documents/GitHub/YOLOdetectify/Custom Football Dataset/train', val_path='/home/etem/Documents/GitHub/YOLOdetectify/Custom Football Dataset/val', nc=2, names=["Ball Carrier", "Player"]):
        self.config = {
            'train': train_path,
            'val': val_path,
            'nc': nc,
            'names': names
        }
    
    def save_to_yaml(self, filename='data.yaml'):
        with open(filename, 'w') as file:
            # Writing to the file directly to maintain the custom format
            file.write(f"train: {self.config['train']}\n")
            file.write(f"val: {self.config['val']}\n\n")
            file.write(f"nc: {self.config['nc']}\n\n")
            file.write("names: [")
            for i, name in enumerate(self.config['names']):
                if i != 0:
                    file.write(", ")
                file.write(f'"{name}"')
            file.write("]\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create YOLO Config File with Custom Parameters')
    parser.add_argument('--train_path', default='/home/etem/Documents/GitHub/YOLOdetectify/Custom Football Dataset/train', help='Path to the training data.')
    parser.add_argument('--val_path', default='/home/etem/Documents/GitHub/YOLOdetectify/Custom Football Dataset/val', help='Path to the validation data.')
    parser.add_argument('--nc', type=int, default=2, help='Number of classes.')
    parser.add_argument('--names', nargs='+', default=["Ball Carrier", "Player"], help='Names of the classes.')

    args = parser.parse_args()

    yolo_config = YOLOConfig(args.train_path, args.val_path, args.nc, args.names)
    yolo_config.save_to_yaml()

