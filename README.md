# TagMD
A mp3 tag editor that is compatible with ID3, APE, Vorbis

http://wiki.slimdevices.com/index.php/Beginners_Guide_To_Tagging

Databases:
http://www.midomi.com/, http://audiotag.info/index.php, http://whatzatsong.com/, http://echoprint.me/, https://musicbrainz.org/, http://discogs.com/, http://freedb.org/, https://en.wikipedia.org/wiki/List_of_online_music_databases

lyrics:
https://www.genius.com , https://www.musixmatch.com/

fingerprinting:
https://www.quora.com/Is-there-an-API-for-Shazam-or-SoundHound
https://www.quora.com/Is-there-an-API-for-Shazam-or-SoundHound


if you aren't sure why your player isnt updating the tags after you change them you should remove all of the tag types because different players look for each tag first.To find CD info from an internet database (freedb, cddb) 

To determine which type of tag you need read below then when choose which tag type fits your player.
Tag types

MP3 files store tag information ("metadata", or data about data) in "ID3" tags. See Wikipedia for a discussion on the differences between ID3v1 (old!) and ID3v2 (newer!). Note both types can be present in a file simultaneously.
With SqueezeCenter, it would be best to eliminate ID3v1 tags entirely, skip ID3v2.2 and use ID3v2.3 or ID3v2.4 alone. ID3v1 tags are limited to 30 characters. Your tagging program of choice may correctly display truncated titles, but it may instead display ID3v2 tag titles or even data from its own cache, and it may not let you know what it's displaying. SqueezeCenter attempts to use ID3v2 if both tag types are present, but with so many different tag types, you can get confused as to which ones your files have. If you have incorrect tag data that seems to persist after you correct it and rescan, look for ID3v1 tags and eliminate them.
Note that some portable devices do not support ID3v2.4 tags yet.
APEv2 tags can also be present in an MP3 along with the ID3 tag types, this further confuses matters. Only MP3Gain should write APEv2 tags - do not put text-based data in APEv2 tags.
FLAC and OGG files store tags in VORBIS comments. (Be careful, as FLAC files can contain VORBIS comments and ID3 tags at the same time. If at all possible delete all ID3 tags from the flac file. FLAC standard only guarantees that VORBIS comments will be read by any flac compliant program, while ID3 may be read by some but not by others.This has confused some people, who were modifying the ID3 tags instead of the VORBIS ones, and not seeing the proper result.)
APE tags are similar to VORBIS comments, in that they are free-form. They are the native tag format for Musepack & Monkey's Audio formats. Additionally, APE tags are often used to store ReplayGain information in the footer of MP3 files.
WMA (Microsoft) and AAC (Apple) use proprietary file formats.
WAV files can't hold tag information at all.
