import os
import shutil

cache_dir = os.path.expanduser('~/.cache/torch/hub/checkpoints')
shutil.rmtree(cache_dir)
