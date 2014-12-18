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

    var self = this;
    this.on = this._map.on;
    this._features = [];

    this._map.on('moveend', function(e) {
        var bounds = self._map.getBounds();
        var northwest = bounds.getNorthWest();
        var southeast = bounds.getSouthEast();
        bounds = { northwest: [northwest.lat, northwest.lng], southeast: [southeast.lat, southeast.lng] };
        request(endpoints.bounded_query, bounds, function(data) {
            self.display(data);
        });
    });
}

Mapbox.prototype.center = function(coordinates) {
    this._map.setView(coordinates, 16);
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

Mapbox.prototype.establishment = function(data, force_popup, clear) {
    force_popup = params(force_popup, false);
    clear = params(clear, true);
    var marker = L.marker(data.coordinates);
    var popup = L.popup({ 
        closeButton: false, 
        closeOnClick: false, 
        offset: [0, -25], 
        className: 'mapbox-popup'
    }).setContent(data.name);
    if (force_popup) {
        popup.setLatLng(marker.getLatLng());
        this._map.addLayer(popup);
    } else {
        marker.bindPopup(popup).openPopup();
    }
    this._map.addLayer(marker);
    return marker;
};

Mapbox.prototype.display = function(data, force_popup, clear, fit) {
    force_popup = params(force_popup, false);
    if (params(clear, true)) {
        this.clear();
    }
    if (data instanceof Array) {
        this._features = [];
        for (var i = 0; i < data.length; i++) {
            var object = data[i];
            if (object.type === 'road') {
                var road = this.road(object);
                this._features.push(road);
            } else {
                var marker = this.establishment(object, force_popup);
                this._features.push(marker);
            }
        }
        var features = L.featureGroup(this._features);
        if (params(fit, false)) {
            this.fit(features.getBounds());
        }
    } else if (data instanceof Object) {
        var marker = this.establishment(data, force_popup);
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

function request(url, data, callback) {
    $.ajax({
        url: url,
        method: 'GET',
        data: { data: JSON.stringify(data) },
        success: function(data) {
            data = JSON.parse(data);
            if (typeof callback === 'function') {
                callback(data);
            }
        }
    });
}

function params(param, normal) {
    return param === undefined ? normal : param;
}