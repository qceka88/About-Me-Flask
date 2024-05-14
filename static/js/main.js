(function ($) {
    "use strict";


    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 43) {
            $('.navbar').addClass('sticky-top shadow-sm position-fixed w-100');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm position-fixed w-100');
        }
    });


    // Smooth scrolling on the navbar links
    $(".navbar-nav a").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();

            $('html, body').animate({
                scrollTop: $(this.hash).offset().top - 45
            }, 250, 'easeInOutExpo');

            if ($(this).parents('.navbar-nav').length) {
                $('.navbar-nav .active').removeClass('active');
                $(this).closest('a').addClass('active');
            }
        }
    });

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 500, 'easeInOutExpo');
        return false;
    });

    // Back to top button-mobile
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top-mobile').fadeIn('slow');
        } else {
            $('.back-to-top-mobile').fadeOut('slow');
        }
    });
    $('.back-to-top-mobile').click(function () {
        $('html, body').animate({scrollTop: 0}, 500, 'easeInOutExpo');
        return false;
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Screenshot carousel
    $(".screenshot-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        loop: true,
        dots: false,
        autoplayTimeout: 2500,
        items: 1
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        loop: true,
        center: true,
        dots: false,
        nav: true,
        page: true,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });


    // Change Certificates Class
    function changeCertificates() {
        const certificatesContainer = document.getElementById("my-certificates");
        let certificatesElements = document.querySelectorAll('.certificate-item');

        if (window.innerWidth <= 600 && certificatesContainer.className === "row gy-5 gx-4 justify-content-center") {
            certificatesContainer.className = "owl-carousel testimonial-carousel";
            certificatesElements.forEach(el => {
                el.className = 'testimonial-item p-3 rounded certificate-item';
                el.removeAttribute('data-wow-delay');
            });
            let testimonialCertificateCarousel = $("#certificates").find(".testimonial-carousel");

            // Testimonials carousel Mobile Version
            testimonialCertificateCarousel.owlCarousel({
                autoplay: true,
                loop: true,
                smartSpeed: 1000,
                center: true,
                dots: true,
                nav: true,
                page: true,
                navText: [
                    '<i class="bi bi-chevron-left"></i>',
                    '<i class="bi bi-chevron-right"></i>'
                ],
                responsive: {
                    0: {
                        items: 2
                    },
                    768: {
                        items: 4
                    },
                    992: {
                        items: 6
                    }
                }
            });

        }
    }
    changeCertificates();
})(jQuery);


// Hide/See phone number
function phoneNumberToggle() {
    const phone = document.getElementById("my-number")
    const toggle = document.getElementById("number-toggle")
    const text = document.getElementById("see-number-text")
    // const img = document.getElementById("my-img");
    const revealedNumber = "+359889110846"
    const hiddenNumber = "+359*********"

    if (phone.innerText === hiddenNumber) {
        phone.innerText = revealedNumber
        // phone.style.display = "none"
        // img.style.display = "block"
        toggle.className = "fa fa-toggle-off fa-xl my-0"
        toggle.style.color = "gray"
        text.innerText = ""
    } else {
        phone.innerText = hiddenNumber
        // phone.style.display = "block"
        // img.style.display = "none"
        toggle.className = "fa fa-toggle-on fa-xl text-primary my-0"
        text.innerText = "(see number)"

    }

}

//Draggable window
function dragChatWindow(window) {
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;

    let isHeader = window.querySelector('.messageBox-header')
    if (isHeader) {
        isHeader.onmousedown = dragMouseDown;
    }

    function dragMouseDown(element) {
        element = element || window.event;
        element.preventDefault();

        pos3 = element.clientX;
        pos4 = element.clientY;

        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
    }

    function elementDrag(element) {
        element = element || window.event;
        element.preventDefault();

        pos1 = pos3 - element.clientX;
        pos2 = pos4 - element.clientY;
        pos3 = element.clientX;
        pos4 = element.clientY;

        window.style.top = (window.offsetTop - pos2) + 'px';
        window.style.left = (window.offsetLeft - pos1) + 'px';
    }

    function closeDragElement() {
        document.onmouseup = null;
        document.onmousemove = null;
    }
}

// Open/Close chat window
function openCloseChat() {
    let element = document.getElementById("mychat");
    if (element.style.display === "block") {
        element.style.display = "none";
    } else {
        element.style.display = "block";
        dragChatWindow(element);
    }
}


// Close Collapsed Nav Bar
function closeNavbar() {
    var form = document.getElementById("navbarCollapse");
    const navButton = document.getElementById("navBut");
    if (form.style.display !== "none") {
        navButton.click()
    }
}

// Check nav but is visible
function isNavButVisible() {
    var navBut = document.getElementById('navBut');
    var navItems = document.querySelectorAll('.menuButton');

    if (navBut.offsetParent !== null) {
        // #navBut is visible
        navItems.forEach(function (navItem) {
            navItem.addEventListener('click', closeNavbar);
        });
    } else {
        // #navBut is not visible
        navItems.forEach(function (navItem) {
            navItem.removeEventListener('click', closeNavbar);
        });
    }
}


// For initial bot message take current time.
function getCurrentDateAndTime() {
    const dateTime = new Date();
    return formatDate(dateTime);
}

const dateDisplay = document.getElementById("time-now");
dateDisplay.textContent = getCurrentDateAndTime();

// Format hours for chat messages
function formatDate(date) {
    const h = "0" + date.getHours();
    const m = "0" + date.getMinutes();

    return `${h.slice(-2)}:${m.slice(-2)}`;
}

// Chatbot get message and return response
function chatBot() {

    const messengerForm = get(".messageBox-inputArea");
    const messengerInput = get(".messageBox-input");
    const messengerChat = get(".messageBox-chat");

    const BOT_IMG = '/static/img/chat/bot_image.jpg';
    const PERSON_IMG = '/static/img/chat/user_picture.jpg';
    const BOT_NAME = "    Robo";
    const PERSON_NAME = "You";

    messengerForm.addEventListener("submit", event => {
        event.preventDefault();

        const messageText = messengerInput.value;
        if (!messageText) return;

        appendMessage(PERSON_NAME, PERSON_IMG, "visitor", messageText);
        messengerInput.value = "";
        botResponse(messageText);
    });

    function appendMessage(name, image, side, text) {
        //   Simple solution for small apps
        const messageHTML = `
<div class="message ${side}-message">
  <div class="message-image" style="background-image: url(${image})"></div>

  <div class="message-bubble">
    <div class="message-info">
      <div class="message-info-name">${name}</div>
      <div class="message-info-time">${formatDate(new Date())}</div>
    </div>
    <div class="message-text">${text}</div>
  </div>
</div>
`;

        messengerChat.insertAdjacentHTML("beforeend", messageHTML);
        messengerChat.scrollTop += 500;
    }

    function botResponse(rawText) {

        // Bot Response
        $.get("/get", {"message": rawText}).done(function (data) {
            const messageText = data;
            console.log(messageText)
            appendMessage(BOT_NAME, BOT_IMG, "chat-bot", messageText);
        });
    }

    // Utils
    function get(selector, root = document) {
        return root.querySelector(selector);
    }
}