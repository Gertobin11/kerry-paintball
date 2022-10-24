window.addEventListener("DOMContentLoaded", () => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const intersecting = entry.isIntersecting;
        if (intersecting) {
          entry.target.classList.add("grow-in-left");
          entry.target.classList.remove("shrink");
        }
      });
    },
    { rootMargin: "-40px" }
  );
  const headers = Array.from(document.getElementsByClassName("info-header"));
  headers.forEach((header) => {
    observer.observe(header)
  })

  /*
   * Add JavaScript for Leaflet maps
   */

  var map2 = L.map("big-map").setView([51.505, -0.09], 13);
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution:
      '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map2);
  map2.setView(new L.LatLng(52.299, -9.657), 10);
  var marker2 = L.marker([52.299, -9.657]).addTo(map2);
  marker2
    .bindPopup(
      "<b>Kerry Paintball</b><br>Located just outside Tralee on the Listowel road."
    )
    .openPopup();
});
