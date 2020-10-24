import os
import string
import shutil
import argparse

DEFAULT_FOLDERTEMPLATE = "$artist/$album"

# Import EyeD3 module. If it does not exist, install it
try:
    import eyed3
except ImportError:
    print("Trying to Install required module: eyed3\n")
    try:
        # Explicit Python3 call
        os.system("python3 -m pip install eyed3")
    except:
        # General call
        os.system("python -m pip install eyed3")


def get_file_metadata(filePath):
    """Reads the ID3 tag of the passed MP3 file, and returns the metadata
    """
    try:
        mp3File = eyed3.load(filePath)
        metaData = {
            "file": filePath,
            "title": mp3File.tag.title,
            "artist": mp3File.tag.artist,
            "album": mp3File.tag.album,
            "year": mp3File.tag.getBestDate(),
            "album_artist": mp3File.tag.album_artist
        }
        return metaData
    except:
        print("%s seems corrupted. Skipping this one." % os.path.basename(filePath))


def iterate_folder(sourceFolder):
    """Iterates files in sourceFolder. For each MP3 file, get_file_metadata() is called
    """
    print("Reading folder contents...")
    metaData = []
    for f in os.listdir(sourceFolder):
        if os.path.splitext(f)[1].upper() == ".MP3":
            filePath = os.path.join(sourceFolder, f)
            metaData.append(get_file_metadata(filePath))
    return metaData


def process_list(metaData, destBaseFolder, folderTemplateString, preview):
    """Iterates meta data list, creates the destination folders, moves files (or just previews the result)
    """
    if preview:
        print("\nPreview:")
    else:
        print("Moving %i files..." % len(metaData))

    # Iterate metaData
    for dataset in metaData:
        # Construct destination path for mp3File
        # Replace $artist with artist name, and $album with album name
        folderTemplate = string.Template(folderTemplateString)
        folderName = folderTemplate.safe_substitute(artist=dataset["artist"], album=dataset["album"], year=dataset["year"], albumartist=dataset["album_artist"])
        destFolder = os.path.join(destBaseFolder , folderName)

        if preview:
            # Print destination folder name
            print("%s --> %s" % (os.path.basename(dataset["file"]), destFolder))
        else:
            # Create destination folder, if it does not already exist
            if not os.path.isdir(destFolder):
                os.makedirs(destFolder)

            # Move file to destination folder
            shutil.move(dataset["file"], destFolder)


def main():
    """Program starts here
    """
    # Set up parser for command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("sourceFolder", type=str, default=None)
    parser.add_argument("-d", "--dest", dest="destBaseFolder", type=str, default=None, metavar="DESTFOLDER", help="Destination folder")
    parser.add_argument("-f", "--format", dest="folderFormat", type=str, default=DEFAULT_FOLDERTEMPLATE, metavar="FOLDERFORMAT", help="Format for destination folders (supported placeholders: $artist, $album, $year, $albumartist)")
    parser.add_argument("-p", "--preview", action="store_true", help="Only show destination preview, don't actually move files.")
    args = parser.parse_args()

    # Get arguments
    sourceFolder = os.path.abspath(args.sourceFolder)
    destBaseFolder = args.destBaseFolder
    if destBaseFolder is None:
        destBaseFolder = sourceFolder
    else:
        destBaseFolder = os.path.abspath(destBaseFolder)
    preview = args.preview
    destFolderTemplate = args.folderFormat

    # Welcome
    print("MP3sort 1.0")
    print("-----------")

    print("sourceFolder = %s" % sourceFolder)
    print("destBaseFolder = %s" % destBaseFolder)

    # Get list of files, along with their metadata
    metaData = iterate_folder(sourceFolder)

    # Now iterate list, create destination folder structure, move files
    process_list(metaData, destBaseFolder, destFolderTemplate, preview)

    # That's it
    print("Finished.")


if __name__ == "__main__":
    main()