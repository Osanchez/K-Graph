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

#Notes
While a majority of the code is left close to the original. some hard coded values were changed and debugging statements were added
to make training and testing easier and get some feedback as to whether or not its doing what its supposed to. That is why this code was included in the submission. I do not take credit 
for any of the code written
