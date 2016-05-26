from starmap.celestial.models import Catalog


CATALOG_NAMES = [
    # Stars catalog
    ('Hip', 'Hipparcos', 'stars'),
    ('HD', 'Henry Draper', 'stars'),
    ('HR', 'Harvard Revised', 'stars'),
    ('Gl', 'Gliese', 'stars'),
    ('BF', 'Bayer / Flamsteed designation', 'stars'),
    ('Bayer', 'Bayer designation', 'stars'),
    ('Flam', 'Flamsteed designation', 'stars'),

    # Deep sky object catalog
    ('M', 'Messier', 'all types'),
    ('NGC', 'New General Catalog', 'all types'),
    ('IC', 'Index Catalog', 'all types'),
    ('C', 'Caldwell', 'bright objects of all types'),
    ('Col', 'Collinder', 'open clusters and associations'),
    ('PK', 'Perek + Kohoutek', 'planetary nebulas'),
    ('PGC', 'Principal Galaxy Catalog', 'galaxies'),
    ('UGC', 'Uppsala Galaxy Catalog', 'galaxies'),
    ('ESO', 'European Southern Observatory', 'galaxies'),
    ('Ter', 'Terzian', 'globular clusters'),
    ('Pal', 'Palomar', 'globular clusters'),
]


def fixture_catalogs():
    for abb, name, desc in CATALOG_NAMES:
        Catalog.objects.create(name=name, abbreviation=abb, description=desc)
