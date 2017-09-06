$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == 'https:' ? 'wss' : 'ws';
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + window.location.pathname);
    var entries = {{ entries }};
    
    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        console.log('recieved message');
        console.log(message);
        var chat = $('#chat')
        var ele = $('<tr></tr>')

        ele.append(
            $('<td></td>').text(data.display_score)
        )
        ele.append(
            $('<td></td>').text(data.real_score)
        )
        ele.append(
            $('<td></td>').text(data.name)
        )
        
        chat.append(ele)
    };

    $('button').on('click', function() {
        var classes = $(this).attr('class').split(/\s+/);
        var message = {
            name: classes[0],
            direction: classes[1],
        }
        
        chatsock.send(JSON.stringify(message));
        console.log('sent message');
        console.log(message);
        return false;
    });
});