
Evaluation Results
==========

FB15k


| Model      |     MeanRank(Raw) |   MeanRank(Filter)   |	Hit@10(Raw)	| Hit@10(Filter)|
| :-------- | --------:| :------: | :------: |:------: |
| TransE(paper)|    243 | 125 |  34.9 | 47.1|
| TransH(paper)        |   212 |  87 |  45.7 | 64.4|

| Uniform Sampling | | | | |
| TransE Left (Our, n=50)   | 242.236  |	85.7559   |	0.393797|  0.588411|
| TransE Right (Our, n=50)   | 162.437|	63.9272  |	0.462833 |  0.630902 |
| TransE Average (Our, n=50)   | 202.3365  |	74.84155  |	0.428315|  0.6096565 |
| TransE Left (Our, n=100)   | 309.935  |	192.351  |	0.458567 |  0.641093 |
| TransE Right (Our, n=100)   | 173.929|	99.5757  |	0.539554 |  0.710738 |
| TransE Average (Our, n=100)   | 241.932	  |	145.96335 |	0.4990605|  0.6759155 |
| Bern Sampling | | | | |
| TransE Left (Our, n=50)   | 321.973  |	207.666  |	0.421086|  0.570415|
| TransE Right (Our, n=50)   | 191.841 | 119.836  |	0.499738|  0.643463 |
| TransE Average (Our, n=50)   | 256.907 | 163.751 |	0.460412|  0.606939 |
| TransE Left (Our, n=100)   | 256.739 |	81.0104   |	0.441232 |  0.677778 |
| TransE Right (Our, n=100)   | 163.39 | 53.7418  |	0.516209 |  0.729173 |
| TransE Average (Our, n=100)   | 210.0645 |	67.3761  |	0.4787205 |  0.7034755 |




Citations
==========

Yankai Lin, Zhiyuan Liu, Maosong Sun, Yang Liu, Xuan Zhu. Learning Entity and Relation Embeddings for Knowledge Graph Completion. The 29th AAAI Conference on Artificial Intelligence (AAAI'15).[[pdf]](http://nlp.csai.tsinghua.edu.cn/~lzy/publications/aaai2015_transr.pdf)
