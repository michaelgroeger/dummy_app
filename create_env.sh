conda create -n dummy python=3.10.8 ipython
source ~/miniconda3/etc/profile.d/conda.sh
conda activate dummy
conda install conda-build
conda develop ./scripts
pip install -r requirements.txt
