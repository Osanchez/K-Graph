# Files needed
To run training models you will need each file from the data set in directory ../data/

Datasets are required in the folder data/ in the following format, containing six files:

+ train.txt: training file, format (e1, e2, rel).

+ valid.txt: validation file, same format as train.txt

+ test.txt: test file, same format as train.txt.

+ entity2id.txt: all entities and corresponding ids, one per line.

+ relation2id.txt: all relations and corresponding ids, one per line.

# How to run
Take each modified .cpp based on the size you want to train on. n=50, n=100. run makefile to compile
to train each model run the command train_transE -method (1 or 0; bern unif)
