import cnn_mnist as cnn
import cv2
import tensorflow as tf
import numpy as np


# Input the path of target picture
img_path = input('Input the path of your image please:\n')
img = cv2.imread(img_path, 0)
size = (28, 28)
shrink = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
ret, th1 = cv2.threshold(shrink, 150, 255, cv2.THRESH_BINARY)

# Utilize the line of code below to save your image converted if necessary
# cv2.imwrite('num_test.png', th1, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])


# Convert the image to binary-picture
temp_img = np.array(th1 == 0)
float_img = temp_img.astype(np.float32)

# ATTENTION : 0 for black pixel and 1 for white pixel
# float_img = (1 - float_img)
input_data = float_img


# To load pre-trained model and predict
model_path = input('Input the path of your model directory please:\n')
my_mnist_classifier = tf.estimator.Estimator(
    model_fn= cnn.cnn_model_fn, model_dir= model_path)

predict_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": input_data},
      num_epochs=1,
      shuffle=False)

predictions = list(my_mnist_classifier.predict(input_fn=predict_input_fn))

predicted_classes = [p["classes"] for p in predictions]
predicted_probs = [p["probabilities"] for p in predictions]

print(
    "New Samples, Class Predictions:    {}\n".format(predicted_classes),
    "All probabilities： {}\n".format(predicted_probs)
    )




