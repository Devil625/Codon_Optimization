A training tool for the codon optimization model for E. coli.
======
In order to accurately capture the codon distribution of the host genes, the codon optimization problem can be converted into that of sequence annotation in deep learning.Sequence labeling models are quite popular in many NLP tasks, such as Named Entity Recognition (NER), part-of-speech (POS) tagging and word segmentation.NCRF++ is a PyTorch based framework with flexiable choices of input features and output structures. 


This is a training tool for the codon optimization model for E. coli,which is based on [NCRF++](https://github.com/jiesutd/NCRFpp/tree/PyTorch0.3)


Welcome to start this repository!


Requirement:
======
	Python: 3  
	PyTorch: 1.4 (Currently, 0.3 and earlier are not supported)


1.Usage：
=========
The program can run in two status; ***training*** and ***decoding***.

In ***training*** status:
`python main.py --config demo.train.config`

In ***decoding*** status:
`python main.py --config demo.decode.config`

The configuration file controls the network structure, I/O, training setting and hyperparameters. 

***Detail configurations and explanations are listed [here](readme/Configuration.md).***


2.Data format:
=========
You can refer to the data format in [CPA](sample_data/CPA.txt). 

In [sample_data](sample_data),we have prepared [train_set](sample_data/cboxtrain.txt), [dev_set](sample_data/cboxdev.txt) and [test_set](sample_data/cboxtest.txt) for training model.

You can also use our [trained_model](sample_data/lstmcrf.0.model) to decode.


3.Data transform:
=========
[codonToBox](codonToBox.py) and [boxToCodon](codonToBox.py) is provided to transform data. 

4.Codonbox website
====
http://www.codonbox.com:7000

