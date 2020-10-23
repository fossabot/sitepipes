from sitepipes.network.site import Site


class NetworkController(Site):
    """ A collection of sites with an agreed upon set of operations """

    def __init__(self, sites=None):
        super().__init__()
        if sites is None:
            sites = []
        self.sites = sites

    def add_site(self, site):
        self.sites.append(site)

    def remove_site(self, site):
        self.sites = [s for s in self.sites if s.name != site.name]

