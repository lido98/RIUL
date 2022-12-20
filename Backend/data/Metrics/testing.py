from re import search
import environment


def test_queries(queries):
    ranks = []
    for querie in queries:
        ranks.append (environment.Environment.search_engine(querie))
        print("Consult: " + querie + "\n")
        for value in ranks[len(ranks)-1]:
            print (str(value.id)+": " + str(ranks[len(ranks)-1][value]))
    return ranks

def test_cases(coll):
    queries = []
    if (coll == "VASWANI"):
        queries.append("measurement of dielectric constant of liquids by the use of microwave techniques")
        queries.append("mathematical analysis and design details of waveguide fed microwave radiations")
    if (coll == "CRAN"):
        pass
    test_queries(queries)
    pass    