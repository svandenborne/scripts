import glob
import re
import stopwords

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

def splitfile(f):
    for line in f.splitlines():
        s = line.split('$$$')
        #danger! assumed that each line has three values splitted by "$$$"
        actors = s[1]
        for actor in actors.split('$$'):
            for word in s[2].split():
                w = re.sub('[\W_]', ' ', word).strip().lower()
                if len(w) > 1 and w not in stopwords.allStopWords: 
                    print actor, w, 1         
 

content = file_contents('data/movies.txt')
splitfile(content)


