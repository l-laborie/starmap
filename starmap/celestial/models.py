from django.db.models import (
    Model,
    PositiveIntegerField,
    CharField,
    FloatField,
    ForeignKey,
    ManyToManyField,
)


class Catalog(Model):
    name = CharField(max_length=50, help_text='Name of catalog', unique=True)
    abbreviation = CharField(max_length=5, unique=True,
                             help_text='Abbreviation of catalog')
    description = CharField(max_length=50,
                            help_text='Description of the object cataloged')


class CatalogIdentifier(Model):

    class Meta(object):
        unique_together = ('identifier', 'object', 'catalog')

    identifier = CharField(max_length=50)
    object = ForeignKey('Object')
    catalog = ForeignKey('Catalog')


class Constellation(Model):
    name = CharField(max_length=50, unique=True,
                     help_text='Name of constellation')
    abbreviation = CharField(max_length=3, unique=True,
                             help_text='Abbreviation of constellation')
    origin = CharField(max_length=50, help_text='origin of constellation')


class Object(Model):
    """This class store all astronomical data of a celestia's object.
    """
    OBJECT_TYPE = (
        ('*', 'Single Star'),
        ('**', 'Double Star'),
        ('***', 'Triple Star'),
        ('Ast', 'Asterism'),
        ('Gxy', 'Galaxy'),
        ('GxyCld', 'Bright cloud/knot in a galaxy'),
        ('GC', 'Globular Cluster'),
        ('HIIRgn', 'HII Region'),
        ('Neb', 'Nebula (emission or reflection)'),
        ('NF', 'Not Found'),
        ('OC', 'Open Cluster'),
        ('PN', 'Planetary Nebula'),
        ('SNR', 'Supernova Remnant'),
        ('MWSC', 'Milky Way Star Cloud'),
    )

    right_ascension = FloatField(
        help_text='he star\'s right ascension for epoch and equinox 2000.0.')
    declination = FloatField(help_text='he star\'s declination for epoch and '
                                       'equinox 2000.0.')
    right_ascension_radian = FloatField(
        help_text='he star\'s right ascension for epoch and equinox 2000.0 '
                  'in radians.')
    declination_radian = FloatField(help_text='he star\'s declination for '
                                              'epoch and equinox 2000.0 in '
                                              'radians')
    constellation = ForeignKey('Constellation', related_name='+')
    magnitude = FloatField(help_text='The star\'s apparent visual magnitude.')
    proper = CharField(
        null=True, blank=True, max_length=50,
        help_text='A common name for the star or deep sky object,'
        'such as \"Barnard\'s Star\" or \"Sirius\" for star.'
        'I have taken these names primarily from the Hipparcos '
        'project\'s web site, which lists representative names for the 150 '
        'brightest stars and many of the 150 closest stars. I have added a '
        'few names to this list. Most of the additions are designations from '
        'catalogs mostly now forgotten (e.g., Lalande, Groombridge, '
        'and Gould [\"G.\"]) except for certain nearby stars which are still '
        'best known by these designations.')
    type = CharField(max_length=6, choices=OBJECT_TYPE,
                     help_text='The object\'s type')

    identifiers = ManyToManyField('Catalog', through='CatalogIdentifier',
                                  related_name='+')


class Star(Object):
    """This class store all astronomical data of a star.
    """
    # Coordinate
    distance = FloatField(
        null=True, blank=True,
        help_text='The star\'s distance in parsecs computed from parallax data'
                  ' in Hipparcos.')

    # Motion
    proper_motion_in_right_ascension = FloatField(
        null=True, blank=True, help_text='in milli arc seconds per year.')
    proper_motion_in_declination = FloatField(
        null=True, blank=True, help_text='in milli arc seconds per year.')
    radial_velocity = FloatField(
        null=True, blank=True, help_text='in km/sec')

    # Light information
    absolute_visual_magnitude = FloatField(
        help_text='The star\'s absolute visual magnitude'
                  '(its apparent magnitude from a distance of 10 parsecs).')
    spectral_type = CharField(
        null=True, blank=True, max_length=50,
        help_text='The star\'s spectral type, if known.')
    color_index = FloatField(
        null=True, blank=True, help_text='The star\'s color index (blue '
                                         'magnitude - visual magnitude), '
                                         'if known.')
    luminosity = FloatField(help_text='Star\'s luminosity as a multiple of '
                                      'Solar luminosity.')

    # Multiple system information
    companion_stars = ManyToManyField('Star')
    primary_companion_star = ForeignKey(
        'Star', null=True, blank=True, related_name='+',
        help_text='If Multiple star system, ID of primary star')
    base = CharField(
        null=True, blank=True, max_length=50,
        help_text='Catalog ID or name for this multi-star system. '
                  'Currently only used for Gliese stars.')

    # Variable Stars
    var = CharField(
        null=True, blank=True, max_length=50,
        help_text='Star\'s standard variable star designation, when known')
    var_min = FloatField(
        null=True, blank=True,
        help_text=' Star\'s approximate magnitude range, for variables. '
                  'This value is based on the Hp magnitudes for the range in '
                  'the original Hipparcos catalog, adjusted to the V '
                  'magnitude scale to match the \"mag\" field')
    var_max = FloatField(
        null=True, blank=True,
        help_text=' Star\'s approximate magnitude range, for variables. '
                  'This value is based on the Hp magnitudes for the range in '
                  'the original Hipparcos catalog, adjusted to the V '
                  'magnitude scale to match the \"mag\" field')


class DeepSky(Object):
    """This class store all astronomical data of a deep sky.
    """
    semi_major_axes = FloatField(
        help_text='Semi-major axes of the object, in arcminutes. If r2 is '
                  'undefined, r1 is interpreted as the object\'s radius.')
    semi_minor_axes = FloatField(
        help_text='Semi--minor axes of the object, in arcminutes. If r2 is '
                  'undefined, r1 is interpreted as the object\'s radius.')
    angle = FloatField(
        help_text=' Position angle of the semimajor axis of the object, '
                  'in degrees. Only defined if r1 and r2 are present.')
