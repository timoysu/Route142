from django.db import models


class Point(models.Model):
    """
        Model for points in the map. Points like intersections, land marks, 
        etc.
    """
    custom_id = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    typ = models.CharField(max_length=255, blank=True)
    is_landmark = models.BooleanField(default=False)

    def __unicode__(self):
        if self.is_landmark:
            return self.name
        else:
            return str(self.custom_id)


class Connection(models.Model):
    vertex1 = models.ForeignKey(Point, related_name='connections')
    vertex2 = models.ForeignKey(Point, related_name='connections')
    distance = models.FloatField()

    def __unicode__(self):
        res = ""
        if self.vertex1.is_landmark:
            res += self.vertex1.name + " - "
        else:
            res += str(self.vertex1.pk) + " - "

        if self.vertex2.is_landmark:
            res += self.vertex2.name
        else:
            res += str(self.vertex2.pk)


class Traffic(models.Model):
    traffic_start_time = models.TimeField(blank=True, null=True)
    traffic_end_time = models.TimeField(blank=True, null=True)
    conection = models.ForeignKey(Connection, related_name='traffic')
