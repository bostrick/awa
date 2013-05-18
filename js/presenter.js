/***************************************************************************
 *
 * PresenterManager
 * 
 ***************************************************************************/

function PresenterManager() {

    this.phost = "http://localhost/"
    this.presenter_base_url = this.phost + "presenter/"
    this.presentation_base_url = this.phost + "awa/"
    this.poll_delay = 5*1000; // ms 
    
    this.user = undefined;
    this.current_slide = undefined;

    this.bind_events();

    /* jquery-ui init */
    /*
    $("#console_accordion").accordion({
        collapsible: true,
        active: false,
    });
    $("#console_tabs").tabs();
    $("div.progress_bar").progressbar({ value: false });
    */

    this.poll();
}

PresenterManager.prototype.bind_events = function () {

    var pmgr = this;
    window.setInterval(function () { pmgr.poll(); }, pmgr.poll_delay);
    
    $("#logo_container").on("click", pmgr, pmgr.lower_hand);
    $("#user_logo").on("click", pmgr, pmgr.raise_hand);

}

PresenterManager.prototype.lower_hand = function (event) {

    var pmgr = event.data;
    var img = event.target;
    var hand = img.id.split("_")[1];

    console.log("lower " + hand);
    $.post(pmgr.presenter_base_url + "lower_hand", {'hand': hand});

    $(img).remove();
}

PresenterManager.prototype.raise_hand = function (event) {

    var pmgr = event.data;
    console.log("raise hand" + pmgr.user);
    if (pmgr.user == -1) { return };
    $.post(pmgr.presenter_base_url + "raise_hand");
}

PresenterManager.prototype.poll = function () {
    var pmgr = this;
    $.ajax({
            type: "GET",
            url: pmgr.presenter_base_url,
            context: pmgr,
    }).done(pmgr.handle_poll_response);
}

PresenterManager.prototype.handle_poll_response = function (msg) {

    pmgr = this;
    console.log("poll");
    console.log(msg);

    if (pmgr.user != msg.user) {
        pmgr.switch_user(msg.user);
    }

    /* FIXME: race here... what if changed before undefined got set? */
    if (pmgr.slide === undefined) {
        console.log("setting page to " + msg.slide);
        pmgr.slide = msg.slide;
    } else if (pmgr.slide != msg.slide) { 
        console.log("relocated page to " + msg.slide);
        window.location = msg.slide;
    }

    if (pmgr.is_presenter()) {
        pmgr.display_hands(msg.hands);
    }
}

PresenterManager.prototype.display_hands = function (hands) {

    img_container = $("#logo_container");
    
    hands.forEach(function (item) {

        if (item == "") { return };

        var hid = "hand_" + item;
        h = $("#" + hid);
        if (h.length) {return };

        console.log("adding " + item);

        img = $("<img/>");
        img.attr("src", "img/"+item+".png");
        img.attr("id", hid);

        img_container.append(img);
    });
}

PresenterManager.prototype.switch_user = function (new_user) {

    console.log("setting user to " + new_user);
    pmgr.user = new_user;
    if (pmgr.is_presenter()) {
        pmgr.become_presenter();
        return;
    }

    $("#user_logo").attr("src", "img/" + new_user + ".png");
}



PresenterManager.prototype.get_current_slide = function () {
    var slide = window.location.pathname.split("/");
    slide = slide[slide.length-1];
    return slide;
}

PresenterManager.prototype.is_presenter = function () {
    return (this.user == -1);
}

PresenterManager.prototype.become_presenter = function () {

    var pmgr = this;
    
    console.log("becoming presenter");
    $("#user_logo").attr("src", "img/qr_100.png");

    pmgr.get_current_slide();
    
    $.ajax({
            type: "POST",
            url: pmgr.presenter_base_url + "set_slide",
            data: { 'slide': pmgr.get_current_slide },
            context: pmgr,
    }).done(pmgr.handle_post_response);
}

PresenterManager.prototype.handle_post_response = function (msg) {
    pmgr = this;
    console.log("post");
}

/*
ConsoleManager.prototype.handle_click = function (event) {

    var cmgr = event.data;
    var btn = event.target;
    var form_data = $("#station_action_form").serialize();
    var action_info = cmgr.action_map[btn.id];

    event.preventDefault();

    if (btn.id == "refresh") { document.location.reload(); return; }

    if (action_info.how == 'console') {

        var data = form_data + "&ajax=1&" + btn.id + "=" + btn.id;
        console.debug("posting: " + data);

        $.post(location.href, data, function(data) {
            console.debug("post back");
            if (action_info.pendable) {
                cmgr.pending_request = btn.id;
                cmgr.pending_request_count = cmgr.pending_request_count_max;
                cmgr.change_state("pending_action");
            }
        });
    }
}
*/
