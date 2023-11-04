  
  const pagination = function () {
    const parentElements = document.querySelector(".pagination");
    parentElements.addEventListener("click", function (e) {
      e.preventDefault();
      const currentEl = e.target.closest(".button-pagination");
      if (!currentEl) return;
      document.querySelectorAll(".button-pagination").forEach((curr) => {
        curr.classList.remove("active");
      });
      currentEl.classList.add("active");
      
      document.querySelectorAll(".contents").forEach((curr) => {
        curr.classList.add("hidden");
      });
      document
        .querySelector(`.content-${currentEl.dataset.num}`)
        .classList.remove("hidden");
    });
  };
  pagination();
