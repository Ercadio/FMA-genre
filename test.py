'''Test program for tf'''

import tensorflow as tf

A = tf.placeholder(tf.float32, None, 'A')
B = tf.placeholder(tf.float32, None, 'B')

C = A + B

with tf.Session() as s:
    ans = s.run(C, {A: 1.0, B: 2.0})
    print(ans)
print("DONE")