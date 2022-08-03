import torch
from models.experimental import attempt_load
from models.yolo import Detect

@torch.no_grad()
def loadModel(weights):
  model = attempt_load(weights)
  model.eval()

  for _, m in model.named_modules():
    if isinstance(m, Detect):
      m.isRknnExport= True
      m.export = True

  return model

@torch.no_grad()
def pt2onnx(model, onnxPath, onnxOpset, size):
  torch.onnx.export(
    model,
    torch.randn(1,3,*size),
    onnxPath,
    verbose=False,
    opset_version=onnxOpset,
    do_constant_folding = True,
    input_names=["images"],
    output_names=["P3div8","P4div16","P5div32"]
  )  
