$(function() {
    var cookie_name = $('body').attr('data-mobile-cookie');
    $(".desktop-link").attr("href", window.location).click(function() {
        $.cookie(cookie_name, "off", {expires:30});
    });
    $(".mobile-link").attr("href", window.location).click(function() {
        $.cookie(cookie_name, "on", {expires:30});
    });

    $.ajaxSetup({
         beforeSend: function(xhr, settings) {
             function getCookie(name) {
                 var cookieValue = null;
                 if (document.cookie && document.cookie != '') {
                     var cookies = document.cookie.split(';');
                     for (var i = 0; i < cookies.length; i++) {
                         var cookie = jQuery.trim(cookies[i]);
                         // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
             }
             if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                 // Only send the token to relative URLs i.e. locally.
                 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
             }
         }
    });


    if($("#delete_item").length > 0) {
        $("#delete_item").click(function() {
            var c = confirm("Are you sure you wish to delete? This cannot be undone.");
            if(c == true) {
                $.post($("#delete_item").data("url"), function(data) {
                    window.location = $("#delete_item").data("redirect");
                });
            }
        });
    }
});
