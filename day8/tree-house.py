with open('day8/forest.txt') as f:
    forest = [[int(y) for y in x.strip()] for x in f.readlines()]
    visible = 4*len(forest) - 4
    # part1
    # for y in range(1, len(forest)-1):
    #     for x in range(1, len(forest[y])-1):
    #         tmp1 = forest[y][:x]
    #         tmp2 = forest[y][x+1:]
    #         # print(f"{tmp1} {forest[y][x]} {tmp2}")
    #         tmp3 = [z[x] for z in forest[:y]]
    #         tmp4 = [z[x] for z in forest[y+1:]]
    #         # print(f"{tmp3} {forest[y][x]} {tmp4}")
    #         if max(tmp1) < forest[y][x] or max(tmp2) < forest[y][x] or max(tmp3) < forest[y][x] or max(tmp4) < forest[y][x]:
    #             visible += 1
    # part2
    scores = []
    for y in range(len(forest)):
        for x in range(len(forest[y])):
            tmp = []
            tmp1 = forest[y][:x]
            tmp2 = forest[y][x+1:]
            tmp3 = [z[x] for z in forest[:y]]
            tmp4 = [z[x] for z in forest[y+1:]]
            tmp.append(reversed(tmp1)) 
            tmp.append(tmp2) 
            tmp.append(reversed(tmp3))
            tmp.append(tmp4)
            tree_score = 1
            for trees in tmp:
                side_score = 0
                for tree in trees:
                    side_score += 1
                    if tree >= forest[y][x]:
                        break
                tree_score *= side_score
            scores.append(tree_score)
    # print(visible)
    #print(scores)
    print(max(scores))