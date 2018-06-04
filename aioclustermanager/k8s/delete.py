from copy import deepcopy

K8S_DELETE = {
    'kind': 'DeleteOptions',
    'propagationPolicy': 'Background'
}


class K8SDelete(object):

    def __init__(self, purge=True):
        self._raw = K8S_DELETE
        if purge:
            self._raw['propagationPolicy'] = 'Foreground'

    def payload(self):
        return deepcopy(self._raw)
