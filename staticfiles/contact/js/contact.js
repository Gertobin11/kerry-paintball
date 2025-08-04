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
    const header = document.getElementsByClassName("contact-header")[0];
    console.log(header)
    observer.observe(header);
  });