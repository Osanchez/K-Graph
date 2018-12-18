
Evaluation Results
==========

FB15k


| Model      |     MeanRank(Raw) |   MeanRank(Filter)   |	Hit@10(Raw)	| Hit@10(Filter)|
| :-------- | --------:| :------: | :------: |:------: |
| TransE(Paper, n=50)   | 210|	82  |	41.9|  61.3 |
| TransE(Paper, n=100)  |    205 |  63 |  47.9 | 70.2 |


| Model      |     MeanRank(Raw) |   MeanRank(Filter)   |	Hit@10(Raw)	| Hit@10(Filter)|
| :-------- | --------:| :------: | :------: |:------: |
| Uniform Sampling | | | | |
| TransE Left (Our, n=50)   | 242.2  |	85.8  |	39.4 |  58.8 |
| TransE Right (Our, n=50)   | 162.4 |	63.9  |	46.3 |  63.1 |
| TransE Average (Our, n=50)   | 202.3  |	74.8  |	42.8 |  61.0 |
| TransE Left (Our, n=100)   | 309.9  |	192.4  |	45.9 |  64.1 |
| TransE Right (Our, n=100)   | 173.9 |	99.6 | 0.54 |  71.0 |
| TransE Average (Our, n=100)   | 241.9 |	146.0 |	49.9|  67.6 |


| Model      |     MeanRank(Raw) |   MeanRank(Filter)   |	Hit@10(Raw)	| Hit@10(Filter)|
| :-------- | --------:| :------: | :------: |:------: |
| Bern Sampling | | | | |
| TransE Left (Our, n=50)   | 322.0  |	207.7  |	42.1 |  57.0 |
| TransE Right (Our, n=50)   | 191.8 | 119.8 | 50.0 |  64.3 |
| TransE Average (Our, n=50)   | 256.9 | 163.8 |	46.0 |  60.7 |
| TransE Left (Our, n=100)   | 256.7 |	81.0 |	44.1 |  67.8 |
| TransE Right (Our, n=100)   | 163.4 | 53.7  |	51.6 |  72.9 |
| TransE Average (Our, n=100)   | 210.1 |	67.4  |	47.9 |  70.3 |




Citations
==========

Yankai Lin, Zhiyuan Liu, Maosong Sun, Yang Liu, Xuan Zhu. Learning Entity and Relation Embeddings for Knowledge Graph Completion. The 29th AAAI Conference on Artificial Intelligence (AAAI'15).[[pdf]](http://nlp.csai.tsinghua.edu.cn/~lzy/publications/aaai2015_transr.pdf)
