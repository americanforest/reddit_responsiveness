$(function() {
    $('#domainform').on('submit', function(event) { //Upon submission of the domainform form
        
        event.preventDefault(); //Prevent reverting to default
        
        var currentime = parseFloat(Math.round((new Date()).getTime() / 1000)); //Current time in UNIX UTC as a float
        
        var upvotes = 10;
        
        var scorehigh = []; //Create the array that will be used

        var subreddit = $('#s').val(); //Get user entered subreddit

        var cors_proxy = "https://cors.now.sh/"; //CORS proxy

        var requrl = "http://www.reddit.com/r/" + subreddit + "/new.json?limit=80000"; //Reddit API address

        var fullurl = cors_proxy + requrl; //Combine CORS Proxy with request REST URL for full URL

        $.getJSON(fullurl, function(jsonoutput) { //Make JSON request with full URL

            threads = jsonoutput.data.children; //This is all the threads collected by the JSON call
            
            for (thread in threads) { //Loop over all collected threads
                
                created_time_string = threads[thread]["data"]["created_utc"]; //Time when thread was created
                
                score = parseFloat(threads[thread]["data"]["ups"]); //Upvotes
                
                created_time_float = parseFloat(created_time_string); //Convert to a floating point number
                
                var difference = currentime - created_time_float; //Time difference between now and when it was created
                
                if (difference > 3600 && difference < 64800) { //If difference is between 1 and 2 days then proceed
                    
                    if ( score > upvotes ) {
                        
                        scorehigh.push("1");
                        
                    } else {
                        
                        scorehigh.push("0");
                        
                    }
                    
                }
                
            }
            
            num_threads = scorehigh.length;
            
            high_scores = parseFloat("0");
            
            for ( score in scorehigh ) {
                
                if (scorehigh[score] == 1) {
                    
                    high_scores++;
                    
                }
            
            }
            
            if ( num_threads > 0 ) {
            
                ratio = (100*high_scores/num_threads).toFixed(4); //Ratio of threads with more than upvote upvotes
                
                document.getElementById("content").innerHTML="<b>"+ratio+"%</b> of threads in this subreddit go more than "+upvotes+" upvotes in the last 16 hours"
                
            } else {
                
                document.getElementById("content").textContent="Error: No threads within last 16 hours!";
                
            }

        });
    });
});