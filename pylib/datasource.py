"""
Ce module est une source de données pour les différents exercices.

Ces données sont hétéroclytes, évidemment, dans un "vrai" projet, elles seraient organisées par
arborescence fonctionnelle.
"""

bbt_s12 = [['The Conjugal Configuration', True, 20],
           ['The Wedding Gift Wormhole', True, 21],
           ['The Procreation Calculation', True, 20],
           ['The Tam Turbulence', True, 19],
           ['The Planetarium Collision', True, 19],
           ['The Imitation Perturbation', True, 19],
           ['The Grant Allocation Derivation', True, 19],
           ['The Consummation Deviation', True, 22],
           ['The Citation Negation', True, 20],
           ['The VCR Illumination', False, 20],
           ['The Paintball Scattering', False, 19],
           ['The Propagation Proposition', False, 20],
           ['The Confirmation Polarization', False, 20],
           ['The Meteorite Manifestation', False, 19],
           ['The Donation Oscillation', False, 21],
           ['The D & D Vortex', False, 20],
           ['The Conference Valuation', False, 19],
           ['The Laureate Accumulation', False, 21],
           ['The Inspiration Deprivation', False, 20],
           ['The Decision Reverberation', False, 19],
           ['The Plagiarism Schism', False, 19],
           ['The Maternal Conclusion', False, 20],
           ['The Change Constant', False, 19],
           ['The Stockholm Syndrome', False, 23]]

def load_season(tv_show=None, season=None):
    """
    Fonction permétant d'accéder à la saison d'une série.

    :param tv_show: la série pour laquelle retourner les épisodes.
    :return: Une liste d'épisodes où un épisode est représenté par une liste
    [titre:str, vu:bool, durée:int].
    """
    return bbt_s12

