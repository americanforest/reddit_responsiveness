$(function () {
    $('#domainform').on('submit', function (event) { //Upon submission of the domainform form
        event.preventDefault(); //Prevent reverting to default
      
        var subreddit = $('#s').val(); //Get user entered subreddit
        
        var cors_proxy = "https://cors.now.sh/"; //CORS proxy
        
        var requrl = "http://www.reddit.com/r/"+subreddit+"/about.json"; //Reddit API address
        
        var fullurl = cors_proxy + requrl;
        
        console.log(fullurl);
        
    }); 
});