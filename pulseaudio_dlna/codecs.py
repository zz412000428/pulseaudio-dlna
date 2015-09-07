#!/usr/bin/python

# This file is part of pulseaudio-dlna.

# pulseaudio-dlna is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pulseaudio-dlna is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pulseaudio-dlna.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import functools
import logging
import re
import inspect
import sys

import pulseaudio_dlna.encoders

logger = logging.getLogger('pulseaudio_dlna.codecs')


def get_codec_by_identifier(identifier):
    for name, _type in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(_type) and issubclass(_type, BaseCodec):
            if _type is not BaseCodec and _type().identifier == identifier:
                return _type
    return None


@functools.total_ordering
class BaseCodec(object):

    ENABLED = False

    def __init__(self):
        self.mime_type = None
        self.suffix = None
        self.identifier = None
        self.priority = None

    @property
    def enabled(self):
        return type(self).ENABLED

    @enabled.setter
    def enabled(self, value):
        type(self).ENABLED = value

    @property
    def specific_mime_type(self):
        return self.mime_type

    def accepts(self, mime_type):
        for accepted_mime_type in self.SUPPORTED_MIME_TYPES:
            if mime_type.lower().startswith(accepted_mime_type.lower()):
                return True
        return False

    def __eq__(self, other):
        return type(self) is type(other)

    def __gt__(self, other):
        return type(self) is type(other)

    def __str__(self, detailed=False):
        return '<{} enabled="{}" priority="{}">{}'.format(
            self.__class__.__name__,
            self.enabled,
            self.priority,
            '\n    ' + str(self.encoder) if detailed else '',
        )


class BitRateMixin(object):
    def __eq__(self, other):
        return type(self) is type(other) and self.bit_rate == other.bit_rate

    def __gt__(self, other):
        return type(self) is type(other) and self.bit_rate > other.bit_rate


@functools.total_ordering
class Mp3Codec(BitRateMixin, BaseCodec):

    SUPPORTED_MIME_TYPES = ['audio/mpeg', 'audio/mp3']

    def __init__(self, mime_string=None):
        BaseCodec.__init__(self)
        self.priority = 18
        self.suffix = 'mp3'
        self.identifier = 'mp3'
        self.mime_type = mime_string or 'audio/mp3'

        self.bit_rate = None

    @property
    def encoder(self):
        return pulseaudio_dlna.encoders.LameEncoder(self.bit_rate)


class WavCodec(BaseCodec):

    SUPPORTED_MIME_TYPES = ['audio/wav', 'audio/x-wav']

    def __init__(self, mime_string=None):
        BaseCodec.__init__(self)
        self.priority = 15
        self.suffix = 'wav'
        self.identifier = 'wav'
        self.mime_type = mime_string or 'audio/wav'

    @property
    def encoder(self):
        return pulseaudio_dlna.encoders.WavEncoder()


class L16Codec(BaseCodec):

    SUPPORTED_MIME_TYPES = ['audio/l16']

    def __init__(self, mime_string=None):
        BaseCodec.__init__(self)
        self.priority = 0
        self.suffix = 'pcm16'
        self.identifier = 'l16'
        self.mime_type = 'audio/L16'

        self.sample_rate = None
        self.channels = None

        if mime_string:
            match = re.match(
                '(.*?)(?P<mime_type>.*?);'
                '(.*?)rate=(?P<sample_rate>.*?);'
                '(.*?)channels=(?P<channels>\d)', mime_string)
            if match:
                self.mime_type = match.group('mime_type')
                self.sample_rate = int(match.group('sample_rate'))
                self.channels = int(match.group('channels'))

    @property
    def specific_mime_type(self):
        if self.sample_rate and self.channels:
            return '{};rate={};channels={}'.format(
                self.mime_type, self.sample_rate, self.channels)
        else:
            return self.mime_type

    @property
    def encoder(self):
        return pulseaudio_dlna.encoders.L16Encoder(
            self.sample_rate, self.channels)

    def __eq__(self, other):
        return type(self) is type(other) and (
            self.sample_rate == other.sample_rate and
            self.channels == other.channels)

    def __gt__(self, other):
        return type(self) is type(other) and (
            self.sample_rate > other.sample_rate and
            self.channels > other.channels)


@functools.total_ordering
class AacCodec(BitRateMixin, BaseCodec):

    SUPPORTED_MIME_TYPES = ['audio/aac', 'audio/x-aac']

    def __init__(self, mime_string=None):
        BaseCodec.__init__(self)
        self.priority = 12
        self.suffix = 'aac'
        self.identifier = 'aac'
        self.mime_type = mime_string or 'audio/aac'

        self.bit_rate = None

    @property
    def encoder(self):
        return pulseaudio_dlna.encoders.AacEncoder(self.bit_rate)


@functools.total_ordering
class OggCodec(BitRateMixin, BaseCodec):

    SUPPORTED_MIME_TYPES = 'audio/ogg', 'audio/x-ogg', 'application/ogg'

    def __init__(self, mime_string=None):
        BaseCodec.__init__(self)
        self.priority = 6
        self.suffix = 'ogg'
        self.identifier = 'ogg'
        self.mime_type = mime_string or 'audio/ogg'

        self.bit_rate = None

    @property
    def encoder(self):
        return pulseaudio_dlna.encoders.OggEncoder(self.bit_rate)


class FlacCodec(BaseCodec):

    SUPPORTED_MIME_TYPES = ['audio/flac', 'audio/x-flac']

    def __init__(self, mime_string=None):
        BaseCodec.__init__(self)
        self.priority = 9
        self.suffix = 'flac'
        self.identifier = 'flac'
        self.mime_type = mime_string or 'audio/flac'

    @property
    def encoder(self):
        return pulseaudio_dlna.encoders.FlacEncoder()


@functools.total_ordering
class OpusCodec(BitRateMixin, BaseCodec):

    SUPPORTED_MIME_TYPES = 'audio/opus', 'audio/x-opus'

    def __init__(self, mime_string=None):
        BaseCodec.__init__(self)
        self.priority = 3
        self.suffix = 'opus'
        self.identifier = 'opus'
        self.mime_type = mime_string or 'audio/opus'

        self.bit_rate = None

    @property
    def encoder(self):
        return pulseaudio_dlna.encoders.OpusEncoder(self.bit_rate)
