var map = new Mapbox('#map');

var data = [
    { 
        type: 'road', 
        start: [10.322983539725495, 123.89861583709715], 
        end: [10.319985856906541, 123.89928102493286],

    },
    { 
        type: 'road', 
        start: [10.319985856906541, 123.89928102493286], 
        end: [10.318592557986818, 123.89994621276854] 
    },
    { 
        type: 'road', 
        start: [10.318592557986818, 123.89994621276854], 
        end: [10.317473692267244, 123.89447450637819] 
    },
    { 
        type: 'road', 
        start: [10.317473692267244, 123.89447450637819], 
        end: [10.316270379412684, 123.89093399047852] 
    },
    { 
        type: 'road', 
        start: [10.316270379412684, 123.89093399047852], 
        end: [10.309894855619483, 123.89312267303467] 
    },
    { 
        type: 'school', 
        coordinates: [10.322983539725495, 123.89861583709715], 
        name: 'University of the Philippines Cebu', 
        description: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.' 
    }
];

setTimeout(function() {
    map.display(data);
}, 3000);