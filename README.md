# candice-odenver-scraper
Web scraper for talks by Candice O'Denver

## What

A friend of mine who love Candice O'Denver's Great Freedom lectures, told me he couldn't find the innumerable MP3s that used to be available for free on her site. Wanting to help my friend, I made this scraper to help download those old talks.

## How

I found the MP3s after looking through WayBackMachine at old snapshots of her sites. I found the page where the MP3s were, and found that they are still being hosted on AWS.

I started downloading the MP3s manually, but then saw that there are thousands of them, and even the simple yet tedious process I had found would have taken me several days to weeks to complete.

So I wrote this python scraping script in about 3 hours :)

## Usage

This is a very basic script, uploaded soley for the purpose of aiding anyone who might also be looking for Candice O'Denver's free talks. It was written in 3 hours, and not with user experience in mind.

All you have to do to make this script work for you is...

1. Make sure you have Python 3 running on your computer
2. `pip install` the requisite libraries. Namely, `BeautifulSoup` and maybe `requests`
3. Change the folder prefix on line 46 of main.py to whatever folder on your computer you want the files to be saved to
4. Run `python main.py`

That's it! You should see the script downloading the files to your folder.

## Gotcha

The script for me stopped halfway through. That's almost 200 hours of listening, so not a bad start. If this gets fixed, I'll update the README accordingly.

And yes, contributions are welcome :)
