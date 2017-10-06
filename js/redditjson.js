$(function() {
    $('#domainform').on('submit', function(event) { //Upon submission of the domainform form
        
        event.preventDefault(); //Prevent reverting to default

        var subreddit = $('#s').val(); //Get user entered subreddit

        var cors_proxy = "https://cors.now.sh/"; //CORS proxy

        var requrl = "http://www.reddit.com/r/" + subreddit + "/new.json?limit=5"; //Reddit API address

        var fullurl = cors_proxy + requrl; //Combine CORS Proxy with request REST URL for full URL

        $.getJSON(fullurl, function(jsonoutput) { //Make JSON request with full URL

            threads = jsonoutput.data.children;

            console.log(threads[1]["data"]["created_utc"]);

        });
    });
});