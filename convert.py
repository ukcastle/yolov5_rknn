from convert_src.onnx2rknn import onnx2rknn
from convert_src.pt2onnx import loadModel, pt2onnx
from time import time
from pathlib import Path
import yaml
import shutil
import argparse

class TimeChecker:
  def __init__(self) -> None:
    self.outputDict = {}

  def checkStatus(self, func):
    def wrapper(*args, **kwargs):
      startTime = time()
      result = func(*args, **kwargs)
      endTime = time()-startTime
      if result == -1:
        print(f"function : {func.__name__} is failed")
        exit(result)
      
      self.outputDict[f"{func.__module__}.{func.__name__}"] = f"{endTime:.4f}"
      return result
    return wrapper
  
  def wrap(self, func):
    return self.checkStatus(func)

  def printTime(self):
    for k,v in self.outputDict.items():
      print(f"function : {k} , time : {v}")


def parseArg():
  parser = argparse.ArgumentParser()
  parser.add_argument("--weights", required=True)
  return parser.parse_args()

def main(expPath):
  with open("convert_src/config.yaml", "r") as f:
    cfg = yaml.safe_load(f)
  ptPath, onnxPath, rknnPath = [expPath / x for x in [cfg["pt"],cfg["onnx"], cfg["rknn"]]]

  model = loadModel(ptPath)
  pt2onnx(model, onnxPath, cfg["ONNX_OPSET"], cfg["SIZE"])
  onnx2rknn(cfg["VERBOSE"], cfg["CONFIG_DICT"], onnxPath, cfg["BUILD_DICT"], rknnPath)

  shutil.copy(rknnPath, cfg["rknn"])

if __name__ == '__main__':
  timeChecker = TimeChecker()
  loadModel = timeChecker.wrap(loadModel)
  pt2onnx = timeChecker.wrap(pt2onnx)
  onnx2rknn = timeChecker.wrap(onnx2rknn)

  args = parseArg()
  main(Path(args.exp))
  
  timeChecker.printTime()