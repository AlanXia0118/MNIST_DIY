import tensorflow as tf
import numpy as np
import cnn_mnist as cnn


model_dir = input('Input the path of your model directory please:\n')
mnist_classifier = tf.estimator.Estimator(
      model_fn=cnn.cnn_model_fn, model_dir=model_dir)

mnist = tf.contrib.learn.datasets.load_dataset("mnist")
eval_data = mnist.test.images
eval_labels = np.asarray(mnist.test.labels, dtype=np.int32)
eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": eval_data},
        y=eval_labels,
        num_epochs=1,
        shuffle=False)
eval_results = mnist_classifier.evaluate(input_fn=eval_input_fn)
print(eval_results)
