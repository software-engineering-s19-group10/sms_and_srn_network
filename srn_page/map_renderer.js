// load when document is ready
$(document).ready(function() {
    // URL to get the geolocation parameters of the user. We don't
    // have to deal with permissions this way.
    let geoipURL = "https://api.ipgeolocation.io/ipgeo?apiKey=a359c0ed992141c78a4d359c5f77aab6";

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
        

            function heatmapRenderer(resData) {
                // we make a successful JSONP call!
                console.log(resData);
                // parse to JSON
                var resArr = jQuery.parseJSON(resData);
    
                // create the circles for the heatmap
                function getCircle(magnitude) {
                    return {
                      path: google.maps.SymbolPath.CIRCLE,
                      fillColor: 'red',
                      fillOpacity: .2,
                      scale: Math.pow(4, magnitude) / 2,
                      strokeColor: 'white',
                      strokeWeight: .8
                    };
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
                    mapTypeId: google.maps.MapTypeId.HYBRID
                });
    
                var heatmap = new google.maps.visualization.HeatmapLayer({
                    data: heatmapDat
                });
    
                heatmap.setMap(map);
            }

            // the api url to get data
            // replace this with whatever we use
            let dataURL = "https://b8cf0f93.ngrok.io/lock_owners/api/srn/";
            
            $.ajax({
                url: dataURL,
                dataType: 'text',
                type: 'GET',
                contentType: "application/json; charset=utf-8",
                success: function(data){
                    console.log(data);
                    heatmapRenderer(data);
                },
                error: function(jqXHR, textStatus, ex) {
                    //console.log(textStatus + "," + ex + "," + jqXHR.responseText);
                }
              }); 
        }
    );
})
