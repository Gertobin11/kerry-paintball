window.addEventListener("DOMContentLoaded", () => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const intersecting = entry.isIntersecting;
          if (intersecting) {
            entry.target.classList.add("grow-in-left");
            entry.target.classList.remove('shrink')
          }
        });
      },
      { rootMargin: "-40px" }
    );
    const header = document.getElementsByClassName("gallery-header")[0];
    console.log(header)
    observer.observe(header);
    /*
     * Apply a fade in effect on the images loading in
     */
    images = Array.from(document.getElementsByClassName('gallery-item'))
    wait = 0
    images.forEach((image) => {
        wait += 200
        setTimeout(() => {
            image.classList.add('fade-up')
            image.classList.remove('faded')
        }, 200 + wait)
    })
  });