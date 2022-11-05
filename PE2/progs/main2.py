from sys import path

path.append('./PE2/modules/packages/extra.zip')

# import extra.iota
# print(extra.iota.funI())

from extra.iota import funI
# import extra.good.best.sigma
from extra.good.best.tau import funT
import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(funI())
# print(extra.good.best.sigma.funS())
print(funT())
print(sig.funS())
print(alp.funA())

for p in path:
    print(p)