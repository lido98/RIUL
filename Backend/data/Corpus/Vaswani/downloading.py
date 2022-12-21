import ir_datasets
import pathlib
dataset = ir_datasets.load("vaswani")

# path = str(pathlib.Path(__file__).parent.absolute()) + '\\files\\vaswani.txt'
# file = open(path, 'w')
# for doc in dataset.docs_iter():
#     doc # namedtuple<doc_id, text>
#     file.write('.I ' + doc[0] + '\n')
#     file.write('.W\n' + doc[1])
# file.close()

# path = str(pathlib.Path(__file__).parent.absolute()) + '\\files\\queries.txt'
# file = open(path, 'w')
# for query in dataset.queries_iter():
#     # namedtuple<doc_id, text>
#     file.write(query[0] + '\n')
#     file.write(query[1].lower())
# file.close()

path = str(pathlib.Path(__file__).parent.absolute()) + '\\files\\qrels.txt'
file = open(path, 'w')
for qrel in dataset.qrels_iter():
    file.write(str(qrel[0]) + ' ' + str(qrel[1]) + ' ' + str(qrel[2]) + '\n')    
file.close()