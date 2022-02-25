from pyswip import Prolog

if __name__ == '__main__':
    prolog = Prolog()
    prolog.assertz("member(X, [X | _])")
    prolog.assertz("member(X, [_ | Hv]) :- member(X, Hv)")
    prolog.assertz("common_elements([H | _], L2) :- member(H, L2)")
    prolog.assertz("common_elements([_ | T], L2) :- common_elements(T, L2)")

    prolog.assertz("symptoms(кандида,антикандида)")

    prolog.assertz("diet(антикандида,[говядина,телятина,молоко,рис],[птица,сельд,яйца,бобы,гречка])")

    prolog.assertz("dish(йогурт,[молоко,клубника,закваска])")
    prolog.assertz("dish(\"зразы из индейки\", [птица, лук, соль, яйцо, укроп, \"зеленый салат\", \"сливочное масло\"])")

    for solution in prolog.query("dish(X,Y),symptoms(кандида, D),diet(D,_,A),common_elements(A,Y)."):
        print("Diet for candida is ", solution["D"], ", dish is ", solution["X"])

