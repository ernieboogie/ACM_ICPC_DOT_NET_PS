import sys

rank_list = []
def rank_bulk(new_bulk):
    if len(rank_list) == 0:
        new_rank = []
        new_rank.append(1)
        new_rank.append(new_bulk)
        rank_list.append(new_rank)
    else:
        for rank in rank_list:
            if True:
                pass
            else:
                new_rank = []
                new_rank.append(1)
                new_rank.append(new_bulk)
                rank_list.append(new_rank)


people = int(sys.stdin.readline().rstrip())

bulk_list = []
for ind in range(people):
    new_bulk = []
    bulk = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    new_bulk.append(bulk[0])
    new_bulk.append(bulk[1])
    new_bulk.append(ind)

for bulk in bulk_list:
    rank_bulk(rank_list, bulk)
