from django.http import QueryDict
import json
from rest_framework import parsers

class MultipartPostParser(parsers.MultiPartParser):

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(
            stream,
            media_type=media_type,
            parser_context=parser_context
        )
        data = {}
        data['petid'] = int(result.data['petid'])
        data['desc'] = result.data['desc']
        # find the data field and parse it
        data = json.loads(json.dumps(data))
        qdict = QueryDict('', mutable=True)
        qdict.update(data)
        print(parsers.DataAndFiles(qdict, result.files).files)
        return parsers.DataAndFiles(qdict, result.files)