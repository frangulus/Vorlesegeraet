#!/bin/bash
#    Copyright (C) 2022 - 2022 Thomas Glaser
# 
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
#
## Setup

TEMP_DIR=./tmp/
TXT_FILE="$TEMP_DIR""rawText"
READ_FILE="$TEMP_DIR""readText"
IMAGE_FILE="$TEMP_DIR""scannedImage.tiff"
debug=0


cleanall(){
# clean text (function from xsane2speach has to be evaluated)
sed -i -r -e 's/››/"/g; s/[-—–]/-/g' "$TXT_FILE.txt"                                    # replaces incompatibel - char
sed -i -r -e 's/ﬁ/fi/g; s/ﬂ/fl/g; s/[íı]/i/g' "$TXT_FILE.txt"                           # fixes ligature ﬁ, ﬂ, char íı
sed -i -r -e 'N;s/([[:lower:]])-\n([[:lower:]][^ ]* ?)/\1\2\n/;P;D' "$TXT_FILE.txt"     # removes "Trennungen"
sed -i -r -e 's/([]])([aäeioöuü])/\ J\2/g' "$TXT_FILE.txt"                              # replace misinterpreted ] with J
sed -i -r -e 's/fš/ß/g' "$TXT_FILE.txt"                                                 # replaces misinterpreted fš with ß
sed -i -r -e 's/<</"/g; s/>>/"/g' "$TXT_FILE.txt"                                       # replaces incompatible characters    
sed -i -r -e 'N;s/([[:lower:]])([[:upper:]])/\1\ \2/' "$TXT_FILE.txt"                   # add missing spaces 
sed -i -r -e 'N;s/([[:lower:]]),([[:alnum:]])/\1\, \2/' "$TXT_FILE.txt"                 # add missing spaces 

                                            
}



#scanimage --source Flatbed --mode 'True Gray' --format=tiff --contrast 20% --brightness -10% --resolution 300 > $IMAGE_FILE
scanimage -l 0 -t 0 -x 216 -y 297 --mode 'Gray' --format=tiff  --resolution 300 > $IMAGE_FILE
tesseract $IMAGE_FILE $TXT_FILE -l deu
cleanall
python3 reorder.py
##{ if [ $debug == 1 ] ; then 
    
    #cat "$READ_FILE.txt"
#     echo "---- Debug run done ---- "
#    else
     #espeak-ng -vmb-de6 -b1 -s140 -f"$READ_FILE.txt"
#fi }    



