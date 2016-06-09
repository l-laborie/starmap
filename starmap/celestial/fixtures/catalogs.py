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
        Catalog.objects.get_or_create(name=name, abbreviation=abb,
                                      description=desc)

def fixture_catalog_hipparcos():
    catalog, _ = Catalog.objects.get_or_create(
        name='Hipparcos', abbreviation='Hip', description='stars')

    return catalog

def fixture_catalog_henry_draper():
    catalog, _ = Catalog.objects.get_or_create(
        name='Henry Draper', abbreviation='HD', description='stars')

    return catalog

def fixture_catalog_harvard_revised():
    catalog, _ = Catalog.objects.get_or_create(
        name='Harvard Revised', abbreviation='HR', description='stars')

    return catalog

def fixture_catalog_gliese():
    catalog, _ = Catalog.objects.get_or_create(
        name='Gliese', abbreviation='Gl', description='stars')

    return catalog

def fixture_catalog_bayer_flamsteed():
    catalog, _ = Catalog.objects.get_or_create(
        name='Bayer Flamsteed', abbreviation='BF', description='stars')

    return catalog

def fixture_catalog_bayer():
    catalog, _ = Catalog.objects.get_or_create(
        name='Bayer', abbreviation='Bayer', description='stars')

    return catalog

def fixture_catalog_flamsteed():
    catalog, _ = Catalog.objects.get_or_create(
        name='Flamsteed', abbreviation='Flam', description='stars')

    return catalog
