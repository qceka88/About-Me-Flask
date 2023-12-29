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

    // Screenshot carousel
    $(".screenshot-carousel-mobile").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        loop: true,
        dots: false,
        autoplayTimeout: 3000,
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
})(jQuery);

// Open/Close chat window

function openCloseChat() {
    var form = document.getElementById("mychat");
    if (form.style.display === "block") {
        form.style.display = "none";
    } else {
        form.style.display = "block";
    }
}

function closeNavBar() {
    var form = document.getElementById("navbarCollapse");
    const navButton = document.getElementById("navBut");
    if (form.style.display !== "none") {
        navButton.click()
    }
}

// For initial bot message take current time.
function getCurrentDateAndTime() {
    const dateTime = new Date();
    return formatDate(dateTime);
}

const dateDisplay = document.getElementById("time-now");
dateDisplay.innerHTML = getCurrentDateAndTime();

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