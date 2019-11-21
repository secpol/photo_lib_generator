#!/usr/bin/python
import fileinput
import sys, os
from itertools import cycle
import random

#page_name = "New York"
column_width = cycle(["3", "3", "6", "8", "4", "4", "4", "4"])	#width of the photo container, sum must be equal to 12 for one row
fade = cycle(["1", "100", "200"])	#time when picture appear
photo_path = "images/usa/image"
extension = ".jpg"
photo_range = ["{0:03}".format(i) for i in range(191,215)] #3 digit format, define range first to last + 1
#photo_count = len(photo_range)	#experimental, for future development

for i in photo_range:
	with open("test.html", "a") as myfile:
	    myfile.write("<div class=\"col-6 col-md-6 col-lg-{}\" data-aos=\"fade-up\" data-aos-delay=\"{}\">".format(next(column_width), next(fade)) + "\n")
	    myfile.write("  <a href=\"{}{}{}\" class=\"d-block photo-item\" data-fancybox=\"gallery\">".format(photo_path, i, extension) + "\n")
	    myfile.write("    <img src=\"{}{}{}\" alt=\"Image\" class=\"img-fluid\">".format(photo_path, i, extension) + "\n")
	    myfile.write("    <div class=\"photo-text-more\">" + "\n")
	    myfile.write("      <span class=\"icon icon-search\"></span>" + "\n")
	    myfile.write("    </div>" + "\n")
	    myfile.write("  </a>" + "\n")
	    myfile.write("</div>" + "\n")


#under development: generate entire website

#with fileinput.FileInput("test.html", inplace=True, backup='.bak') as file:
    #for line in file:
        #print(line.replace("Shutter", page_name), end='')
