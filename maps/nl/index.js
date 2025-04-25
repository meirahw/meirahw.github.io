<div id="my-custom-map" style="width: 600px; height: 400px"></div>

var map = L.map(‘my-custom-map’).setView([51.505, -0.09], 13);

L.tileLayer(‘https://tile.openstreetmap.org/{z}/{x}/{y}.png’, { attribution: ‘© OpenStreetMap contributors’ }).addTo(map);

L.marker([51.5, -0.09]).addTo(map) .bindPopup(‘A pretty CSS popup.
Easily customizable.’) .openPopup();

