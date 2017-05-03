function drawMap(definitionPrefix) {
    console.log('leaflet_init.js: definitionPrefix = ' + definitionPrefix);

    var $newItem = $('#' + definitionPrefix + '-map');

    if ($newItem.length === 0) {
        console.error('leaflet_init.js: Unable to find $newItem !');
        return null;
    }

    var initMap = function(definitionPrefix) {
        console.log('leaflet_init.js:initMap() definitionPrefix = ' + definitionPrefix);

        // window.addEventListener('map:init', function(e){
        //     var detail = e.detail;
        //     L.marker([50.5, 3.0]).addTo(detail.map);
        // });
    };
    return initMap;
}
