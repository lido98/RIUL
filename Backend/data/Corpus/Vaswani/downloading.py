import ir_datasets
import pathlib
dataset = ir_datasets.load("vaswani")

path = str(pathlib.Path(__file__).parent.absolute()) + '\\files\\vaswani.txt'
file = open(path, 'w')
for doc in dataset.docs_iter():
    doc # namedtuple<doc_id, text>
    file.write('.I ' + doc[0] + '\n')
    file.write('.W\n' + doc[1])
file.close()