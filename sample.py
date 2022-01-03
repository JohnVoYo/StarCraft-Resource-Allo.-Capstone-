
import pandas as pd
import sc2reader
from collections import defaultdict

categories = ['second', 'minerals_current', 'vespene_current',
              'minerals_used_in_progress_army',
              'minerals_used_in_progress_economy',
              'minerals_used_in_progress_technology',
              'vespene_used_in_progress_army',
              'vespene_used_in_progress_economy',
              'vespene_used_in_progress_technology',
              'minerals_killed_army', 'minerals_killed_economy',
              'minerals_killed_technology',
              'vespene_killed_army', 'vespene_killed_economy',
              'vespene_killed_technology',
              'workers_active_count']


def get_stats(filename, df):
    #this gets the replay with depth of looking
    replay = sc2reader.load_replay(filename, load_level=3)

    #collects the number of different types of events from the replay
    event_names = set([event.name for event in replay.events])

    #makes & adds numbers to each of the events
    events_of_type = {name: [] for name in event_names}

    #adds all of the event info for each of the event types into their own event section
    for event in replay.events:
        events_of_type[event.name].append(event)

    #like to stat collector in tracker.py _> playerstatsevent acutally variabel
    player_stats = events_of_type["PlayerStatsEvent"]


    player1_stats = defaultdict(list, {k:[] for k in categories})
    player2_stats = defaultdict(list, {k:[] for k in categories})

    for stat in player_stats:
        if stat.pid == 1:
            for a in stat.__dict__.keys():
                if a in categories:
                    player1_stats[a].append(getattr(stat, a))
        if stat.pid == 2:
            for a in stat.__dict__.keys():
                if a in categories:
                    player2_stats[a].append(getattr(stat, a))

    players = [player1_stats, player2_stats]

    for player in players:
        df = df.append(player, ignore_index=True)
    return df


sc_df = pd.DataFrame(columns=categories)
sc_df = get_stats('GameVideo.SC2Replay', sc_df)

sc_df.to_csv('sc_stats.tsv', sep='\t', index=False)
