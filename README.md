## Install

```bash
conda create -n {env name} python=3.6.13
conda activate {env name}
chmod 755 install.sh
./install.sh
```

## Train

- Using train.sh

```sh
#!/bin/bash

CMD=""

function addArg {
  if [ "$#" -eq 1 ]; then
    CMD+=" --$1"
  elif [ "$#" -eq 2 ]; then
    CMD+=" --$1 $2"
  fi
}

addArg "weights" "models/yolov5s.pt"
addArg "cfg" "models/yolov5s.yaml"
addArg "data" "data/face_detection.yaml"
addArg "hyp" "data/hyps/hyp.face_detection.yaml"
addArg "epochs" 50
addArg "batch-size" 128
addArg "imgsz" 320
addArg "rect"
addArg "single-cls"
addArg "optimizer" "AdamW"
addArg "project" "runs/facedetection"
# addArg "name" "v5s"
addArg "seed" 42

python train.py $CMD
```

`./train.sh`


## Converting 

- fix convert_src/config.yaml

```bash
python convert.py --weights {exp/weights path}
```