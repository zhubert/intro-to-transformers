import argparse
import subprocess
import glob

parser = argparse.ArgumentParser(description="Run Jupyter notebooks")
parser.add_argument("directory", nargs="?", default=None, help="Directory of notebooks to run (e.g., 'building-a-transformer')")
args = parser.parse_args()

if args.directory:
    pattern = f"{args.directory}/*.ipynb"
else:
    pattern = "[a-z]**/*.ipynb"

for notebook in sorted(glob.glob(pattern, recursive=True)):
    print(f"Running {notebook}")
    subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook, '--inplace'])
