# Do not modify the seasons array
seasons = [0, 32, 21, 18, 17, 24, 31, 8, 24, 21, 26]

def season_episode(global_episode, seasons):
    for season_num, season_episodes in enumerate(seasons):
        if global_episode > season_episodes:
            global_episode -= season_episodes
        else:
            break
    return (season_num, global_episode)

# Season 182 should return (9, 7)
print(season_episode(182, seasons))
