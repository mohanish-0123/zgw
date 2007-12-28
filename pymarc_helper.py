from web.net import htmlquote
from pymarc import MARCReader, marc8_to_unicode

class Serializer:
  """Serializes a PyZ3950.zoom.ResultSet object as a pymarc.MARCReader object"""
  def pymarc_serialize(self):
    result_list = []
    for result in self:
      result_list.append(result.data)
    return MARCReader("".join(result_list))

class Humanizer:
  """Humanizes a pymarc.Field or pymarc.Record object.
  
  Uses the string methods of pymarc to generate MARCBreaker format data.
  Newlines are prettified into line break tags, and then the ANSEL characters
  are encoded into Unicode."""
  def humanize(self):
    h = self.__str__()
    h = htmlquote(h)
    h = h.replace('\n', '<br/>\n')
    return marc8_to_unicode(h)
#