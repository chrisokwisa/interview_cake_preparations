# Design a URL shortener like TinyURL or bit.ly . This is a system design problem.

# The goal is to design a system that takes a very long URL and converts it into a short URL. 
# The short URL should be short enough to be easily copied and pasted into 
# applications, and should redirect to the original URL when visited.  
# The system should also be able to handle a large volume of requests, since millions of URLs will be shortened.


# For example, the URL https://www.interviewcake.com/ is 38 characters long.
# If we shorten it to https://ic.k/1, that's only 10 characters, and we can easily 
# copy and paste it into applications.

# We'll use a hash function to convert a URL like https://www.interviewcake.com/
# into a short string like 1. We'll store the URL and its short string in a database.

# When someone visits the short URL https://ic.k/1, our application will look up
# that short string in our database and redirect them to the original URL https://www.interviewcake.com/.

# We'll also want to prevent people from using the same short string for different URLs.
# For example, if we shortened https://www.interviewcake.com/ to 1, we wouldn't want
# someone to be able to use 1 to shorten https://www.google.com/ and have it redirect to https://www.interviewcake.com/.


# Features:

# Is this a full web app with a web interface? No let's just build an API

# Since it's an API, do we need aunthentication or user accounts to develop keys? No, let's just make it open to start

# can people modify or delete links? Let's leave that out for now

# 
