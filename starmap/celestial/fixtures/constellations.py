from starmap.celestial.models import Constellation


CONSTELLATION_NAMES = [
    ('Aquila', 'Aql', 'Ptolemee'),  # Aigle
    ('Andromeda', 'And', 'Ptolemee'),
    ('Ara', 'Ara', 'Ptolemee'),  # Autel
    ('Libra', 'Lib', 'Ptolemee'),  # Balance
    ('Cetus', 'Cet', 'Ptolemee'),  # Baleine
    ('Aries', 'Ari', 'Ptolemee'),  # Belier
    ('Pyxis', 'Pyx', 'Lacaille'),  # Bousolle
    ('Bootes', 'Boo', 'Ptolemee'),  # Bouvier
    ('Caelum', 'Cae', 'Lacaille'),  # Burin
    ('Chamaeleon', 'Cha', 'Bayer'),  # Cameleon
    ('Cancer', 'Cnc', 'Ptolemee'),
    ('Capricornus', 'Cap', 'Ptolemee'),
    ('Carina', 'Car', 'Lacaille'),  # Carene
    ('Cassiopeia', 'Cas', 'Ptolemee'),
    ('Centaurus', 'Cen', 'Ptolemee'),
    ('Cepheus', 'Cep', 'Ptolemee'),
    ('Coma Berenices', 'Com', 'Tycho Brahe'),  # Chevelure de Berenice
    ('Canes Venatici', 'CVn', 'Hevelius'),  # Chiens de chasse
    ('Auriga', 'Aur', 'Ptolemee'),  # Cocher
    ('Columba', 'Col', 'Plancius'),
    ('Circinus', 'Cir', 'Lacaille'),  # Compas
    ('Corvus', 'Crv', 'Ptolemee'),  # Corbeau
    ('Crater', 'Crt', 'Ptolemee'),  # Coupe
    ('Corona Australis', 'CrA', 'Ptolemee'),  # Couronne australe
    ('Corona Borealis', 'CrB', 'Ptolemee'),  # Couronne boreale
    ('Crux', 'Cru', 'Plancius'),  # Croix du sud
    ('Cygnus', 'Cyg', 'Ptolemee'),
    ('Delphinus', 'Del', 'Ptolemee'),  # Dauphin
    ('Dorado', 'Dor', 'Bayer'),  # Dorade
    ('Draco', 'Dra', 'Ptolemee'),  # Dragon
    ('Scutum', 'Sct', 'Hevelius'),  # Écu de Sobieski
    ('Eridanus', 'Eri', 'Ptolemee'),
    ('Sagitta', 'Sge', 'Ptolemee'),  # Fleche
    ('Fornax', 'For', 'Lacaille'),  # Fourneau
    ('Gemini', 'Gem', 'Ptolemee'),  # Gemeaux
    ('Camelopardalis', 'Cam', 'Plancius'),  # Girapfe
    ('Canis Major', 'CMa', 'Ptolemee'),  # Grand Chien
    ('Ursa Major', 'UMa', 'Ptolemee'),  # Grande Ourse
    ('Grus', 'Gru', 'Bayer'),  # Grue
    ('Hercules', 'Her', 'Ptolemee'),
    ('Horologium', 'Hor', 'Lacaille'),  # Horloge
    ('Hydra', 'Hya', 'Ptolemee'),
    ('Hydrus', 'Hyi', 'Bayer'),
    ('Indus', 'Ind', 'Bayer'),  # Indien
    ('Lacerta', 'Lac', 'Hevelius'),  # Lezard
    ('Monoceros', 'Mon', 'Plancius'),  # Licorne
    ('Lepus', 'Lep', 'Ptolemee'),  # Lievre
    ('Leo', 'Leo', 'Ptolemee'),  # Lion
    ('Lupus', 'Lup', 'Ptolemee'),  # Loup
    ('Lynx', 'Lyn', 'Hevelius'),
    ('Lyra', 'Lyr', 'Ptolemee'),  # Lyre
    ('Antlia', 'Ant', 'Lacaille'),  # Machine Pneumatique
    ('Microscopium', 'Mic', 'Lacaille'),  # Microscope
    ('Musca', 'Mus', 'Bayer'),  # Mouche
    ('Octans', 'Oct', 'Lacaille'),  # Octant
    ('Apus', 'Aps', 'Bayer'),  # Oiseau de paradis
    ('Ophiuchus', 'Oph', 'Ptolemee'),
    ('Orion', 'Ori', 'Ptolemee'),
    ('Pavo', 'Pav', 'Bayer'),  # Paon
    ('Pegasus', 'Peg', 'Ptolemee'),
    ('pictor', 'Pic', 'Lacaille'),  # Peintre
    ('Perseus', 'Per', 'Ptolemee'),  # Persee
    ('Equuleus', 'Equ', 'Ptolemee'),  # Petit Cheval
    ('Canis Minor', 'CMi', 'Ptolemee'),  # Petit Chien
    ('Leo Minor', 'LMi', 'Hevelius'),  # Petit Lion
    ('Vulpecula', 'Vul', 'Hevelius'),  # Petit Renard
    ('Ursa Minor', 'UMi', 'Ptolemee'),  # Petite Ourse
    ('Phoenix', 'Phe', 'Bayer'),
    ('Piscis Austrinus', 'PsA', 'Ptolemee'),  # Poisson Austral
    ('Volans', 'Vol', 'Bayer'),  # Poisson Volant
    ('Pisces', 'Psc', 'Ptolemee'),  # Poissons
    ('Puppis', 'Pup', 'Lacaille'),  # Poupe
    ('Norma', 'Nor', 'Lacaille'),  # Regle
    ('Reticulum', 'Ret', 'Lacaille'),  # Reticule
    ('Sagittarius', 'Sgr', 'Ptolemee'),
    ('Scorpius', 'Sco', 'Ptolemee'),  # Scorpion
    ('Sculptor', 'Scl', 'Lacaille'),  # Sculpteur
    ('Serpens', 'Ser', 'Ptolemee'),  # Serpent
    ('Sextans', 'Sex', 'Hevelius'),  # Sextant
    ('Mensa', 'Men', 'Lacaille'),  # Table
    ('Taurus', 'Tau', 'Ptolemee'),
    ('Telescopium', 'Tel', 'Lacaille'),  # Telescope
    ('Tucana', 'Tuc', 'Bayer'),  # Toucan
    ('Triangulum', 'Tri', 'Ptolemee'),  # Triangle
    ('Triangulum Australe', 'TrA', 'Bayer'),  # Triangle Austral
    ('Aquarius', 'Aqr', 'Ptolemee'),  # Verseau
    ('Virgo', 'Vir', 'Ptolemee'),  # Vierge
    ('Vela', 'Vel', 'Lacaille'),  # Voiles
]


def fixture_constellation():
    for name, abb, ori in CONSTELLATION_NAMES:
        Constellation.objects.create(name=name, abbreviation=abb, origin=ori)
