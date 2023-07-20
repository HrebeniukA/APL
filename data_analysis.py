import pandas as pd


def team_performance(APL, name):
    """
        Возвращает информацию о выступлении конкретной команды.

        Args:
            APL (DataFrame): Данные о сезонах и командах.
            name (str): Название команды.

        Returns:
            str: Строка с информацией о выступлении команды.

        Raises:
            KeyError: Если указанное название команды не найдено в данных.

    """

    if name.title() not in APL['Team'].values:
        raise KeyError("Team not found. Please make sure the team name is entered correctly.")
    team = APL[APL['Team'] == name.title()]
    return team.to_string(index=False)


def every_season(APL, year):
    """
        Возвращает информацию о командах определенного сезона.

        Args:
            APL (DataFrame): Данные о сезонах и командах.
            year (int): Год сезона.

        Returns:
            str: Строка с информацией о командах в указанном сезоне.
                 Возвращает сообщение, если данные не доступны для указанного года.

        Raises:
            KeyError: Если указанное имя столбца не найдено в наборе данных.

        """

    try:
        years_df = APL[APL['Season_End_Year'] == year].sort_values('Rk')
        if years_df.empty:
            return f"No data available for the year {year}."
        else:
            years = years_df.to_string(index=False)
            return years
    except KeyError:
        return f"Invalid data format or column name in the dataset."


def sum_of_all_seasons_for_a_team(APL, name):
    """
        Возвращает накопленную статистику для команды по всем сезонам.

        Args:
            APL (DataFrame): Данные, содержащие информацию о сезонах и командах.
            name (str): Название команды.

        Returns:
            str: Строка с накопленной статистикой для команды.
                 Возвращает сообщение, если команда не найдена в наборе данных.

    """

    team = APL[APL['Team'] == name.title()]
    if team.empty:
        return f"Team '{name}' not found in the dataset."

    sum_mp = team['MP'].sum()
    sum_w = team['W'].sum()
    sum_d = team['D'].sum()
    sum_l = team['L'].sum()
    sum_gf = team['GF'].sum()
    sum_ga = team['GA'].sum()
    sum_gd = team['GD'].sum()
    sum_pts = team['Pts'].sum()

    sum_data = {'Team': [team['Team'].iloc[0]],
                'MP': [sum_mp],
                'W': [sum_w],
                'D': [sum_d],
                'L': [sum_l],
                'GF': [sum_gf],
                'GA': [sum_ga],
                'GD': [sum_gd],
                'Pts': [sum_pts]}
    sum_df = pd.DataFrame(sum_data)
    return sum_df.to_string(index=False)



def sum_of_all_seasons(APL):
    """
        Возвращает накопленную статистику по всем командам за все сезоны.

        Args:
            APL (DataFrame): Данные, содержащие информацию о сезонах и командах.

        Returns:
            DataFrame: Накопленная статистика по всем командам,
                       отсортированная по общему количеству очков (Pts) по убыванию.

    """

    sum_by_team = APL.groupby('Team')[['MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']].sum()
    return sum_by_team.sort_values('Pts', ascending=False)



def relegated_teams(APL, filter_value):
    """
    Возвращает таблицу команд, которые вылетели (или другие значения, указанные в filter_value) из АПЛ.

    Параметры:
    - APL: DataFrame с данными о таблицах АПЛ.
    - filter_value: Значение, используемое для фильтрации данных (по умолчанию 'Relegated').

    Возвращает:
    - DataFrame с отфильтрованными данными по командам, вылетевшим из АПЛ.
    """

    eliminated = APL[APL['Notes'] == filter_value]
    if eliminated.empty:
        return "No eliminated teams found."

    relegated = APL[APL['Notes'] == filter_value].drop('Notes', axis=1).sort_values(['Season_End_Year', 'Rk'])
    return relegated.to_string(index=False)


def sum_of_eliminated_teams(APL, filter_value):
    """
    Возвращает строку с информацией о командах, вылетевших (или других значениях, указанных в filter_value) из АПЛ.

    Параметры:
    - APL: DataFrame с данными о таблицах АПЛ.
    - filter_value: Значение, используемое для фильтрации данных (по умолчанию 'Relegated').

    Возвращает:
    - Строка с информацией о вылетевших командах, их количестве и годах сезонов.
    """
    eliminated = APL[APL['Notes'] == filter_value]
    if eliminated.empty:
        return "No eliminated teams found."

    grouped_teams = eliminated.groupby('Team')['Season_End_Year'].agg(lambda x: f'({", ".join(map(str, x))})')
    team_counts = eliminated['Team'].value_counts()
    result = [f'{team} {count} {grouped_teams[team]}' for team, count in team_counts.items()]
    output = '\n'.join(result)
    return output


def top_points(APL):
    """
        Возвращает таблицу с информацией о командах с наибольшим количеством набранных очков.

        Параметры:
        - APL: DataFrame с данными о таблице АПЛ.

        Возвращает:
        - Таблицу с информацией о командах с наибольшим количеством набранных очков.
    """

    points = APL.drop('Notes', axis=1).sort_values('Pts', ascending=False).head()

    return points.to_string(index=False)


def top_points_of_all_seasons(APL):
    """
    Возвращает таблицу с информацией о командах с наибольшим общим количеством набранных очков за все сезоны.

    Параметры:
    - APL: DataFrame с данными о таблице АПЛ.

    Возвращает:
    - Таблицу с информацией о командах с наибольшим общим количеством набранных очков за все сезоны.
    """

    sum_by_team = APL.groupby('Team')[['MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']].sum()

    top_teams = sum_by_team.sort_values('Pts', ascending=False).head()

    return top_teams


def table_of_winners(APL):
    """
        Возвращает таблицу с годом и названием команд, занимающих первое место в каждом сезоне.

        Parameters:
            APL (DataFrame): Данные о позициях команд в сезонах АПЛ.

        Returns:
            str: Таблица с годом и названием команд, без индексов.
    """
    first_place_teams = APL.loc[APL['Rk'] == 1, ['Season_End_Year', 'Team']]
    return first_place_teams.to_string(index=False)


def average_number_of_goals_per_season(APL):
    """
       Вычисляет среднее количество голов в каждом сезоне АПЛ.

       Parameters:
           APL (DataFrame): Данные о позициях команд в сезонах АПЛ.

       Returns:
           Series: Среднее количество голов в каждом сезоне, округленное до одного знака после запятой.
       """

    goals_per_season = APL.groupby('Season_End_Year').agg({'GF': 'sum', 'GA': 'sum'})
    goals_per_season1= goals_per_season['Total_Goals'] = goals_per_season['GF'] + goals_per_season['GA']
    mp = APL.groupby('Season_End_Year')['MP'].sum()
    a = goals_per_season1 / mp
    return a.round(1)


def average_number_of_goals_per_season_per_team(APL, name):
    """
        Вычисляет среднее количество голов команды в каждом сезоне АПЛ.

        Parameters:
            APL (DataFrame): Данные о позициях команд в сезонах АПЛ.
            name (str): Название команды.

        Returns:
            Series: Среднее количество голов команды в каждом сезоне, округленное до одного знака после запятой.
        """

    team_data = APL[APL['Team'] == name.title()]
    if team_data.empty:
        return 'No such command found.'

    goals_per_season = team_data.groupby('Season_End_Year').agg({'GF': 'sum', 'GA': 'sum', 'MP': 'sum'})
    goals_per_season['Average_Goals'] = (goals_per_season['GF'] + goals_per_season['GA']) / goals_per_season['MP']
    return goals_per_season['Average_Goals'].round(1)


def most_productive_team_per_season(APL):
    """
        Определяет самую продуктивную команду в каждом сезоне АПЛ.

        Parameters:
            APL (DataFrame): Данные о позициях команд в сезонах АПЛ.

        Returns:
            str: Строка, содержащая информацию о самой продуктивной команде в каждом сезоне.
                 Каждая строка имеет формат "Год: Команда (Количество голов)".
                 Строки разделены символом перевода строки.
    """

    seasons = APL['Season_End_Year'].unique()
    result = []

    for season in seasons:
        season_data = APL[APL['Season_End_Year'] == season]
        max_goals = season_data['GF'].max()
        most_productive_teams = season_data.loc[season_data['GF'] == max_goals, ['Team', 'GF']]
        teams_info = ', '.join(
            f"{team} ({goals})" for team, goals in zip(most_productive_teams['Team'], most_productive_teams['GF']))
        result.append(f"{season}: {teams_info}")

    return '\n'.join(result)


def average_goals_per_match_by_year(APL, name):
    """
        Вычисляет среднее количество голов в матче для указанной команды по годам.

        Parameters:
            APL (DataFrame): Данные о позициях команд в сезонах АПЛ.
            name (str): Название команды.

        Returns:
            Series: Серия с средним количеством голов в матче для каждого года.
    """

    try:
        if name.title() not in APL['Team'].unique():
            return f"The team '{name}' is not found in the dataset."

        team_data = APL[APL['Team'] == name.title()]
        goals_per_year = team_data.groupby('Season_End_Year').agg({'GF': 'sum', 'MP': 'sum'})
        goals_per_year['Average_Goals'] = goals_per_year['GF'] / goals_per_year['MP']
        return goals_per_year['Average_Goals'].round(1)
    except KeyError:
        return f"Invalid data format or column name in the dataset."


def get_best_scoring_team_by_season(APL):
    """
        Возвращает информацию о командах с наивысшим средним количеством голов в каждом сезоне.

        Args:
            APL (DataFrame): Данные о сезонах и командах.

        Returns:
            str: Строка с информацией о командах и сезонах в формате "season: team1 (average_goals), team2 (average_goals), ...".

    """

    best_teams = []
    seasons = APL['Season_End_Year'].unique()

    for season in seasons:
        season_data = APL[APL['Season_End_Year'] == season]
        avg_goals = season_data.groupby('Team').agg({'GF': 'sum', 'MP': 'sum'})
        avg_goals['Average_Goals'] = avg_goals['GF'] / avg_goals['MP']
        max_avg_goals = avg_goals['Average_Goals'].max()
        best_teams_season = avg_goals[avg_goals['Average_Goals'] == max_avg_goals]
        best_teams_info = ', '.join(f"{team} ({max_avg_goals.round(1)})" for team in best_teams_season.index)
        best_teams.append(f"{season}: {best_teams_info}")

    return '\n'.join(best_teams)