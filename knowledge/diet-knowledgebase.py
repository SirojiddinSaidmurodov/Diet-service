from pyswip import Prolog

if __name__ == '__main__':
    prolog = Prolog()
    prolog.assertz("содержит(X,[X|_]).")
    prolog.assertz("содержит(X, [_|Hv]) :- содержит(X,Hv).")

    prolog.assertz("симптомы(кандида,антикандида).")

    prolog.assertz("диета(антикандида,[говядина,телятина,молоко,рис],[птица,сельд,яйца,бобы,гречка]).")

    prolog.assertz("блюдо(йогурт,[молоко,клубника,закваска]).")
    prolog.assertz("блюдо(зразы из индейки, [курица, лук,соль,яйцо,укроп,зеленый салат,сливочное масло]).")
    # list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
    for soln in prolog.query("father(X,Y)"):
        print(soln["X"], "is the father of", soln["Y"])
    # michael is the father of john
    # michael is the father of gina