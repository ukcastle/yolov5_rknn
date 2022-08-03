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