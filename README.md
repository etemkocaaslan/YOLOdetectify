# Yolodetectify

## Description
Yolodetectify harnesses the power of the YOLOv8m model to enable efficient object detection on custom datasets. By seamlessly integrating the `bing_photo_fetcher`, it automates the process of sourcing and organizing internet images to fit the specific requirements of YOLOv8m. Furthermore, the tool is engineered to autonomously partition datasets into training and validation sets, and the `yolo_config_manager` ensures effortless creation of the essential `data.yaml` configuration for the training pipeline. Users can interact with the model either through a user-friendly CLI or directly as a script via `model.py`.

## Features
- **Image Fetching**: Utilize `bing_photo_fetcher` to source and format images directly from the web, optimized for YOLOv8m.
- **Data Partitioning**: Automated splitting of datasets into training and validation sets ensures efficient model training.
- **YAML Configuration**: With `yolo_config_manager`, generate the `data.yaml` configuration vital for the training pipeline.
- **Dual Invocation**: Opt for either Command Line or script-based execution with `model.py`.
- **Dependencies Management**: A comprehensive `requirements.txt` file streamlines environment setup.

## Setup & Installation
1. Begin by cloning this repository to your local workspace.
   ```bash
   git clone gh repo clone etemkocaaslan/YOLOdetectify
   ```
2. Move to the newly cloned project directory:
   ```bash
   cd Yolodetectify
   ```
3. Set up your environment by installing the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Bing Photo Fetcher**:
  Download images based on search queries:
  ```bash
  python bing_photo_fetcher.py --search_queries Football soccer --num_images_per_query 100 --output_folder_name images
  ```

- **YOLO Config Manager**:
  Generate YOLO configurations:
  ```bash
  python yolo_config_manager.py --train_path /path/to/train/data --val_path /path/to/val/data --nc 2 --names Player Ball
  ```

- **Model Training**:
  To train the YOLO model:
  ```bash
  python model.py --model_name yolov8m.pt --data data.yaml --epochs 30 --imgsz 640
  ```

_Note_: Modify the paths and values in the above CLI commands according to your specific configurations.

## Contributors
- **Etem Kocaaslan** (and any other collaborators you'd like to highlight)

## License
Yolodetectify operates under *LICENSE*. Detailed licensing information is available in the LICENSE file.
