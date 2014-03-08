class URL:
    """URL manipulation class"""

    def __init__(self, url):
        self._url = url
        self._query_dict = {}

    def get_query_dict(self):
        # Remove fragment if present.
        p = self._url
        if '#' in self._url:
            p = self._url.split("#", 0)

        # Convert query string to dictionary
        if '?' in p:
            bb, qs = p.split("?", 1)
            pairs = [s2 for s1 in qs.split('&') for s2 in s1.split(';')]
            for name_value in pairs:
                name, value = name_value.split('=')
                if name in self._query_dict:
                    self._query_dict[name].append(value)
                else:
                    self._query_dict[name] = [value]

            return self._query_dict

    def update_query_param(self, key, value, strict_mode=False):
        # populate query dict if it is not populated already
        if not self._query_dict:
            self.get_query_dict()

        if not strict_mode:
            self._query_dict[key] = [value]
            return self

        if key in self._query_dict:
            self._query_dict[key] = [value]
            return self
        else:
            raise ValueError("param not present in query parameter" % key)

    def get_query_string(self):
        qs = ''
        for name in self._query_dict.keys():
            for value in self._query_dict[name]:
                qs += name + "=" + value + "&"

        return qs[:-1]