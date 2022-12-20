from abc import ABCMeta, abstractmethod
from typing import List

from numpy import true_divide


class Metrics(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, RR: List[int], REL: List[int]):
        pass

class Precission(Metrics):
    def __call__(self, RR: List[int], REL: List[int]):
        rr = set(RR)
        rel = set(REL)

        rrel = rr.intersection(rel)

        return true_divide(len(rrel), len(rr))

class Recall(Metrics):
    def __call__(self, RR: List[int], REL: List[int]):
        rr = set(RR)
        rel = set(REL)

        rrel = rr.intersection(rel)
        nrel = rel.difference(rrel)

        return true_divide(len(rrel), (len(rrel) + len(nrel)))

class FMean(Metrics):
    def __call__(self, RR: List[int], REL: List[int], beta: float = 0.7):
        P = Precission()(RR, REL)
        R = Recall()(RR, REL)

        return true_divide((1 + beta**2),(P**-1 + (beta**2 / R)))


class F1Mean(Metrics):
    def __call__(self, RR: List[int], REL: List[int]):
        P = Precission()(RR, REL)
        R = Recall()(RR, REL)

        return true_divide(2 , (P**-1 + R**-1))

