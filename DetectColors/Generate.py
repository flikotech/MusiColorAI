import os


class Generate:
    def __init__(self,BUNDLE_PATH, CONFIG):
        self.BUNDLE_PATH=BUNDLE_PATH
        self.CONFIG=CONFIG


    def generate(self):
        os.system('python ../magenta/magenta/models/melody_rnn/melody_rnn_generate.py \
        --config=' + self.CONFIG + ' \
        --bundle_file=' + self.BUNDLE_PATH + ' \
        --output_dir=/tmp/melody_rnn/generatedFromColor \
        --num_outputs=10 \
        --num_steps=128 \
        --primer_melody="[60]"')


# <absolute path of .mag file>
# BUNDLE_PATH='models/modelSadLookback_rnn.mag'
# # <one of 'basic_rnn', 'lookback_rnn', or 'attention_rnn', matching the bundle>
# CONFIG='lookback_rnn'

# TODO: change os!
