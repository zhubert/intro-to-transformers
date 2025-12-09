import os
import subprocess
import glob

for notebook in sorted(glob.glob("[a-z]**/*.ipynb", recursive=True)):
    print(f"Notebook is {notebook}")
    subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook, '--inplace'])
