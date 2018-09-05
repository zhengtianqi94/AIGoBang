import tensorflow as tf
from SGFfile import SGFflie
import os

sgf = SGFflie()

class myCNN():
    def __init__(self):
        '''初始化神经网络'''
        self.sess = tf.InteractiveSession()

        # paras
        self.W_conv1 = self.weight_varible([5, 5, 1, 32])
        self.b_conv1 = self.bias_variable([32])
        # conv layer-1
        self.x = tf.placeholder(tf.float32, [None, 225])
        self.y = tf.placeholder(tf.float32, [None, 225])
        self.x_image = tf.reshape(self.x, [-1, 15, 15, 1])

        self.h_conv1 = tf.nn.relu(self.conv2d(self.x_image, self.W_conv1) + self.b_conv1)
        self.h_pool1 = self.max_pool_2x2(self.h_conv1)

        # conv layer-2
        self.W_conv2 = self.weight_varible([5, 5, 32, 64])
        self.b_conv2 = self.bias_variable([64])

        self.h_conv2 = tf.nn.relu(self.conv2d(self.h_pool1, self.W_conv2) + self.b_conv2)
        self.h_pool2 = self.max_pool_2x2(self.h_conv2)

        # full connection
        self.W_fc1 = self.weight_varible([4 * 4 * 64, 1024])
        self.b_fc1 = self.bias_variable([1024])

        self.h_pool2_flat = tf.reshape(self.h_pool2, [-1, 4 * 4 * 64])
        self.h_fc1 = tf.nn.relu(tf.matmul(self.h_pool2_flat, self.W_fc1) + self.b_fc1)

        # dropout
        self.keep_prob = tf.placeholder(tf.float32)
        self.h_fc1_drop = tf.nn.dropout(self.h_fc1, self.keep_prob)

        # output layer: softmax
        self.W_fc2 = self.weight_varible([1024, 225])
        self.b_fc2 = self.bias_variable([225])

        self.y_conv = tf.nn.softmax(tf.matmul(self.h_fc1_drop, self.W_fc2) + self.b_fc2)

        # model training
        self.cross_entropy = -tf.reduce_sum(self.y * tf.log(self.y_conv))
        self.train_step = tf.train.AdamOptimizer(1e-3).minimize(self.cross_entropy)

        self.correct_prediction = tf.equal(tf.argmax(self.y_conv, 1), tf.argmax(self.y, 1))
        self.accuracy = tf.reduce_mean(tf.cast(self.correct_prediction, tf.float32))
        self.saver = tf.train.Saver()

        init = tf.global_variables_initializer()  # 不存在就初始化变量
        self.sess.run(init)

    def weight_varible(self, shape):
        '''权重变量'''
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)

    def bias_variable(self, shape):
        '''偏置变量'''
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial)

    def conv2d(self, x, W):
        '''卷积核'''
        return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

    def max_pool_2x2(self, x):
        '''池化核'''
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    def restore_save(self, method=1):
        '''保存和读取模型'''
        if method == 1:
            self.saver.restore(self.sess, 'save\model.ckpt')
            #print("已读取数据")
        elif method == 0:
            saver = tf.train.Saver(write_version=tf.train.SaverDef.V2)
            saver.save(self.sess, 'save\model.ckpt')
            #print('已保存')

    def predition(self, qiju):
        '''预测函数'''
        _qiju = self.createdataformqiju(qiju)
        pre = self.sess.run(tf.argmax(self.y_conv, 1), feed_dict={self.x: _qiju, self.keep_prob: 1.0})

        point = [0, 0]
        l = pre[0]
        for i in range(15):
            if ((i + 1) * 15) > l:
                point[0] = int(i*30 + 25)
                point[1] = int((l - i * 15) * 30 + 25)
                break
        return point

    def train(self, qiju):
        '''训练函数'''
        sgf = SGFflie()
        _x, _y = sgf.createTraindataFromqipu(qiju)
        for i in range(10):
            self.sess.run(self.train_step, feed_dict={
                self.x: _x,
                self.y: _y
            })
        self.restore_save(method=0)

    def train1(self, x, y):
        '''另一个训练函数'''
        for i in range(100):
            self.sess.run(self.train_step, feed_dict={
                self.x: x,
                self.y: y,
                self.keep_prob: 0.5
            })
        print('训练好了一次')
        #self.restore_save(method=0)

    def createdataformqiju(self, qiju):
        '''生成数据'''
        data = []
        tmp = []
        for row in qiju:
            for point in row:
                if point == -1:
                    tmp.append(0.0)
                elif point == 0:
                    tmp.append(2.0)
                elif point == 1:
                    tmp.append(1.0)
        data.append(tmp)
        return data

#这一段用来训练神经网络，要训练是把注释去掉并运行这个文件就可以了
'''_cnn = myCNN()
path = sgf.allFileFromDir('C:\PythonCodes\AIGoBang\sgf\\')
_x, _y = sgf.createTraindataFromqipu(path[0])

step = 0
_path = path[:2000]
for filepath in path:
    x, y = sgf.createTraindataFromqipu(filepath)
    for i in range(1):
        _cnn.sess.run(_cnn.train_step, feed_dict={_cnn.x: x, _cnn.y: y, _cnn.keep_prob: 0.5})
    print(step)
    step += 1
_cnn.restore_save(method=0)
_cnn.restore_save(method=1)
print(_cnn.sess.run(tf.argmax(_cnn.y_conv, 1), feed_dict={_cnn.x: _x[0:10], _cnn.keep_prob: 1.0}))
#'''
