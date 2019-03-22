// load when document is ready
$(document).ready(function() {
    // URL to get the geolocation parameters of the user. We don't
    // have to deal with permissions this way.
    let geoipURL = "http://api.ipstack.com/check?access_key=7fdd0c524e76bc908f8b11b56d76e887&format=1";

    // get the corresponding json with geolocation
    $.getJSON(geoipURL, 
        function(result){
            // get the latitude and longitude
            lat = result["latitude"];
            long = result["longitude"];

            // function to initialize the map;
            // center it at the current position of user 
            function initMap(latitude, longitude) {
                map = new google.maps.Map(document.getElementById('map'), {
                    zoom: 2,
                    center: {lat: lat, lng: long},
                    mapTypeId: 'terrain'
                });
        
                // set the circles
                map.data.setStyle(function(feature) {
                  var magnitude = feature.getProperty('mag');
                  return {
                    icon: getCircle(magnitude)
                  };
                });
                return map;
            }
            
            // initialize the map
            var map = initMap(lat, long);
        
            // the api url to get data
            let dataURL = "http://localhost:8000/lock_owners/api/srn/?format=json";

            $.getJSON(dataURL, 
                // function to parse and display
                function(res) {
                    // parse to JSON
                    var resArr = jQuery.parseJSON(res);
        
                    // create the circles for the heatmap
                    function getCircle(magnitude) {
                        return {
                          path: google.maps.SymbolPath.CIRCLE,
                          fillColor: 'red',
                          fillOpacity: .2,
                          scale: Math.pow(2, magnitude) / 2,
                          strokeColor: 'white',
                          strokeWeight: .5
                        };
                    }
        
                    function eqfeed_callback(results) {
                        map.data.addGeoJson(results);
                    }
        
                    var heatmapDat = [];
                    
                    /* Data points defined as an array of LatLng objects */
                    for(let i = 0; i < resArr.length; i++) {
                        heatmapDat.push(new google.maps.LatLng(resArr[i]["latitude"], resArr[i]["longitude"]))
                    }           
        
                    var place = new google.maps.LatLng(lat, long);
        
                    map = new google.maps.Map(document.getElementById('map'), {
                        center: place,
                        zoom: 13,
                        mapTypeId: 'satellite'
                    });
        
                    var heatmap = new google.maps.visualization.HeatmapLayer({
                        data: heatmapDat
                    });
        
                    heatmap.setMap(map);
                }
            )
        }
    );
})
