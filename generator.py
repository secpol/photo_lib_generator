#!/usr/bin/python
import sys, os
from itertools import cycle

cityname = "NewYork"
cityshort = "ny"
mytitle = "Holidays"
column_width = cycle(["3", "3", "6", "8", "4", "4", "4", "4"])	#width of the photo container, sum of numbers must be equal to 12 for one row
fade = cycle(["1", "100", "200"])	#fade time in ms
photo_path = "images/"+cityshort+"/"
#extension = ".jpg"
#photo_range = ["{0:03}".format(i) for i in range(191,215)] #3 digit format, define range first to last + 1
photo_list = os.listdir(photo_path)
photo_count = len(photo_list)	#number of photos in a directory

for i in photo_list:
	with open(cityname+"_generated"+".php", "a") as contents:
		    contents.write("				<div class=\"col-6 col-md-6 col-lg-{}\" data-aos=\"fade-up\" data-aos-delay=\"{}\">".format(next(column_width), next(fade)) + "\n")
		    contents.write("  				<a href=\"{}{}\" class=\"d-block photo-item\" data-fancybox=\"gallery\">".format(photo_path, i) + "\n")
		    contents.write("    					<img src=\"{}{}\" alt=\"Image\" class=\"img-fluid\">".format(photo_path, i) + "\n")
		    contents.write("    					<div class=\"photo-text-more\">" + "\n")
		    contents.write("      					<span class=\"icon icon-search\"></span>" + "\n")
		    contents.write("    					</div>" + "\n")
		    contents.write("  				</a>" + "\n")
		    contents.write("				</div>" + "\n")

with open(cityname+".php", "a+") as base, open("single_a.html", "r") as begin, open(cityname+"_generated"+".php", "r") as middle, open("single_b.html", "r") as end:
				base.write(begin.read())
				base.write(middle.read())
				base.write(end.read())

os.remove(cityname+"_generated"+".php")

with open(cityname+".php") as text:
	ntext = text.read().replace("pcount",str(photo_count)+" photos").replace("cname",cityname).replace("mtitle",mytitle)
with open(cityname+".php", "w") as text:
	text.write(ntext)
