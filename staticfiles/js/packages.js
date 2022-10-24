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
  const header = document.getElementsByClassName("packages-header")[0];
  observer.observe(header);
});
