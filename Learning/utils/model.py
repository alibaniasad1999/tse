import tensorflow as tf

def lstm_model(x, y):
    model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(32, return_sequences=True, input_shape=(x.shape[1], x.shape[2])),  # First LSTM layer
        tf.keras.layers.LSTM(32, return_sequences=True),  # Second LSTM layer
        tf.keras.layers.LSTM(16),  # Third LSTM layer
        tf.keras.layers.RepeatVector(3),  # Repeat the output to 3 days (output 3 time steps)
        tf.keras.layers.LSTM(16, return_sequences=True),  # LSTM to process the output sequence
        tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(4))  # Output layer (3 days * 4 kinds)
    ])
    
    return model
