import tensorflow as tf
import random
from PIL import Image
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_lfw_people
import pandas as pd
tf.disable_eager_execution()

tf.set_random_seed(777)
'''
people = fetch_lfw_people(min_faces_per_person = 20, resize = 0.7)
people_ = np.array(people.images)
print(people_.shape)

X_one_hot = pd.get_dummies(people.target_names)
print(people.target_names)
print(X_one_hot)
'''
#print(X_one_hot)

img_name = ['elsa', 'taeri', 'kimtaehi', 'suji', 'somin']

img_real = Image.open("/home/kernel/Desktop/eunji.JPG")
img_real_ = img_real.resize((128, 128))
x_test = np.array(img_real_)
print(x_test.shape)
x_test = x_test.reshape([1, 128, 128, 3])

data_set_y = [[1, 0, 0, 0, 0],[1, 0, 0, 0 ,0],[1, 0, 0, 0, 0],[1, 0, 0, 0, 0],[1, 0, 0, 0, 0],
[0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0],
[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0],
[0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0],
[0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]]

size = (128, 128)

data_set_x = []
for name in img_name:
    for cnt in range(1, 6):
        name_ = name + str(cnt) + '.jpg'
        img = Image.open("/home/kernel/Desktop/practice/" + name + '/' + name_)
        img_ = img.resize(size)
        #plt.imshow(img_)
        data_set_x.append(np.array(img_))

keep_prob = tf.placeholder(tf.float32)
X = tf.placeholder(tf.float32, [None, 128, 128, 3])
Y = tf.placeholder(tf.float32, [None, 5])
learning_rate = 0.01

W1 = tf.Variable(tf.random_normal([2, 2, 3, 32], stddev = 0.01))
L1 = tf.nn.conv2d(X, W1, strides = [1, 1, 1, 1], padding = 'SAME')
L1 = tf.nn.max_pool(L1, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')
L1 = tf.nn.dropout(L1, keep_prob = keep_prob)

W2 = tf.Variable(tf.random_normal([2, 2, 32, 64], stddev = 0.01))
L2 = tf.nn.conv2d(L1, W2, strides = [1, 1, 1, 1], padding = 'SAME')
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')
L2 = tf.nn.dropout(L2, keep_prob = keep_prob)

W3 = tf.Variable(tf.random_normal([2, 2, 64, 128], stddev=0.01))
L3 = tf.nn.conv2d(L2, W3, strides=[1, 1, 1, 1], padding='SAME')
L3 = tf.nn.relu(L3)
L3 = tf.nn.max_pool(L3, ksize=[1, 2, 2, 1], strides=[
                    1, 2, 2, 1], padding='SAME')
L3 = tf.nn.dropout(L3, keep_prob=keep_prob)
L3_flat = tf.reshape(L3, [-1, 128 * 16 * 16])

W4 = tf.get_variable("W4", shape = [128 * 16 * 16, 625], initializer = tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([625]))
L4 = tf.nn.relu(tf.matmul(L3_flat, W4) + b4)
L4 = tf.nn.dropout(L4, keep_prob = keep_prob)

W5 = tf.get_variable("W5", shape = [625, 5], initializer = tf.contrib.layers.xavier_initializer())
b5 = tf.Variable(tf.random_normal([5]))
logits = tf.matmul(L4, W5) + b5

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = Y))
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)

print('Learing start')

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(100):
    avg_cost = 0
    feed_dict = {X : data_set_x, Y : data_set_y, keep_prob : 0.7}
    c, _ = sess.run([cost, optimizer], feed_dict = feed_dict)
    print(c)


print("Prediction : ", sess.run(tf.argmax(logits, 1), feed_dict = {X : x_test, keep_prob : 1}))
print(tf.argmax(logits, 1))
real_img = Image.open("/home/kernel/Desktop/practice/" + img_name[2] + "/" + img_name[2] + "1" + ".jpg")
plt.imshow(real_img)
plt.show()



