import sys
import collections

alpha_dict = dict()
alpha_dict['a'] = -1
alpha_dict['b'] = -1
alpha_dict['c'] = -1
alpha_dict['d'] = -1
alpha_dict['e'] = -1
alpha_dict['f'] = -1
alpha_dict['g'] = -1
alpha_dict['h'] = -1
alpha_dict['i'] = -1
alpha_dict['j'] = -1
alpha_dict['k'] = -1
alpha_dict['l'] = -1
alpha_dict['m'] = -1
alpha_dict['n'] = -1
alpha_dict['o'] = -1
alpha_dict['p'] = -1
alpha_dict['q'] = -1
alpha_dict['r'] = -1
alpha_dict['s'] = -1
alpha_dict['t'] = -1
alpha_dict['u'] = -1
alpha_dict['v'] = -1
alpha_dict['w'] = -1
alpha_dict['x'] = -1
alpha_dict['y'] = -1
alpha_dict['z'] = -1



word = sys.stdin.readline().rstrip()

for ind in range(len(word)):

    if alpha_dict[word[ind]] ==  -1:
        alpha_dict[word[ind]] = ind

od = collections.OrderedDict(sorted(alpha_dict.items()))

a = list(map(str, list(od.values())))

sys.stdout.write(" ".join(a) + '\n')
