##########################################################################
# Copyright 2009 Carlos Ribeiro
#
# This file is part of Radio Tray
#
# Radio Tray is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 1 of the License, or
# (at your option) any later version.
#
# Radio Tray is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Radio Tray.  If not, see <http://www.gnu.org/licenses/>.
#
##########################################################################
import urllib2
from lxml import etree
from lxml import objectify
from StringIO import StringIO

class AsxPlaylistDecoder:

    def __init__(self):
        print "ASX-familiy playlist decoder"
        
    def extractStream(self,  url):

        print "Downloading playlist..."

        req = urllib2.Request(url)
        f = urllib2.urlopen(req)
        str = f.read()
        f.close()

        print "Playlist downloaded"
        print "Decoding playlist..."

        parser = etree.XMLParser(recover=True)
        root = etree.parse(StringIO(str),parser)
        result = root.xpath("//ref/@href")

        if (len(result) > 0):
            return result
        else:
            return None