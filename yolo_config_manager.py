import yaml

class YOLOConfig:
    def __init__(self, train_path, val_path, nc, names):
        self.config = {
            'train': train_path,
            'val': val_path,
            'nc': nc,
            'names': names
        }
    
    def save_to_yaml(self, filename='model.yaml'):
        with open(filename, 'w') as file:
            yaml.dump(self.config, file, default_flow_style=False)
    
    def load_from_yaml(self, filename='model.yaml'):
        with open(filename, 'r') as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)
        return self.config

if __name__ == '__main__':
    train_path = "/home/etem/Documents/GitHub/YOLOdetectify/dataset/train"
    val_path = "/home/etem/Documents/GitHub/YOLOdetectify/dataset/val"
    nc = 2
    names = ["Ball Carrier", "Player"]
    
    config = YOLOConfig(train_path, val_path, nc, names)
    config.save_to_yaml()

