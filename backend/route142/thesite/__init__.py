# from models import Point, Connection
# import json
# import math

# f = open("ways.json")
# ways = json.loads(f.read())
# f.close()
# ctr = 0
# towrite = []
# for w in ways:
#     ctr += 1
#     print ctr
#     points = w['points']
#     index = 1
#     while index < len(points):
#         s = Point.objects.filter(custom_id=points[index - 1])
#         if s:
#             s = s[0]
#         d = Point.objects.filter(custom_id=points[index])
#         if d:
#             d = d[0]
#         if d and s:
#             distance = math.sqrt((s.lat - d.lat)*(s.lat - d.lat) +
#                                 (s.lon - d.lon)*(s.lon - d.lon))
#             oneway = w['oneway'] != 'no'
#             towrite.append(Connection(vertex1=s, vertex2=d, distance=distance,
#                            oneway=oneway))
#         index += 1

#     if len(towrite) > 300:
#         Connection.objects.bulk_create(towrite)
#         towrite = []
# Connection.objects.bulk_create(towrite)
