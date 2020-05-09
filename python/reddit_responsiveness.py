# Import PRAW, a Python package for interactin with the Reddit API

import praw

#Import Time to get current time

import time

# Create the instance of Reddit to use

reddit = praw.Reddit(client_id='OnutaBIG1C-oKA',
                     client_secret='',
                     user_agent='fedora (by /u/glkjap)') 

# Current UNIX time UTC

now = time.time()


#Array of number of comments and score

numscorearray=[]

numcomarray=[]

#Array of subreddits

subs = ["announcements","funny","AskReddit","todayilearned","science","worldnews","pics","IAmA","gaming","videos","movies","aww","blog","Music","gifs","news","explainlikeimfive","askscience","EarthPorn","books","television","LifeProTips","mildlyinteresting","space","Showerthoughts","DIY","Jokes","sports","gadgets","tifu","nottheonion","InternetIsBeautiful","photoshopbattles","food","history","Futurology","Documentaries","dataisbeautiful","listentothis","UpliftingNews","personalfinance","GetMotivated","OldSchoolCool","philosophy","Art","nosleep","creepy","WritingPrompts","TwoXChromosomes","Fitness","technology","WTF","bestof","AdviceAnimals","politics","atheism","europe","interestingasfuck","woahdude","gonewild","gameofthrones","leagueoflegends","pcmasterrace","BlackPeopleTwitter","reactiongifs","trees","Unexpected","oddlysatisfying","Overwatch","Android","wholesomememes","programming","Games","facepalm","nba","nsfw","4chan","me_irl","relationships","lifehacks","cringepics","fffffffuuuuuuuuuuuu","sex","pokemon","tattoos","comics","soccer","reddit.com","Frugal","NSFW_GIF","pokemongo","RealGirls","ImGoingToHellForThis","CrappyDesign","malefashionadvice","OutOfTheLoop","StarWars","dankmemes","buildapc","YouShouldKnow","AskHistorians","AskTrumpSupporters","Atlanta","AtlantaEats","AtlantaUnited","baseball","bestof","Boxing","Braves","buildapc","CasualConversation","Championship","changemyview","classiccovers","climateskeptics","columbiasc","comicbooks","coolguides","coversongs","coys","CrowdPulledOnStage","dataisbeautiful","DebateCommunism","DecaturGA","DeltaLog","DepthHub","Documentaries","economy","explainlikeimfive","feelgood","Gamecocks","gatech","Guitar","happycrowds","history","HomeNetworking","HumansBeingBros","IAmA","InternetIsBeautiful","IWantToLearn","Jokes","Judaism","lectures","linux","linux4noobs","london","MarchForScience","math","MLS","MurderedByWords","Music","nano","NatureGifs","networking","nffc","nostalgia","opendirectories","Physics","politics","programming","punk","science","scifi","soccer","space","steamdeals","sysadmin","talesfromtechsupport","technology","techsupport","todayilearned","videos","wikipedia","worldnews","xboxone","YouShouldKnow"]

print "Subreddit, % with > 3 comments, % with > 10 score, Total submissions"

for sub in subs:

	#Loop over all submissions from 1-2 days ago and see how many have more than 3 comments

	for submission in reddit.subreddit(sub).new(limit = None):

		sub_time = submission.created_utc

		time_diff = float(now) - float(sub_time)

		comments = int(submission.num_comments)

		if time_diff > float(3600) and time_diff < float(43200):
			
			if int(submission.score) > 10:

				numscorearray.append(1);				

			else:
				
				numscorearray.append(0);

			if comments > 3:

				numcomarray.append(1);				

			else:
				
				numcomarray.append(0);


	total_subs = len(numcomarray)

	total_responsives = 0

	total_score_responsives = 0

	for responsive in numcomarray:

		if responsive == 1:

			total_responsives = total_responsives + 1

	for responsive in numscorearray:

		if responsive == 1:
			
			total_score_responsives = total_score_responsives + 1

		
	total_responsives_f = float(total_responsives)

	total_score_responsives_f = float(total_score_responsives)

	total_subs_f = float(total_subs)


	if total_subs_f > 0:

		percentage = round(total_responsives_f*100/total_subs_f);

		score_percentage = round(total_score_responsives_f*100/total_subs_f);

		print sub + ", " + str(percentage)+", "+ str(score_percentage) + ", "+str(total_subs_f)


