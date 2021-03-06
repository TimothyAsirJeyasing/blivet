#
# mdraid.py
# mdraid functions
#
# Copyright (C) 2009-2014  Red Hat, Inc.  All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author(s): Dave Lehman <dlehman@redhat.com>
#

from ..size import Size
from . import raid

import logging
log = logging.getLogger("blivet")

# these defaults were determined empirically
MD_SUPERBLOCK_SIZE = Size("2 MiB")
MD_CHUNK_SIZE = Size("512 KiB")

class MDRaidLevels(raid.RAIDLevels):
    @classmethod
    def isRaidLevel(cls, level):
        return super(MDRaidLevels, cls).isRaidLevel(level) and \
           hasattr(level, 'get_max_spares') and \
           hasattr(level, 'get_space') and \
           hasattr(level, 'get_recommended_stride') and \
           hasattr(level, 'get_size')

RAID_levels = MDRaidLevels(["raid0", "raid1", "raid4", "raid5", "raid6", "raid10", "linear"])
