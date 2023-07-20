import matplotlib.pyplot as plt
from data_analysis import average_number_of_goals_per_season_per_team


def plot_average_goals_per_season(APL, teams):
    """
        Визуализирует среднее количество голов для каждой команды по сезонам.

        Parameters:
            APL (DataFrame): Данные о позициях команд в сезонах АПЛ.
            teams (list): Список команд для отображения на графике.

        Returns:
            None
    """

    for team in teams:
        average_goals = average_number_of_goals_per_season_per_team(APL, team)

        if isinstance(average_goals, str):
            print(average_goals)
            continue

        plt.plot(average_goals.index, average_goals.values, marker='o', label=team)

    plt.xlabel('Season')
    plt.ylabel('Average Goals')
    plt.title('Average Goals per Season')
    plt.legend()
    plt.show()


def plot_points_per_season(APL, teams):
    """
        Строит график количества очков команды по сезонам.

        Parameters:
            APL (DataFrame): Данные о позициях команд в сезонах АПЛ.
            teams (list): Список названий команд.

        Returns:
            None
    """

    for team in teams:
        team_data = APL[APL['Team'] == team.title()]

        if team_data.empty:
            print(f"Team '{team}' not found in the dataset.")
            continue

        years = team_data['Season_End_Year']
        points = team_data['Pts']

        min_position = min(points)
        max_position = max(points)

        plt.plot(years, points, marker='o', label=team)

    plt.xlabel('Год')
    plt.ylabel('Количество очков')
    plt.title('Количество очков команд по сезонам')
    plt.legend()
    plt.ylim(min_position - 1, max_position + 1)
    plt.show()


def plot_positions_per_season(APL, teams):
    """
    Строит график занятого места команды(й) по сезонам.

    Parameters:
        APL (DataFrame): Данные о позициях команд в сезонах АПЛ.
        teams (str or list): Название команды или список названий команд.

    Returns:
        None
    """
    if isinstance(teams, str):
        teams = [teams]

    all_positions = []

    for team in teams:
        team_data = APL[APL['Team'] == team.title()]

        if team_data.empty:
            print(f"Team '{team}' not found in the dataset.")
            continue

        years = team_data['Season_End_Year']
        positions = team_data['Rk']

        all_positions.extend(positions.values)

        plt.plot(years, positions, marker='o', label=team)

    plt.gca().invert_yaxis()

    min_position = min(all_positions)
    max_position = max(all_positions)
    plt.ylim(max_position + 1, min_position - 1)

    plt.xlabel('Год')
    plt.ylabel('Занятое место')
    plt.title('Занятое место команд по сезонам')
    plt.legend()
    plt.show()