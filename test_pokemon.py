from pokemon import compare_stats

def test_compare_stats_player_loses():
    stat_player = 10
    stat_opponent = 30
    stat = "id"
    
    results = compare_stats(stat, stat_player, stat_opponent)

    expect_results = (f"Better luck next time :( You lost based on {stat}. "
    f"Your {stat} is {stat_player} "
    f"and your opponents {stat} is {stat_opponent}")
   
    assert results == expect_results

def test_compare_stats_player_wins():
    stat_player = 40
    stat_opponent = 30
    stat = "id"
    
    results = compare_stats(stat, stat_player, stat_opponent)

    expect_results = (f"Congratulations! You won based on {stat}. "
                f"Your {stat} is {stat_player} "
                f"and your opponents {stat} is {stat_opponent}")
   
    assert results == expect_results


def test_compare_stats_player_draw():
    stat_player = 40
    stat_opponent = 40
    stat = "id"
    
    results = compare_stats(stat, stat_player, stat_opponent)

    expect_results = (f"It's a draw! You drew based on {stat}. "
                f"Your {stat} is the same as your opponent's")
   
    assert results == expect_results
