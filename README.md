# MNIST_DIY
Official Tensorflow MNIST program, with implementations of Opencv to recognize hand-written digits from your own pictures.


# Installation
The model performs with:
* Tensorflow 1.1.0
* Opencv3<br>
Both of which you can easily get access to on Anaconda.


# Predicting
A pre-trained model is provided in  `My_mnist_model`  for you to implement recognition directly. The model take as input arbitrary size of your own pictures(e.g. /tmp/number_1.jpg) with hand-written digits, utilizing high-level Tensorflow module `tf.estimator` to restore check points before. APIs of Opencv3 are used to pre-process the image. 
To start prediction, run the following comman:<br>
```
python Read_Predict_mnist.py
```
Input the path of images or the model directory according to prompts, and you should see results similar to this:<br>
```
New Samples, Class Predictions:    [3]
```
Also, there are some test images available in `test_images`.


# Datasets
You don’t have to prepare dataset yourself. The following line of code in the script `cnn_mnist.py` will load all the labled datasets you need in the process of training, evaluating and predicting:
```
mnist = tf.contrib.learn.datasets.load_dataset(“mnist”)
```

# Training
As mentioned above, a pre-trained model is provided for you.<br>
If you would like to develop your own model, just delete all files in the model directory. Codes for setting parameters can be found at the start of the script `cnn_mnist.py`:<br>
```
# Set parameters for training
train_learning_rate = 0.1
train_batch_size = 50
train_steps = 1500
train_logging_every_n_iter = 100
```
Then run the command below to start training:
```
python cnn_mnist.py
```
Here, you can set `train_logging_every_n_iter` to change the iterations between two training logs.  
It’s easy for you to train a well-performed model which achieves roughly 98% accuracy within 5000 train_steps, setting train_batch_size to be 50 and train_learning_rate to be 0.01. You may also need to fine-tune the model, since it may slightly suffer from the problem of overfitting by far.


# Evaluation
To evaluate your model, run the following command:
```
python Eval_mnist.py
```
Then you will experience a similar procedure of inputting the path of model directory. You should finally see a result of evaluation like this:
```
{'accuracy': 0.97970003, 'loss': 0.060401399, 'global_step': 5000}
```
