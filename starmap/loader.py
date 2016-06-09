"""Just a script will load file from https://github.com/astronexus/HYG-Database
"""

from starmap.celestial.models import (
    CatalogIdentifier,
    Constellation,
    Star,
)
from starmap.celestial.fixtures.catalogs import (
    fixture_catalog_bayer,
    fixture_catalog_bayer_flamsteed,
    fixture_catalog_flamsteed,
    fixture_catalog_gliese,
    fixture_catalog_harvard_revised,
    fixture_catalog_henry_draper,
    fixture_catalog_hipparcos,
)
from starmap.celestial.fixtures.constellations import fixture_constellation



def load_stars(path):
    fixture_constellation()
    hipparcos = fixture_catalog_hipparcos()
    henry_draper = fixture_catalog_henry_draper()
    harvard = fixture_catalog_harvard_revised()
    gliese = fixture_catalog_gliese()
    bayer_flamsteed = fixture_catalog_bayer_flamsteed()
    bayer_ = fixture_catalog_bayer()
    flamsteed = fixture_catalog_flamsteed()

    multiple_stars = []

    with open(path) as file:
        for line in file.read().splitlines():
            id, hip, hd, hr, gl, bf, proper, ra, dec, dist, pmra, pmdec, rv, \
            mag, absmag, spect, ci, x, y, z, vx, vy, vz, rarad, decrad, \
            pmrarad, pmdecrad, bayer, flam, con, comp, comp_primary, base, \
            lum, var, var_min, var_max = line.split(',')

            if id == 'id':
                continue

            # get ids
            id = int(id)

            # create star object
            star = Star.objects.create(
                # object data
                id=id, proper=proper,
                right_ascension=ra.replace(' ', ':'),
                declination=float(dec),
                right_ascension_radian=float(rarad),
                declination_radian=float(decrad),
                magnitude=mag,
                type='*',

                # star data
                distance=float(dist),
                proper_motion_in_right_ascension=float(pmra),
                proper_motion_in_declination=float(pmdec),
                radial_velocity=float(rv),
                absolute_visual_magnitude=float(absmag),
                spectral_type=spect,
                luminosity=float(lum),
                x=float(x),
                y=float(y),
                z=float(z)
            )

            # find constellation
            if len(con) > 0:
                constellation = Constellation.objects.get(abbreviation=con)
                star.constellation = constellation

            # multiple star
            if len(comp_primary) > 0:
                multiple_stars.append((comp_primary, star))

            # multiple star base
            if len(base) > 0:
                star.base = base
                star.refresh_from_db()

            # variable stars
            if var_max is not None and len(var) > 0:
                star.variable = var
            if var_max is not None and len(var_min) > 0:
                star.magnitude_min = float(var_min)
            if var_max is not None and len(var_max) > 0:
                star.magnitude_max = float(var_max)

            # color index
            if len(ci) > 0:
                star.color_index = float(ci)
                star.refresh_from_db()

            # get hipparcos id
            if len(hip) > 0:
                CatalogIdentifier.objects.create(
                    identifier=hip, object=star, catalog=hipparcos)

            # get henry draper
            if len(hd) > 0:
                CatalogIdentifier.objects.create(
                    identifier=hd, object=star, catalog=henry_draper)

            # get harvard
            if len(hr) > 0:
                CatalogIdentifier.objects.create(
                    identifier=hr, object=star, catalog=harvard)

            # get gliese
            if len(gl) > 0:
                CatalogIdentifier.objects.create(
                    identifier=gl, object=star, catalog=gliese)

            # get bayer flamsteed
            if len(bf) > 0:
                CatalogIdentifier.objects.create(
                    identifier=bf, object=star, catalog=bayer_flamsteed)

            # get bayer
            if len(bayer) > 0:
                CatalogIdentifier.objects.create(
                    identifier=bayer, object=star, catalog=bayer_)

            # get flamsteed
            if len(flam) > 0:
                CatalogIdentifier.objects.create(
                    identifier=flam, object=star, catalog=flamsteed)

    for comp_primary, star in multiple_stars:
        base_star = Star.objects.get(id=int(comp_primary))
        star.primary_companion_star = base_star
        star.refresh_from_db()
        if base_star.type in ('*', '**'):
            base_star.type += '*'
            base_star.refresh_from_db()
