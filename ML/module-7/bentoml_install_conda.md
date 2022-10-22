

Installation of bento inside a conda env

conda install -c anaconda pip
which -a pip
  /usr/local/bin/pip
  /opt/anaconda3/envs/zoomcamp-ml/bin/pip

/opt/anaconda3/envs/zoomcamp-ml/bin/pip install bentoml

bentoml --version 

NB - just trying to keep things tidy and in an enviroment. running pip install bentoml will install bentoml sitewide or machine wide. I can't afford package comflict on my dev pc