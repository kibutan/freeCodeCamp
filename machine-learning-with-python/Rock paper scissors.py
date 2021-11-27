# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
n = 0
play_order = [{
  "RRR":0,"RRP":0,"RRS":0,
  "RPR":0,"RPP":0,"RPS":0,
  "RSR":0,"RSP":0,"RSS":0,

  "PRR":0,"PRP":0,"PRS":0,
  "PPR":0,"PPP":0,"PPS":0,
  "PSR":0,"PSP":0,"PSS":0,

  "SRR":0,"SRP":0,"SRS":0,
  "SPR":0,"SPP":0,"SPS":0,
  "SSR":0,"SSP":0,"SSS":0,
}]
# print(n)
play_order2 = [{
  "RR":0,"RP":0,"RS":0,
  "PR":0,"PP":0,"PS":0,
  "SR":0,"SP":0,"SS":0,
}]

player_hist = [{
  "RR":0,"RP":0,"RS":0,
  "PR":0,"PP":0,"PS":0,
  "SR":0,"SP":0,"SS":0,
}]
opponent_history=["P"]
player_history = ["S"]
last_two_player = ["S"]

def player(prev_play):
    global n
    global opponent_history
    global play_order
    global play_order2
    global player_hist
    global player_history
    global last_two_player
    if n%1000 == 0:print(n)
    
    # print("l2",opponent_history[-2:])
    
    if n%1000 == 0:
      play_order = [{
        "RRR":0,"RRP":0,"RRS":0,
        "RPR":0,"RPP":0,"RPS":0,
        "RSR":0,"RSP":0,"RSS":0,

        "PRR":0,"PRP":0,"PRS":0,
        "PPR":0,"PPP":0,"PPS":0,
        "PSR":0,"PSP":0,"PSS":0,

        "SRR":0,"SRP":0,"SRS":0,
        "SPR":0,"SPP":0,"SPS":0,
        "SSR":0,"SSP":0,"SSS":0,
      }]
      # print(n)
      play_order2 = [{
        "RR":0,"RP":0,"RS":0,
        "PR":0,"PP":0,"PS":0,
        "SR":0,"SP":0,"SS":0,
      }]
      player_hist = [{
        "SS":0,"SP":0,"SR":0,
        "PS":0,"PP":0,"PR":0,
        "RS":0,"RP":0,"RR":0,
      }]
    n += 1
    if not prev_play:
      prev_play = "S"
      opponent_history = ["S"]
      player_history = ["R"]
      last_two_player = ["R"]
    if len(opponent_history) >= 1000:
      opponent_history.clear()
      opponent_history = ["S"]
      player_history = ["R"]
      last_two_player = ["R"]
    
    opponent_history.append(prev_play)
    # if len(opponent_history) > 100:
    #   opponent_history = opponent_history[-100:]
    last_two = "".join(opponent_history[-2:])
    last_three = "".join(opponent_history[-3:])

    if len(last_two) == 2:
      play_order2[0][last_two] += 1
    if len(last_three) == 3:
      play_order[0][last_three] += 1

    potential_plays = [
        prev_play + "R", prev_play + "P", prev_play + "S",
        last_two + "R", last_two + "P", last_two + "S"        
    ]

    potential_plays_player = [
        last_two_player[-1] + "R", last_two_player[-1] + "P", last_two_player[-1] + "S"
    ]

    if n >=4000 and n < 5000:
      sub_order = {k:player_hist[0][k] for k in potential_plays_player if k in player_hist[0]}
      sub_order2 = {l:play_order2[0][l] for l in potential_plays_player if l in play_order2[0]}
      prediction = max(sub_order,key=sub_order.get)[-1:]
      ideal_response = {"R":"S","P":"R","S":"P"}

    else:
      sub_order = {k:play_order[0][k] for k in potential_plays if k in play_order[0]}
      sub_order2 = {l:play_order2[0][l] for l in potential_plays if l in play_order2[0]}
      most_used = 0
      for key,value in sub_order.items():
        # print(key,value)
        most_used = max(most_used,value)
      prediction = max(sub_order,key=sub_order.get)[-1:] if most_used > 3 else max(sub_order2,key=sub_order2.get)[-1:]
      ideal_response = {"R":"P","P":"S","S":"R"}
    guess = ideal_response[prediction]

    # print(play_order)
    # print("l2",last_two,"l3",last_three,"prev_play",prev_play)
    # print("OPP_PRED",prediction,"VS ",guess,"ME")
    # print("sub_order",sub_order)
    # print("sub_order2",sub_order2)
    # print("pot_plays",potential_plays)
    # print(prev_play,guess)
    player_history.append(guess)

    last_two_player = "".join(player_history[-2:])
    if len(last_two_player) == 2:
      player_hist[0][last_two_player] += 1


    return guess
