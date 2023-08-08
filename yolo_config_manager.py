import argparse
import yaml

class YOLOConfig:
    def __init__(self, train_path='/dataset/train', val_path='/dataset/val', nc=2, names=["Ball Carrier", "Player"]):
        self.config = {
            'train': train_path,
            'val': val_path,
            'nc': nc,
            'names': names
        }
    
    def save_to_yaml(self, filename='data.yaml'):
        with open(filename, 'w') as file:
            yaml.dump(self.config, file, default_flow_style=False)
    
    def load_from_yaml(self, filename='model.yaml'):
        with open(filename, 'r') as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)
        return self.config

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create YOLO Config File with Custom Parameters')
    parser.add_argument('--train_path', default='/dataset/train', help='Path to the training data.')
    parser.add_argument('--val_path', default='/dataset/val', help='Path to the validation data.')
    parser.add_argument('--nc', type=int, default=2, help='Number of classes.')
    parser.add_argument('--names', nargs='+', default=["Ball Carrier", "Player"], help='Names of the classes.')

    args = parser.parse_args()

    yolo_config = YOLOConfig(args.train_path, args.val_path, args.nc, args.names)
    yolo_config.save_to_yaml()

