from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    # 장르별 총 재생 횟수와 곡 리스트를 저장할 딕셔너리 초기화
    genre_dict = defaultdict(int)
    genre_song_list = defaultdict(list)
    
    # 장르별 총 재생 횟수와 곡 리스트 업데이트
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_dict[genre] += play
        genre_song_list[genre].append((play, idx))
    
    for genre in sorted(genre_dict, key=lambda x: -genre_dict[x]):
        best_songs = sorted(genre_song_list[genre], key=lambda x: (-x[0], x[1]))[:2]
        answer.extend([song[1] for song in best_songs])
    
    return answer