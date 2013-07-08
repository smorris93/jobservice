function status(x)
{
    console.log('status', x);
    $('#status').text(x);
}

$(
    function()
    {
        var lRate = 5000;
        var lProgressBar = $("#progressbar");
        var lProgressLabel = $(".progress-label");
        lProgressBar.progressbar(
            {
                value: false,
                change: function()
                {
                    lProgressLabel.text(lProgressBar.progressbar("value") + "%");
                }
            }
        );
});

$(document).ready(function()
    {
        var lProgressBar = $("#progressbar");
        var lProgressLabel = $(".progress-label");

        //status('Connecting ...');
        socket = io.connect("");

        socket.on('connect', function()
            {
                //status('Connected');
                socket.emit('update', '');
            });
        socket.on('reconnect', function()
            {
                status('');
            });
        socket.on('reconnecting', function(msec)
            {
                status('Connection lost. Reconnecting in ' + (msec/1000) + ' seconds ...');
                $("#status").append($('<a href="#">').text("Try now").click(function(evt)
                        {
                            evt.preventDefault();
                            socket.socket.connect();
                        }));
            });
        socket.on('connect_failed', function() { /* status('Connect failed.'); */ });
        socket.on('reconnect_failed', function() { /* status('Reconnect failed.'); */ });
        socket.on('error', function (e) { /* status('Error: ' + e); */ });
        socket.on('progress', function(pArg) 
            {
                //status("Progress. " + pArg);
                lProgressLabel.css("color", "black");
                lProgressBar.progressbar("value", pArg);
            });
        socket.on('success', function(pArg) 
            {
                //status("Progress. " + pArg);
                lProgressBar.progressbar("value", 100);
                lProgressLabel.css("color", "red");
                lProgressLabel.text("Password: '" + pArg + "'");
            });
        socket.on('reset_progress', function(pArg) 
            {
                console.log("resetting ...");
                socket.emit('update', '');
            });
    });
function status(x)
{
    console.log('status', x);
    $('#status').text(x);
}

$(
    function()
    {
        var lRate = 5000;
        var lProgressBar = $("#progressbar");
        var lProgressLabel = $(".progress-label");
        lProgressBar.progressbar(
            {
                value: false,
                change: function()
                {
                    lProgressLabel.text(lProgressBar.progressbar("value") + "%");
                }
            }
        );
});

$(document).ready(function()
    {
        var lProgressBar = $("#progressbar");
        var lProgressLabel = $(".progress-label");

        //status('Connecting ...');
        socket = io.connect("");

        socket.on('connect', function()
            {
                //status('Connected');
                socket.emit('update', '');
            });
        socket.on('reconnect', function()
            {
                status('');
            });
        socket.on('reconnecting', function(msec)
            {
                status('Connection lost. Reconnecting in ' + (msec/1000) + ' seconds ...');
                $("#status").append($('<a href="#">').text("Try now").click(function(evt)
                        {
                            evt.preventDefault();
                            socket.socket.connect();
                        }));
            });
        socket.on('connect_failed', function() { /* status('Connect failed.'); */ });
        socket.on('reconnect_failed', function() { /* status('Reconnect failed.'); */ });
        socket.on('error', function (e) { /* status('Error: ' + e); */ });
        socket.on('progress', function(pArg) 
            {
                //status(pArg.value);
                lProgressBar.progressbar("value", pArg.value);
                if (pArg.success)
                {
                    lProgressLabel.css("color", "red");
                    lProgressLabel.text("Result: '" + pArg.message + "'");
                }
                else
                {
                    lProgressLabel.css("color", "black");
                    lProgressBar.progressbar("value", pArg.value);
                }
            });
        socket.on('reset_progress', function(pArg) 
            {
                socket.emit('update', '');
            });
    });
