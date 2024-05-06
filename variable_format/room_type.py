def room_info(rooms):
    roomInfo = {}
    roomInfo['Laboratory'] = set(room['_id'] for room in rooms if room['type'] == 'Laboratory')
    roomInfo['Lecture'] = set(room['_id'] for room in rooms if room['type'] == 'Lecture')
    
    return roomInfo