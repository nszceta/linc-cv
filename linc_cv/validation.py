import json
import os
from operator import itemgetter

from linc_cv.predict import validate_on_image_path


def classifier_classes_lut_to_labels(lut_path):
    try:
        with open(lut_path) as f:
            class_indicies = json.load(f)
    except FileNotFoundError:
        return None
    labels = [x[0] for x in sorted(class_indicies.items(), key=itemgetter(1))]
    return labels


def validate_classifier(*, traintest_path, model, test_datagen, labels):
    results = []
    for root, dirs, files in os.walk(os.path.join(traintest_path, 'test')):
        for f in files:
            image_path = os.path.join(root, f)
            gt_label = image_path.split(os.path.sep)[-2]
            p = validate_on_image_path(
                model=model, image_path=image_path, test_datagen=test_datagen,
                labels=labels)
            results.append([gt_label, p])
    return results
