(function () {
  // ---------------------------------------------------------------
  // 1. Custom footer link
  // ---------------------------------------------------------------
  function addCustomFooterLink() {
    var footer = document.querySelector(".ptx-page-footer");
    if (!footer || footer.querySelector(".custom-site-footer-link-wrap")) {
      return;
    }

    var wrap = document.createElement("div");
    wrap.className = "custom-site-footer-link-wrap";

    var prefix = document.createElement("span");
    prefix.className = "custom-site-footer-prefix";
    prefix.textContent = "Adapted to PreTeXt by ";

    var link = document.createElement("a");
    link.className = "custom-site-footer-link";
    link.href = "https://www.idems.international/";
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.textContent = "IDEMS International";
    link.setAttribute("aria-label", "Visit IDEMS International");

    wrap.appendChild(prefix);
    wrap.appendChild(link);
    footer.appendChild(wrap);
  }

  // ---------------------------------------------------------------
  // 2. R code block toggles
  //
  // PreTeXt renders <program language="r"> as:
  //   <div class="code-box">
  //     <pre class="program clipboardable">
  //       <code id="rs-code-..." class="language-r">...</code>
  //     </pre>
  //   </div>
  //
  // We prepend a "Show/Hide R code" button to each .code-box that
  // contains R code, and start with the code hidden so readers can
  // focus on the text and figures.
  // ---------------------------------------------------------------
  function addRCodeToggles() {
    var codeBoxes = document.querySelectorAll("div.code-box");

    codeBoxes.forEach(function (box) {
      // Check if this code-box contains R code
      var rCode = box.querySelector(
        'code[class~="language-r"], code[class~="language-R"]'
      );
      if (!rCode) return;

      // Create wrapper to hold button + code-box together
      var wrapper = document.createElement("div");
      wrapper.className = "r-code-toggle-wrapper";
      box.parentNode.insertBefore(wrapper, box);
      wrapper.appendChild(box);

      // Create toggle button
      var btn = document.createElement("button");
      btn.className = "r-code-toggle-btn";
      btn.setAttribute("aria-expanded", "false");
      btn.textContent = "Show R code";

      // Hide the code block initially
      box.style.display = "none";

      btn.addEventListener("click", function () {
        var expanded = btn.getAttribute("aria-expanded") === "true";
        if (expanded) {
          box.style.display = "none";
          btn.setAttribute("aria-expanded", "false");
          btn.textContent = "Show R code";
        } else {
          box.style.display = "";
          btn.setAttribute("aria-expanded", "true");
          btn.textContent = "Hide R code";
        }
      });

      wrapper.insertBefore(btn, box);
    });
  }

  // ---------------------------------------------------------------
  // Initialise after the DOM is ready
  // ---------------------------------------------------------------
  function init() {
    addCustomFooterLink();
    addRCodeToggles();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
