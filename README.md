# MNIST_DIY
Official Tensorflow MNIST program, 
with implementations of Opencv to recognize hand-written digits from your own pictures.


# Installation
The model performs with:
* Tensorflow 1.1.0
* Opencv3.<br>
Both of which you can easily get access to on Anaconda.


# Predicting
A pre-trained model is provided for in `My_mnist_model` you to implement recognition directly.The model take as input arbitrary size of your own pictures with hand-written digits.
To start prediction, run the following comman:<br>
`python Read_Predict_mnist.py`
Then you will see the prompt: `Input the path of your model directory please:`. Input the path as well as file name(e.g. /tmp/num1.jpg), and you should see results similar to these:


