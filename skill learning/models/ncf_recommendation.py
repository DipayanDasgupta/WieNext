import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Dense, Concatenate
from tensorflow.keras.models import Model

class NCFRecommender:
    def __init__(self, num_users, num_items, embedding_size=50):
        self.num_users = num_users
        self.num_items = num_items
        self.embedding_size = embedding_size
        self.model = self._build_model()

    def _build_model(self):
        user_input = Input(shape=[1], name='user')
        item_input = Input(shape=[1], name='item')
        user_embedding = Embedding(input_dim=self.num_users, output_dim=self.embedding_size)(user_input)
        item_embedding = Embedding(input_dim=self.num_items, output_dim=self.embedding_size)(item_input)
        user_vec = Flatten()(user_embedding)
        item_vec = Flatten()(item_embedding)
        dot = Dot(axes=1)([user_vec, item_vec])
        x = Dense(128, activation='relu')(dot)
        x = Dense(64, activation='relu')(x)
        output = Dense(1, activation='sigmoid')(x)
        model = Model(inputs=[user_input, item_input], outputs=output)
        model.compile(optimizer='adam', loss='binary_crossentropy')
        return model

    def train_model(self, user_data, item_data, labels, epochs=5, batch_size=64):
        self.model.fit([user_data, item_data], labels, epochs=epochs, batch_size=batch_size)
