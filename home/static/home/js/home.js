window.addEventListener("DOMContentLoaded", () => {
  /*
   * Add animations when cards enter the view
   */
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const intersecting = entry.isIntersecting;
        if (intersecting) {
          entry.target.classList.add("fade-up");
          entry.target.classList.remove("faded");
        }
      });
    },
    { rootMargin: "-40px" }
  );
  const cards = Array.from(document.getElementsByClassName("package-card"));
  cards.forEach((card) => {
    observer.observe(card);
  });
  /*
   * Add JavaScript for Leaflet maps
   */
  var map = L.map("map").setView([51.505, -0.09], 13);
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution:
      '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);
  map.setView(new L.LatLng(52.299, -9.657), 10);
  var marker = L.marker([52.299, -9.657]).addTo(map);
  marker.bindPopup("<b>Kerry Paintball</b><br>Located just outside Tralee on the Listowel road.").openPopup();
});
