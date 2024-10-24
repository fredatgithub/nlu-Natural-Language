from sparknlp.annotator import *
from sparknlp.base import *


class ConvNextImageClassifier:
    @staticmethod
    def get_default_model():
        return ConvNextForImageClassification \
            .pretrained() \
            .setInputCols("image_assembler") \
            .setOutputCol("classes")

    @staticmethod
    def get_pretrained_model(name, language, bucket=None):
        return ConvNextForImageClassification \
            .pretrained(name, language, bucket) \
            .setInputCols("image_assembler") \
            .setOutputCol("class")





