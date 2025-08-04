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
});
