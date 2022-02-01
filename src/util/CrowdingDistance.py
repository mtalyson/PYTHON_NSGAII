import numpy as np

from src.individuo.Individuo import Individuo
from src.problema.ProblemaExemplo import ProblemaExemplo


class CrowdingDistance:

    def avaliar(self, t: [Individuo]):
        s = len(t)

        for ind in t:
            ind.crowdingdistance = 0

        primeiroindividuo = t.__getitem__(0)
        quantidadeobjetivos = len(primeiroindividuo.getObjetivos())

        for m in range(quantidadeobjetivos):
            self.sort(t, m)
            t.__getitem__(0).crowdingdistance = float('inf')
            t.__getitem__(s - 1).crowdingdistance = float('inf')

            for i in range(s - 1):
                aux = (t.__getitem__(i + 1).getObjetivos()[m] - t.__getitem__(i - 1).getObjetivos()[m]) / \
                      (t.__getitem__(s - 1).getObjetivos()[m] - t.__getitem__(0).getObjetivos()[m])

                t.__getitem__(i).crowdingdistance += aux

    def sort(self, t: [Individuo], n):

        for i in range(len(t)-1):
            for j in range(i + 1, len(t)):
                """if t.__getitem__(i).getObjetivos()[n] > t.__getitem__(j).getObjetivos()[n]:
                    aux = t.__getitem__(i)
                    t.__setitem__(i, t.__getitem__(j))
                    t.__setitem__(j, aux)"""


def main():
    fronteiraindividuos = [
        Individuo(ProblemaExemplo(), np.array([6], float)), Individuo(ProblemaExemplo(), np.array([7], float)),
        Individuo(ProblemaExemplo(), np.array([8], float)), Individuo(ProblemaExemplo(), np.array([9], float))
    ]

    cd = CrowdingDistance()
    cd.avaliar(fronteiraindividuos)


if __name__ == "__main__":
    main()