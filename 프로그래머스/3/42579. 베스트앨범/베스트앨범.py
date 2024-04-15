def solution(genres, plays):
    answer = []
    adding = dict()
    adding_each = dict()
    check = 0

    # 각 장르별 총 재생 횟수와 각 곡의 재생 횟수 저장
    for genre, play in zip(genres, plays):
        if genre in adding:
            adding[genre] += play
            adding_each[genre].append(play)
        else:
            adding[genre] = play
            adding_each[genre] = [play]

    # 장르별 총 재생 횟수를 기준으로 내림차순 정렬
    adding = sorted(adding.items(), key=lambda x: x[1], reverse=True)

    # 각 장르별 곡들의 재생 횟수를 내림차순 정렬
    for genre in adding_each:
        adding_each[genre].sort(reverse=True)

    # 정렬된 정보를 바탕으로 최종 결과 생성
    for genre, total_play in adding:
        selected_songs = adding_each[genre][:2]
        if len(selected_songs) ==2 and selected_songs[0] == selected_songs[1]:
            for A, B in enumerate(plays):
                if B == selected_songs[0]:
                    answer.append(A)
        else:
            for play_count in selected_songs:
            
                index = plays.index(play_count)
                if index in answer:
                    index = plays[check+1:].index(play_count)
                answer.append(index)
            

    return answer