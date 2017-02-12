import tensorflow as tf

# Basic model parameters.
tf.app.flags.DEFINE_string('game', 'uniform',
                           """Bandit experiment type to be run""")
tf.app.flags.DEFINE_string('GPU', "0",
                           """The GPU device to run on""")
tf.app.flags.DEFINE_boolean('resume', False,
                            """Resume training from latest checkpoint""")
tf.app.flags.DEFINE_boolean('train', True,
                            """Whether to train or test""")
tf.app.flags.DEFINE_boolean('show_training', True,
                            """Show windows with workers training""")
tf.app.flags.DEFINE_string('checkpoint_dir', './models/',
                           """Directory where to save model checkpoints.""")
tf.app.flags.DEFINE_string('summaries_dir', './summaries',
                           """Directory where to write event logs""")
tf.app.flags.DEFINE_string('frames_dir', './frames',
                           """Directory where to write event gifs""")
tf.app.flags.DEFINE_integer('summary_interval', 5, """Number of episodes of interval between summary saves""")
tf.app.flags.DEFINE_integer('checkpoint_interval', 500, """Number of episodes of interval between checkpoint saves""")
tf.app.flags.DEFINE_integer('frames_interval', 100, """Number of episodes of interval between frames saves""")
tf.app.flags.DEFINE_integer('nb_actions', 2, """Number of actions to take""")
tf.app.flags.DEFINE_integer('nb_concurrent', 4, """Start from epoch""")
tf.app.flags.DEFINE_integer('max_episode_buffer_size', 32, """Start from epoch""")

tf.app.flags.DEFINE_integer('agent_history_length', 4, """Start from epoch""")
tf.app.flags.DEFINE_integer('resized_width', 84, """Start from epoch""")
tf.app.flags.DEFINE_integer('resized_height', 84, """Start from epoch""")
tf.app.flags.DEFINE_float('gamma', 0.99, """Learning rate""")
tf.app.flags.DEFINE_float('lr', 0.00001, """Learning rate""")
