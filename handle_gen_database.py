import robocupRAI as RoboCupDBA

# -------------- Gen Station
# data = {
#     'name': None,
#     'code': None,
#     'type': None,
#     'rotation': 0,
#     'zone': None,
#     'present': False,
#     'pose': []
# }

# dataList = []
# nameList = ['M-CS1', 'M-CS2', 'M-RS1', 'M-RS2', 'M-BS', 'M-DS', 'M-SS']
# codeList = [200, 202, 210, 212, 220, 230, 240]
# for code, name in zip(codeList, nameList):
#     _type = name[2:4]
#     data['name'] = name + '-I'
#     data['type'] = _type
#     data['code'] = code + 2
#     dataList.append(data.copy())
    
#     data['name'] = name + '-O'
#     data['code'] = code + 1
#     dataList.append(data.copy())

# print(RoboCupDBA.blindInsertList(host= '10.26.11.13', data = dataList, collection= 'station_info'))


# -------------- Gen Station (Modify dataset)
# data = {
#     'rotation': 270,
#     'zone': 'M_Z12',
#     'present': True,
#     'pose': [-0.5, 1.5, 245]
# }
# print(RoboCupDBA.directUpdate(collection= 'station_info', key={'code': 202}, data= data))
# print(RoboCupDBA.directUpdate(collection= 'station_info', key={'code': 201}, data= data))

# data = {
#     'rotation': 90,
#     'zone': 'M_Z54',
#     'present': True,
#     'pose': [-4.5, 3.5, 92]
# }
# print(RoboCupDBA.directUpdate(collection= 'station_info', key={'code': 222}, data= data))

# data = {
#     'rotation': 0,
#     'zone': 'M_Z33',
#     'present': True,
#     'pose': [-2.5, 2.5, 3]
# }
# print(RoboCupDBA.directUpdate(collection= 'station_info', key={'code': 212}, data= data))
# print(RoboCupDBA.directUpdate(collection= 'station_info', key={'code': 211}, data= data))

# data = {
#     'rotation': 180,
#     'zone': 'M_Z11',
#     'present': True,
#     'pose': [-5, 2.5, 3]
# }
# print(RoboCupDBA.directUpdate(collection= 'station_info', key={'code': 242}, data= data))
# print(RoboCupDBA.directUpdate(collection= 'station_info', key={'code': 241}, data= data))



# if (RoboCupDBA.query(collection= 'station_info', data={'code': 201, 'present': True})):
#     print('is present')
# else:
#     print('is missing')








# -------------- Gen Map
# dataList = []
# for i in range(1, 6):
#     for j in range(1, 6):
#         data = {}
#         data['observing_zone'] = f'M_Z{i}{j}'
#         data['env'] = {str(i * 45) : False for i in range(0, 8)}
        
#         dataList.append(data.copy())

# print(RoboCupDBA.blindInsertList(host= '192.168.0.134', data = dataList, collection= 'explore_map'))
# RoboCupDBA.resetMap()





# RoboCupDBA.blindInsert(data= {"kl": [3, 4, 5, 6]}, collection='explore_map')
# RoboCupDBA.updateMap(zone=11, oren=270, stat=True)
    