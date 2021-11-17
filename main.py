

import sc2reader

#this gets the replay with depth of looking
replay = sc2reader.load_replay('king_sejong_station_le.sc2replay', load_level=3)

print('-------')

#collects the number of different types of events from the replay
event_names = set([event.name for event in replay.events])

#makes & adds numbers to each of the events
events_of_type = {name: [] for name in event_names}

#adds all of the event info for each of the event types into their own event section
for event in replay.events:
    events_of_type[event.name].append(event)

#like to stat collector in tracker.py _> playerstatsevent acutally variabel
player_stats = events_of_type["PlayerStatsEvent"]

space = " "


categories = ["mineral amt","vespene amt","mineral used army","mineral used economy","mineral used technology","vespene used army","vespene used economy","vespene used technology","minerals killed army","minerals killed economy","minerals killed technology","vespene killed army","vespene killed economy","vespene killed technology","workers active","time"]
playernum = [1,2]

playeri = []
playerii = []

count = 1
for category in categories:  # each category
    for player in playernum:  # each player
        playeri = []
        playerii = []
        for stat in player_stats:  # goes through each of the numbers
            if stat.pid == 1:  # if its player # then gets printed out
                if count == 1:
                    playeri.append(stat.minerals_current) #bank
                if count == 2:
                    playeri.append(stat.vespene_current)
                if count == 3:
                    playeri.append(stat.minerals_used_in_progress_army) #circulation
                if count == 4:
                    playeri.append(stat.minerals_used_in_progress_economy)
                if count == 5:
                    playeri.append(stat.minerals_used_in_progress_technology)
                if count == 6:
                    playeri.append(stat.vespene_used_in_progress_army)
                if count == 7:
                    playeri.append(stat.vespene_used_in_progress_economy)
                if count == 8:
                    playeri.append(stat.vespene_used_in_progress_technology)

                if count == 9:
                    playeri.append(stat.minerals_killed_army) #army use
                if count == 10:
                    playeri.append(stat.minerals_killed_economy)
                if count == 11:
                    playeri.append(stat.minerals_killed_technology)
                if count == 12:
                    playeri.append(stat.vespene_killed_army)
                if count == 13:
                    playeri.append(stat.vespene_killed_economy)
                if count == 14:
                    playeri.append(stat.vespene_killed_technology)

                if count == 15:
                    playeri.append(stat.workers_active_count) #production

                if count == 16:
                    playeri.append((stat.frame) / 16)  # time


            if stat.pid == 2:
                if count == 1:
                    playerii.append(stat.minerals_current)
                if count == 2:
                    playerii.append(stat.vespene_current)
                if count == 3:
                    playerii.append(stat.minerals_used_in_progress_army)
                if count == 4:
                    playerii.append(stat.minerals_used_in_progress_economy)
                if count == 5:
                    playerii.append(stat.minerals_used_in_progress_technology)
                if count == 6:
                    playerii.append(stat.vespene_used_in_progress_army)
                if count == 7:
                    playerii.append(stat.vespene_used_in_progress_economy)
                if count == 8:
                    playerii.append(stat.vespene_used_in_progress_technology)

                if count == 9:
                    playerii.append(stat.minerals_killed_army)
                if count == 10:
                    playerii.append(stat.minerals_killed_economy)
                if count == 11:
                    playerii.append(stat.minerals_killed_technology)
                if count == 12:
                    playerii.append(stat.vespene_killed_army)
                if count == 13:
                    playerii.append(stat.vespene_killed_economy)
                if count == 14:
                    playerii.append(stat.vespene_killed_technology)

                if count == 15:
                    playerii.append(stat.workers_active_count)

                if count == 16:
                    playerii.append((stat.frame) / 16) #time

    count += 1
    #playeri.append(100000)
    #playerii.append(100000)
    print(categories[count-2])
    print(playeri)
    print(playerii)
    print("")


