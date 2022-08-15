import boto3
import tensorflow as tf

from io import BytesIO
import numpy as np
from PIL import Image

LABELS = {
    0: 'With Fire',
    1: 'Without Fire'
}

s3 = boto3.client('s3')


def lambda_handler(event, context):

    print(event)

    model = tf.keras.models.load_model('./model.h5')

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    file_byte_string = s3.get_object(Bucket=bucket_name, Key=key)['Body'].read()
    image = Image.open(BytesIO(file_byte_string))
    image = image.resize((224, 224))

    image = image - np.mean(image)

    input_tensor = np.array(np.expand_dims(image, axis=0), dtype=np.float32)

    output_data = model.predict(x=input_tensor, verbose=0)

    output_data = np.squeeze(output_data)
    result = np.argmax(output_data, axis=-1)

    print(f'Prediction: {LABELS[result]}')
    print(f'Probability: {output_data[result]:.2f}')
