# vim: tabstop=4 shiftwidth=4
"""
If a filename contains a timestamp in the form of YYYY-MM-DD-hh-mm,
change the mtime to be the timestamp instead of the one kept by the
filesystem. For example, a valid filename would be
foo-2002-04-01-00-00.txt for April fools day on the year 2002
"""
import os, re, time

__author__ = 'Tim Roberts http://www.probo.com/timr/blog/'
__version__ = '$Id$'

DAYMATCH = re.compile('([0-9]{4})-([0-1][0-9])-([0-3][0-9])-([0-2][0-9])-([0-5][0-9]).txt')

def cb_filestat(args):
    filename = args["filename"]
    stattuple = args["mtime"]
    
    mtime = 0
    mtch = DAYMATCH.match(os.path.basename(filename))
    if mtch:
        try:
            timetuple = time.strptime("-".join(mtch.groups()), "%Y-%m-%d-%H-%M")
            mtime = time.mktime(timetuple)
        except:
            pass

    if mtime: 
        args["mtime"] = tuple(list(stattuple[:8]) + [mtime] + list(stattuple[9:]))

    return args
