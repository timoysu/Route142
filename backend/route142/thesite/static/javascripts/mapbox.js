// LIMIT MAP BOUNDARIES TO CEBU ISLAND ONLY
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
    this._features = [];
}

Mapbox.prototype.center = function(coordinates) {
    this._map.setView(coordinates, 17);
};

Mapbox.prototype.fit = function(bounds) {
    this._map.fitBounds(bounds);
};

Mapbox.prototype.clear = function() {
    for (var i in this._features) {
        this._map.removeLayer(this._features[i]);
    }
    this._features = [];
};

Mapbox.prototype.road = function(data) {
    var road = L.polyline([data.start, data.end], { color: traffic_indicator_color(data.traffic) });
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
        this._features = [];
        for (var i = 0; i < data.length; i++) {
            var object = data[i];
            if (object.type === 'road') {
                var road = this.road(object);
                this._features.push(road);
            } else {
                var marker = this.establishment(object);
                this._features.push(marker);
            }
        }
        var features = L.featureGroup(this._features);
        this.fit(features.getBounds());
    } else if (data instanceof Object) {
        var marker = this.establishment(data);
        this._features.push(marker);
        this.center(data.coordinates);
    }
};

// SOME UTILITY FUNCTIONS
function traffic_indicator_color(traffic) {
    if (traffic === 'light') {
        return 'green';
    } else if (traffic === 'moderate') {
        return 'orange';
    } else if (traffic === 'heavy') {
        return 'red';
    }
    return 'white';
}