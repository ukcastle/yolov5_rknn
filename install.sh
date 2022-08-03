# conda create -n yolo_rknn python=3.6.13 # Use 3.6!!
# conda activate yolo_rknn
pip install -r requirements.txt

wget https://github.com/ukcastle/yolov5_rknn/releases/download/1.7.1/rknn_toolkit-1.7.1-cp36-cp36m-linux_x86_64.whl
pip install rknn_toolkit-1.7.1-cp36-cp36m-linux_x86_64.whl