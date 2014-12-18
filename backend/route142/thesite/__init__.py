# from models import Point, Connection
# import json
# import math

# f = open("ways-cleaned.json")
# ways = json.loads(f.read())
# f.close()
# ctr = 0
# towrite = []
# print len(ways)
# for w in ways:
#     ctr += 1
#     print ctr
#     points = w['points']
#     index = 1
#     while index < len(points):
#         try:
#             s = Point.objects.get(custom_id=points[index - 1])
#             d = Point.objects.get(custom_id=points[index])
#             if d and s:
#                 distance = math.sqrt((s.lat - d.lat)*(s.lat - d.lat) +
#                                     (s.lon - d.lon)*(s.lon - d.lon))
#                 oneway = w['oneway'] != 'no'
#                 towrite.append(Connection(vertex1=s, vertex2=d, distance=distance,
#                                oneway=oneway))
#         except:
#             pass
#         index += 1

#     if len(towrite) > 300:
#         Connection.objects.bulk_create(towrite)
#         towrite = []
# Connection.objects.bulk_create(towrite)

# f = open("points-cleaned.json")

# marks = json.loads(f.read())
# f.close()
# print len(marks)

# to_write = []
# for m in marks:
#     to_write.append(Point(custom_id=m['id'], lat=m['lat'], lon=m['long'], is_landmark=False))
#     if len(to_write) > 500:
#         Point.objects.bulk_create(to_write)
#         to_write = []
# Point.objects.bulk_create(to_write)

# f = open("landmarks-cleaned.json")

# marks = json.loads(f.read())
# f.close()

# to_write = []
# for m in marks:
#     to_write.append(Point(custom_id=m['id'], lat=m['lat'], lon=m['long'], is_landmark=True, name=m['name'], typ=m['type']))
#     if len(to_write) > 500:
#         Point.objects.bulk_create(to_write)
#         to_write = []
# Point.objects.bulk_create(to_write)






