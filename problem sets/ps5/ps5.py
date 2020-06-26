# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()      
        
    def is_phrase_in(self, text):
        word_seperators = ' ' + string.punctuation
        for item in word_seperators:
            if item in text:
                my_list = text.lower().split(item)
                break
            else:
                my_list = [text.lower()]
            
        for i in range(len(my_list)):
            for item in word_seperators:
                if item in my_list[i]:
                    my_list[i] = my_list[i].replace(item, '')
        
        final_list = []
        for item in my_list:
            if item != '':
                final_list.append(item)
        
        final_text = ' '.join(final_list)
    
        words_in_phrase = self.phrase.split()
        counter = 0
        for word1 in words_in_phrase:
            for word2 in final_list:
                if word1 == word2:
                    counter += 1
            
        if self.phrase in final_text and counter == len(words_in_phrase):
            return True
        else:
            return False
        

# Problem 3
# TODO: TitleTrigger
            
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        title = story.get_title().lower()
        return PhraseTrigger.is_phrase_in(self, title)

# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        description = story.get_description().lower()
        return PhraseTrigger.is_phrase_in(self, description)

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, time):
        pubdate = datetime.strptime(time, "%d %b %Y %H:%M:%S")
        pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))
        self.time = pubdate
        
# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
        
    def evaluate(self, story):
        pubdate = story.get_pubdate()
        pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))
        if pubdate < self.time:
            return True
        else:
            return False
        
class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
        
    def evaluate(self, story):
        pubdate = story.get_pubdate()
        pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))
        if pubdate > self.time:
            return True
        else:
            return False        

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
        
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def evaluate(self, story):
        if self.trigger1.evaluate(story) and self.trigger2.evaluate(story):
            return True
        else:
            return False

# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def evaluate(self, story):
        if self.trigger1.evaluate(story) or self.trigger2.evaluate(story):
            return True
        else:
            return False

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    
    stories_to_be_returned = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                stories_to_be_returned.append(story)
                break
    return stories_to_be_returned

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    
    trigger_dict = {}
    trigger_list = []
    for line in lines:
        elements = line.split(',')
        if elements[0] != 'ADD':
            if elements[1] == 'TITLE':
                trigger_dict[elements[0]] = TitleTrigger(elements[2])
            elif elements[1] == 'DESCRIPTION':
                trigger_dict[elements[0]] = DescriptionTrigger(elements[2])
            elif elements[1] == 'BEFORE':
                trigger_dict[elements[0]] = BeforeTrigger(elements[2])
            elif elements[1] == 'AFTER':
                trigger_dict[elements[0]] = AfterTrigger(elements[2])
            elif elements[1] == 'NOT':
                trigger_dict[elements[0]] = NotTrigger(elements[2])
            elif elements[1] == 'AND':
                trigger_dict[elements[0]] = AndTrigger(elements[2], elements[3])
            elif elements[1] == 'OR':
                trigger_dict[elements[0]] = OrTrigger(elements[2], elements[3])
        else:
            for index in range(1, len(elements)):
                if elements[index] in trigger_dict.keys():
                    trigger_list.append(trigger_dict[elements[index]])
                
    return trigger_list
    

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Coronavirus")
        t2 = TitleTrigger("Turkey")
        t3 = AfterTrigger("13 May 2020 17:00:00")
        t4 = AndTrigger(t1, t2)
        triggerlist = [t3, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk() 
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

