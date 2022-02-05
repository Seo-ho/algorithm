# 프로그래머스 베스트 앨범
#genres = ["classic", "pop", "classic", "classic", "pop"]
#plays = [500, 600, 150, 800, 2500]


def solution1(genres, plays):
    dic = {}
    for g, p in zip(genres, plays):
        if g not in dic.keys():
            dic[g] = p
        else:
            dic[g] += p

    answer_list = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    final_answer = []

    for g, p in answer_list:
        count = {}
        for i in range(len(genres)):
            if genres[i] == g:
                count[i] = plays[i]

        count_list = sorted(count.items(), key = lambda x: x[1], reverse = True)
        final_answer.append(count_list[0][0])
        if len(count_list) >= 2:
            final_answer.append(count_list[1][0])

    print(final_answer)
    return final_answer


def solution2(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}

    for i in zip(genres, plays, range(len(plays))):
        # print(i)
        d[i[0]].append([i[1], i[2
    # lambda 2번 사용해서 많이 재생된 장르 순서
    genresort = sorted(list(d.keys()), key = lambda x: sum(map(lambda y: y[0], d[x])), reverse=True)
    print(genresort)

    for g in genresort:
        # x[0] > [600, 1]에서 600. 노래 횟수 순 reverse를 걸어서 높은게 먼저
        # -x[1] > 고유번호(index). reverse를 걸어서 낮은게 먼저
        temp = [e[1] for e in sorted(d[g], key = lambda x: (x[0], -x[1]), reverse=True)]
        
        answer += temp[:min(len(temp),2)]
    print(answer)
    return answer



if __name__ == '__main__':
   solution1(genres, plays)
   solution2(genres, plays)

