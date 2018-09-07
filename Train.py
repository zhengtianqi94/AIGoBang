import tensorflow as tf
from SGFFileProcess import SGFflie
from CNN import myCNN

sgf = SGFflie()
_cnn = myCNN()
path = sgf.allFileFromDir('sgf\\')
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