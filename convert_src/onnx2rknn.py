from rknn.api import RKNN # v1.7.1
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

def _setConfig(rknn : RKNN, configDict : dict):
    rknn.config(**configDict)       

def _loadModel(rknn : RKNN, path):
    return rknn.load_onnx(model=path)

def _buildModel(rknn : RKNN, buildDict : dict):
    return rknn.build(**buildDict)

def _exportModel(rknn : RKNN, outputPath):
    return rknn.export_rknn(outputPath)

def onnx2rknn(verbose, configDict, onnxPath, buildDict, outputPath):
    rknn = RKNN(verbose=verbose)
    _setConfig(rknn, configDict)
    _loadModel(rknn, onnxPath)
    _buildModel(rknn, buildDict)
    _exportModel(rknn, outputPath)

    rknn.release()