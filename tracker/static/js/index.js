document.addEventListener("DOMContentLoaded", function () {

    const sidebarToggle =
        document.getElementById("sidebarToggle");

    const sidebar =
        document.querySelector(".sidebar");


    if (sidebarToggle && sidebar) {

        sidebarToggle.addEventListener("click", function () {
            sidebar.classList.add("show");
            window.setTimeout(() => hideOnClickOutside(sidebar), 100);
        });

    }

});


// Source - https://stackoverflow.com/a/3028037
// Posted by Art, modified by community. See post 'Timeline' for change history
// Retrieved 2026-08-15, License - CC BY-SA 4.0

function hideOnClickOutside(element) {
    const outsideClickListener = event => {
        if (!element.contains(event.target) && isVisible(element)) { // or use: event.target.closest(selector) === null
          element.classList.remove("show");
          removeClickListener();
        }
    }

    const removeClickListener = () => {
        document.removeEventListener('click', outsideClickListener);
    }

    document.addEventListener('click', outsideClickListener);
}

const isVisible = elem => !!elem && !!( elem.offsetWidth || elem.offsetHeight || elem.getClientRects().length ); // source (2018-03-11): https://github.com/jquery/jquery/blob/master/src/css/hiddenVisibleSelectors.js 
