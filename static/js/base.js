window,addEventListener('DOMContentLoaded', () => {
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

  /*
   * Add Animation to the burger Menu 
  */
  const burgerToggler = document.getElementsByClassName('navbar-toggler')[0];
  let isOpen = false;
  burgerToggler.addEventListener('click', () => {
    console.log(isOpen)
    if (!isOpen) {
      burgerToggler.classList.add('open');
      isOpen = true;
    }
    else {
      burgerToggler.classList.remove('open');
      isOpen = false;
    }
  })

  /*
   * Remove the message after 3 seconds
  */
  const messageContainer = document.getElementsByClassName('message-container')[0];
  if(messageContainer){
    setTimeout(() => {
      messageContainer.remove()
    }, 4000)
  }

})