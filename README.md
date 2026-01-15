# IPEO_Species_Distribution_Modeling
This repository contains different jupyter notebooks training and evaluating species distribution models using single-modal as well as multimodal approaches. The data include climate data, Landsat timeseries and satellite imagery and need to be added to the cloned repositories' top-level folder as a folder called 'data'.

Trained models have been uploaded using git LFS and are available as '.pth' files.

The inference.ipynb notebook in the Inference folder imports the model weights for the multimodal model trained during the second approach to multimodal modeling and generates predictions for the sample with index 100 in the test set. The environment requirements to run this file are specified in the environment.yml file. The current working directory needs to be adapted to match the repositories' top-level folder.

The files included in the folder Models should be run in Google Colab and the base_path variable/the current working directory needs to be adapted to match the repositories' top-level folder.

