class Parameters:
    SUPL_VER_MAJ = 2
    SUPL_VER_MIN = 0
    SUPL_VER_SERVID = 0

    LPP_VER_MAJ = 12
    LPP_VER_TECH = 4
    LPP_VER_EDITOR = 0

    GSM_REF_MCC = 244
    GSM_REF_MNC = 5
    GSM_REF_LAC = 23010
    GSM_REF_CI = 12720

    #FQDN = 'supl.vodafone.com'
    #FQDN = 'supl.google.com'
    FQDN = '127.0.0.1'
    PORT = 7275

    IMSI = bytes.fromhex('FFFF919448458398')

    RRLP_ENABLED = True
    LPP_ENABLED = True