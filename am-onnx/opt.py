#!/usr/bin/env python3

import sys
import onnxruntime as rt

sess_options = rt.SessionOptions()

sess_options.log_severity_level = 0
sess_options.graph_optimization_level = rt.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
sess_options.optimized_model_filepath = sys.argv[2]

session = rt.InferenceSession(sys.argv[1], sess_options)
