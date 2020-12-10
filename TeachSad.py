import os
import Teach

# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \
CONFIG = 'lookback_rnn'


Teach.createNoteSequences("SAD_DATA", "tmpSAD/notesequences.tfrecord")

Teach.createSequenceExamples(CONFIG, 'tmpSAD/notesequences.tfrecord', 'tmpSAD/melody_rnn/sequence_examples',0.1)

Teach.train(CONFIG,
              'tmpSad/melody_rnn/logdir/run1',
              'tmpSAD/melody_rnn/sequence_examples/training_melodies.tfrecord',
              64,[128,128],10000)

# Teach.evaluate('CONFIG,
#                'tmpSad/melody_rnn/logdir/run1',
#                '/tmp/melody_rnn/generatedEVALUATELOOK',
#                10, 128,
#                64, [128, 128], 60)

# Teach.createBundle(CONFIG,'tmpSad/melody_rnn/logdir/run1',64,[128, 128],'tmpSAD/attention_rnn.mag')
