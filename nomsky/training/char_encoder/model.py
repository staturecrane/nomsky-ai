import tensorflow as tf

from tensorflow import keras

from nomksy.tokenizers.tokenizer import CHAR_TO_IDX


class CharEncoder(keras.Model):
    def __init__(self):
        super(CharEncoder, self).__init__()

        self.embedding = keras.layers.Embedding(len(CHAR_TO_IDX), 8)
        self.gru_one = keras.layers.Bidirectional(
            keras.layers.GRU(256, return_sequences=True, return_state=True)
        )
        self.gru_two = keras.layers.Bidirectional(keras.layers.GRU(256))
        self.projection = keras.layers.Dense(512)

    def call(self, x):
        return self.projection(self.gru_two(self.gru_one(self.embedding(x))))


class CharDecoder(keras.Model):
    def __init__(self, num_classes: int):
        super(CharDecoder, self).__init__()

        self.gru_one = keras.layers.Bidirectional(
            keras.layers.GRU(256, return_sequences=True, return_state=True)
        )
        self.gru_two = keras.layers.Bidirectional(keras.layers.GRU(256))
        self.clkassifier = tf.keras.TimeDistributed(keras.layers.Dense(num_classes))

    def call(self, x):
        return self.classifier(self.gru_two(self.gru_one(x)))
