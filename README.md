# MP3sort
Simple script to sort mp3 files by ID3 tag data

## Usage

Examples:

`python mp3sort.py /Users/somebody/Desktop/unsorted_mp3s`  
Sorts all MP3 files in `/Users/somebody/Desktop/unsorted_mp3s` in folders located on the Desktop.

`python /Users/somebody/Desktop/unsorted_mp3s --dest /Users/somebody/Music`  
Sorts all MP3 files in `/Users/somebody/Desktop/unsorted_mp3s` in folders located in `/Users/somebody/Music`.

`python /Users/somebody/Desktop/unsorted_mp3s --format $artist/$year/$album`  
Sorts all MP3 files in `/Users/somebody/Desktop/unsorted_mp3s` in folders located on the Desktop, using the specified folder structure.

`python mp3sort.py /Users/somebody/Desktop/unsorted_mp3s --preview`  
Sorts all MP3 files in `/Users/somebody/Desktop/unsorted_mp3s` in folders located on the Desktop, but DOESN'T actually move the files. Instead, only a preview will be shown.

## Requirements
* Python 3
* Python module EyeD3 (script will attempt to install it automatically)

## Copyright
&copy; 2020 by Frank Willeke  
Published under GNU Public License v3