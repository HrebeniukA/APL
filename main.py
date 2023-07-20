import pandas as pd
from data_analysis import (
    team_performance, every_season, sum_of_all_seasons_for_a_team,
    sum_of_all_seasons, relegated_teams, sum_of_eliminated_teams,
    top_points, top_points_of_all_seasons, table_of_winners, average_number_of_goals_per_season,
    average_number_of_goals_per_season_per_team, most_productive_team_per_season,
    average_goals_per_match_by_year, get_best_scoring_team_by_season
)
from data_visualization import (
    plot_average_goals_per_season, plot_points_per_season,
    plot_positions_per_season
)
from data_processing import clean_notes


APL = pd.read_csv('premier-league-tables.csv')
APL = clean_notes(APL)


def main():
    APL = pd.read_csv('premier-league-tables.csv')
    APL = clean_notes(APL)

    ars = team_performance(APL, 'arsenal')
    chl = team_performance(APL, 'Chelsea')
    print(chl)
    print(ars)
    ars1 = every_season(APL, 'arsenal')
    print(ars1)
    ars2 = sum_of_all_seasons_for_a_team(APL, 'arsenal')
    print(ars2)
    print(sum_of_all_seasons(APL))
    print(relegated_teams(APL, 'Champions League'))
    print(sum_of_eliminated_teams(APL, 'Champions League'))
    print(top_points(APL))
    print(top_points_of_all_seasons(APL))
    print(table_of_winners(APL))
    print(average_number_of_goals_per_season(APL))
    print(average_number_of_goals_per_season_per_team(APL, 'arsenal'))
    print(most_productive_team_per_season(APL))
    print(average_goals_per_match_by_year(APL, 'arsenal'))
    print(get_best_scoring_team_by_season(APL))

    teams = ['Arsenal', 'Chelsea', 'liverpool']
    plot_points_per_season(APL, teams)
    plot_positions_per_season(APL, teams)
    plot_average_goals_per_season(APL, teams)


if __name__ == '__main__':
    main()