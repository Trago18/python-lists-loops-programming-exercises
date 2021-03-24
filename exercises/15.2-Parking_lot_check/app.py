parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

def get_parking_lot(x):
    state = {'total_slots': 0, 'available_slots': 0, 'occupied_slots': 0}
    for d1 in x:
        for d2 in d1:
            if (d2 == 1):
                state['total_slots'] += 1
                state['occupied_slots'] += 1
            elif (d2 == 2):
                state['total_slots'] += 1
                state['available_slots'] += 1
    print(state)

get_parking_lot(parking_state)
