def tekaski_kal(pretecena,cas,zeljena,starost):
    ex_fac = 1.2
    pace = cas / pretecena
    if pretecena > zeljena:
        cas1 = cas -  (pretecena - zeljena) * ex_fac * pace 
        return cas1
    elif pretecena < zeljena:
        cas1 = cas + (zeljena - pretecena) * ex_fac * pace
        return cas1
