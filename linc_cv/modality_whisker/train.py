from linc_cv import WHISKER_IMAGES_PATH, WHISKER_IMAGES_TRAINTEST_PATH, \
    WHISKER_CLASSES_LUT_PATH, WHISKER_MODEL_PATH, \
    WHISKER_TRAINING_IMAGEDATAGENERATOR_PARAMS, \
    WHISKER_TESTING_IMAGEDATAGENERATOR_PARAMS, \
    WHISKER_TRAINING_LOG_PATH
from linc_cv.training import train


def train_whisker_classifier(mp=True):
    return train(
        images_dir=WHISKER_IMAGES_PATH,
        images_traintest_dir=WHISKER_IMAGES_TRAINTEST_PATH,
        lut_path=WHISKER_CLASSES_LUT_PATH,
        model_path=WHISKER_MODEL_PATH,
        training_idg_params=WHISKER_TRAINING_IMAGEDATAGENERATOR_PARAMS,
        testing_idg_params=WHISKER_TESTING_IMAGEDATAGENERATOR_PARAMS,
        training_log=WHISKER_TRAINING_LOG_PATH,
        mp=mp)
