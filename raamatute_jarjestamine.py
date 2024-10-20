def raamatute_järjestamine(kõrgused, riiuli_pikkus):
    
    # Sordime raamatute kõrgused kahanevas järjekorras
    kõrgused_sorditud = sorted(kõrgused, reverse=True)

    # Loome tühi riiul, kuhu raamatuid paigutada
    riiul = []

    #Lisame raamatud riiulile ükshaaval, alustades kõrgeimast
    raamatu_arv = len(kõrgused_sorditud)
    jääk_riiulistääk_riiulist = riiuli_pikkus


    while raamatu_arv > 0 and jääk_riiulist >= kõrgused_sorditud[raamatu_arv - 1]:
        # Lisame raamatu riiulile
        raamat = kõrgused_sorditud[raamatu_arv - 1]
        riiul.append(raamat)

        # Vähendame jääki riiulil
        jääk_riiulist -= raamat

        # Liigume järgmise raamatu juurde
        raamatu_arv -= 1

   # Tagastame raamatute järjestuse riiulil
    return riiul

    
#Algoritmis sorteerime raamatute kõrgused kahanevas järjekorras ja seejärel lisame raamatud riiulile ükshaaval, alustades kõrgeimast raamatust ja liikudes allapoole. 
#Algoritmi lõppedes saame raamatute järjestuse riiulil vastavalt nende kõrgusele.