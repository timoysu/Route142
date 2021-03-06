// limit map boundaries to Cebu island only
var southWest = L.latLng(9.394871245232979, 123.277587890625);
var northEast = L.latLng(11.35348957008566, 124.134521484375);
var mapBounds = L.latLngBounds(southWest, northEast);

function Mapbox(selector) {
    var element = document.querySelector(selector);
    this._map = L.mapbox.map(element, 'arnelleablane.kd50de5h', {
        accessToken: 'pk.eyJ1IjoiYXJuZWxsZWFibGFuZSIsImEiOiI2QW5EWXRjIn0.CH2zHC1Stgj5-vXXfPzmgQ',
        maxBounds: mapBounds
    });

    this.on = this._map.on;
}

Mapbox.prototype.center = function(coordinates) {
    this._map.setView(coordinates, 17);
};

Mapbox.prototype.road = function(data, road) {
    if (road) {
        road.addLatLng(data.start);
        road.addLatLng(data.end);
        return road;
    }
    var road = L.polyline([data.start, data.end]);
    this._map.addLayer(road);
    return road;
};

Mapbox.prototype.establishment = function(data) {
    var marker = L.marker(data.coordinates);
    this._map.addLayer(marker);
    return marker;
};

Mapbox.prototype.display = function(data) {
    if (data instanceof Array) {
        var road = null;
        for (var i = 0; i < data.length; i++) {
            var object = data[i];
            if (object.type === 'road') {
                road = this.road(object, road);
            } else {
                this.establishment(object);
            }
        }
    } else if (data instanceof Object) {
        this.establishment(data);
        this.center(data.coordinates);
    }
};