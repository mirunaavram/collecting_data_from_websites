# collecting_data_from_websites

Proiectul este reprezentat de un script python care:

 scaneaza https://www.top500.org/ 
 gaseste pe fiecare an primele 3 cele mai puternice sisteme
 realizeaza media pe luna/an 
 afiseaza o figura cu evoluția performantei vs. timp 
 calculeaza progresul mediu realizat pe an

Pasi proiect:

scanarea https://www.top500.org/ , utilizarea metodei find_all cu scopul de a gasi toate link-urile de pe pagina respectiva , memorarea in containers tuturor ul-urilor (unordered list) care au id-ul "squarelist"
cum ‘a’ este tag-ul pentru link din html, cautam fiecare link din lista cu ani din site-ul suport si cream link-ul fiecarei luni, daca este posibila accesarea acelui link ( daca pagina respectiva functioneaza)
daca se poate accesa pagina unei anumite luni, cautam eticheta ‘td’ si obtinem manual valorile Rmax ale primelor 3 sisteme, calculand ,totodata, si media lor atat pe luna (cand contor = 1), cat si pe an ( cand contor = 2)
retinem intr-un array valorile performantei fiecarui an ( axa_performanta )
retine intr-un array fiecare an ( axa_an)
in functie de cele 2 array-uri cream diagrama in python 
calcuam progresiul mediu pe fiecare an si facem media aritmetica a rezultatului obtinut
