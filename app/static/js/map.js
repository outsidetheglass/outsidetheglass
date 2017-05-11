// Load Map
var map = L.map( 'map', {
    center: [20.0, 5.0],
    minZoom: 2,
    zoom: 2
});
L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: ['a','b','c']
}).addTo( map );

// Geolocate
var lc = L.control.locate({
    position: 'topleft',
    locateOptions: {maxZoom: 30},
    strings: {
        title: "Find Location"
    }
}).addTo(map);

// Map Markers
var markers = [
   {'name': 'SOUTHSHORE AT DETROIT LAKE', 'lat': '44.7054', 'lng': '-122.176186111'}, {'name': 'Craters of the Moon Group Campground', 'lat': '43.4727777778', 'lng': '-113.566944444'}, {'name': 'LEFT TAILRACE CAMPGROUND', 'lat': '44.0408333333', 'lng': '-99.4394444444'}, {'name': 'WHITE ROCK MOUNTAIN RECREATION AREA', 'lat': '35.6898611111', 'lng': '-93.9563611111'}, {'name': 'Colonial Creek South Campground', 'lat': '48.6895805556', 'lng': '-121.096061111'}, {'name': 'Alsea Falls Recreation Site', 'lat': '44.3205611111', 'lng': '-123.487822222'}, {'name': 'Toto Creek Campground', 'lat': '34.3949444444', 'lng': '-83.9867777778'}, {'name': 'MEDICINE LAKE RECREATION AREA', 'lat': '41.5858444444', 'lng': '-121.585569444'}, {'name': 'Moonflower Canyon Group Site', 'lat': '38.5538805556', 'lng': '-109.586925'}, {'name': 'Rim Campground', 'lat': '34.3054166667', 'lng': '-110.909166667'}, {'name': 'HALFWAY FLAT CAMPGROUND', 'lat': '46.980475', 'lng': '-121.095822222'}, {'name': 'SINKHOLE CAMPGROUND', 'lat': '34.3048055556', 'lng': '-110.885416667'}, {'name': 'MOOSALAMOO CAMPGROUND', 'lat': '43.919', 'lng': '-73.0271'}, {'name': 'MOGOLLON CAMPGROUND', 'lat': '34.3214305556', 'lng': '-110.956666667'}, {'name': 'Big Meadow Campground', 'lat': '36.7181388889', 'lng': '-118.833055556'}, {'name': 'WHITE SPAR CAMPGROUND', 'lat': '34.5061694444', 'lng': '-112.477680556'}
 ]
for ( var i=0; i < markers.length; i++ )
{
   L.marker( [markers[i].lat, markers[i].lng] )
      .bindPopup( '<a href="' + markers[i].url + '" target="_blank">' + markers[i].name + '</a>' )
      .addTo( map );
}
