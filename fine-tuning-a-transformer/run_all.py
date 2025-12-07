import os
import subprocess
import glob

for notebook in sorted(glob.glob('*.ipynb')):
    subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook, '--inplace'])
