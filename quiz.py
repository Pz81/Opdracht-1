print('\n\n\nWelkom bij de Mijn Kennis Quiz 2023')

antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
punten=0
aantal_vragen=10
 
if antwoord.lower()=='ja':

    print('\n\nMooi. Dan gaat de Mijn Kennis Quiz 2023 beginnen!!\nGeef bij iedere vraag antwoord op het geen dat jij denkt.\n\n')

    antwoord=input('Vraag 1: Wat is mijn lievelings eten? ')
    if antwoord.lower()=='Pizza' or antwoord.lower()=='Schnitzel':
        punten += 1
        print('goed!')
    else:
        print('fout!')
 
    antwoord=input('Vraag 2: Wat is mijn favorite hobby? ')
    if antwoord.lower()=='Gamen':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 3: Wat is mijn favorite kleur? ')
    if antwoord.lower()=='Groen':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 4: Op welke sport zit ik? ')
    if antwoord.lower()=='Jiu Jitsu':
        punten += 1
        print('goed')
    else:
        print('fout')
       
        antwoord=input('Vraag 5: Welke 2 games speel ik het meest? ')
    if antwoord.lower()=='Fortnite en Ark':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 6: Waar woon ik? ')
    if antwoord.lower()=='Waddinxveen':
        punten += 1
        print('goed')
    else:
        print('fout')

        antwoord=input('Vraag 7: Wanneer is mijn verjaardag? ')
    if antwoord.lower()=='6 Oktober':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 8: Wat is mijn achternaam? ')
    if antwoord.lower()=='Stegmann':
        punten += 1
        print('goed')
    else:
        print('fout') 

    antwoord=input('Vraag 9: Hoe oud ben ik? ')
    if antwoord.lower()=='18 jaar':
        punten += 1
        print('goed')
    else:
        print('fout') 

    antwoord=input('Vraag 10: Wat doe ik naast jiu jitsu het liefst aan sport? ')
    if antwoord.lower()=='Op wintersport gaan':
        punten += 1
        print('goed')
    else:
        print('fout') 

    


    print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
    cijfer = round(float(10/aantal_vragen*punten), 1)
    print('Je cijfer voor dit project komt daarmee op een voorlopige '+str(cijfer)+'.')
    if punten >= 2: print('Goed bezig!')
    else:           print('Hmmm, kan beter... nog even oefenen chef.\n\n')

elif antwoord.lower()=='nee':
    print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
else:
    print('Dit antwoord ken ik niet!')