from re import search
import environment

def test_queries(queries):
    ranks = []
    for querie in queries:
        ranks.append (environment.Environment.search_engine(querie))
    return ranks

def test_cases():
    pass    