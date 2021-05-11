#!/usr/bin/env python
"""
Run a back health posture detector to notify user every 10 seconds to straighten up their back if not.

Usage:
  run_back_health_posture.py --custom_classifier=PATH
                           [--camera_id=CAMERA_ID]
                           [--path_in=FILENAME]
                           [--path_out=FILENAME]
                           [--title=TITLE]
                           [--use_gpu]
  run_back_health_posture.py (-h | --help)

Options:
  --custom_classifier=PATH   Path to the custom classifier to use
  --path_in=FILENAME         Video file to stream from
  --path_out=FILENAME        Video file to stream to
  --title=TITLE              This adds a title to the window display
"""
import json
import os
import time

from docopt import docopt
import numpy as np
import torch

import sense.display
from sense.downstream_tasks.nn_utils import LogisticRegression
from sense.downstream_tasks.nn_utils import Pipe
from sense.downstream_tasks.postprocess import PostprocessClassificationOutput
from sense.loading import build_backbone_network
from sense.loading import load_backbone_model_from_config
from sense.loading import update_backbone_weights
from sense.controller import Controller


global_timer = time.perf_counter()


class MyBackHealthController(Controller):

    def display_prediction(self, img: np.ndarray, prediction_postprocessed: dict):
        super().display_prediction(img, prediction_postprocessed)

        global global_timer
        local_timer = time.perf_counter()
        print(local_timer, global_timer, global_timer + 60)
        if local_timer > global_timer + 10:
            prediction, prob = prediction_postprocessed['sorted_predictions'][0]
            print(prediction, prob)
            if 'unhealthy' in prediction:
                os.system("notify-send 'Warning!' 'Time to straighten your back!' -t 5000")
                os.system("zenity --error --text='Time to straighten your back!' --title='Warning!'")
            global_timer = time.perf_counter()


if __name__ == "__main__":
    # Parse arguments
    args = docopt(__doc__)
    camera_id = int(args['--camera_id'] or 0)
    path_in = args['--path_in'] or None
    path_out = args['--path_out'] or None
    custom_classifier = args['--custom_classifier'] or None
    title = args['--title'] or None
    use_gpu = args['--use_gpu']

    # Load backbone network according to config file
    backbone_model_config, backbone_weights = load_backbone_model_from_config(custom_classifier)

    # Load custom classifier
    checkpoint_classifier = torch.load(os.path.join(custom_classifier, 'best_classifier.checkpoint'))

    # Update original weights in case some intermediate layers have been finetuned
    update_backbone_weights(backbone_weights, checkpoint_classifier)

    # Create backbone network
    backbone_network = build_backbone_network(backbone_model_config, backbone_weights)

    with open(os.path.join(custom_classifier, 'label2int.json')) as file:
        class2int = json.load(file)
    INT2LAB = {value: key for key, value in class2int.items()}

    gesture_classifier = LogisticRegression(num_in=backbone_network.feature_dim,
                                            num_out=len(INT2LAB))
    gesture_classifier.load_state_dict(checkpoint_classifier)
    gesture_classifier.eval()

    # Concatenate feature extractor and met converter
    net = Pipe(backbone_network, gesture_classifier)

    postprocessor = [
        PostprocessClassificationOutput(INT2LAB, smoothing=4)
    ]

    display_ops = [
        sense.display.DisplayFPS(expected_camera_fps=net.fps,
                                 expected_inference_fps=net.fps / net.step_size),
        sense.display.DisplayTopKClassificationOutputs(top_k=1, threshold=0.1),
    ]
    display_results = sense.display.DisplayResults(title=title, display_ops=display_ops)

    # Run live inference
    controller = MyBackHealthController(
        neural_network=net,
        post_processors=postprocessor,
        results_display=display_results,
        callbacks=[],
        camera_id=camera_id,
        path_in=path_in,
        path_out=path_out,
        use_gpu=use_gpu
    )
    controller.run_inference()




