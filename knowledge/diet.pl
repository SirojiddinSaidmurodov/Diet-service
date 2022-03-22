member(X, [X | _]).
member(X, [_ | Hv]) :- member(X, Hv).
common_elements([H | _], L2) :- member(H, L2).
common_elements([_ | T], L2) :- common_elements(T, L2).

dishProducts([], []):-!.
dishProducts([[HeadR|_]|Tail], [HeadR|TailR]):-
    dishProducts(Tail, TailR).

pfc([],0,0,0,0).
pfc([[ProductName | _]|Other],Cal,P,F,C):-
    pfc(Other,Cal1,P1,F1,C1),
    product(ProductName,TempCal,TempP,TempF,TempC),
    Cal is TempCal + Cal1,
    P is TempP + P1,
    F is TempF + F1,
    C is TempC + C1.

symptoms(кандида, антикандида).
symptoms("плохое усвоение углеводов", "low fodmap").
symptoms("пищевая зависимость", lchf).

diet(антикандида,[говядина, телятина, молоко, рис], [птица, сельд,яйца,бобы,гречка]).
diet("low fodmap",["манная крупа",хлеб,молоко],[гречка,рис,"молоко без лактозы"]).
diet(lchf,[молоко,шоколад,консервы,чеснок,лук],[сало,птица,немолоко,апельсин,шпинат,корнишоны]).

dish(йогурт,
    [[молоко,1],[клубника,1],[закваска,1]]).
dish("зразы из индейки",
    [[индейка,1], [лук,1], [соль,1], [яйца,1], [укроп,1], ["зеленый салат",1], ["сливочное масло",1]]).
dish("кальмаровый салат",
    [[кальмар,1], [огурцы,1], [соль,1], [яйца,1], [перец,1], [майонез,1]]).
dish("судак с подушкой из шпината",
    [[судак,1],["лимонный сок",1], ["оливковое масло",1],[соль,1], [лук,1], [шпинат,1], ["сливочное масло",1]]).
dish("легкий овощной суп",
[[]])

%      название, энергитичность, белки, жиры, углеводы
product(молоко,     60,	            3,	    3,	    5).
product(клубника,41, 0.8, 0.4,8).
product(индейка,276, 20, 22, 0).
product(лук, 41, 1.4, 0.2, 8).
product(соль, 0.1, 0.1, 0.1, 0.1).
product(яйца, 157, 13, 12, 0.7).
product(укроп, 40, 3, 0.5, 6).
product("зеленый салат", 14, 1, 0.14, 1.8).
product("сливочное масло", 662, 0.5, 72.5, 0.8).
product(кальмар, 122, 21.8, 2.8, 2.0).
product(огурцы, 14, 0.8, 0.1, 2.5).
product(перец, 40, 2, 0.2, 10).
product(майонез, 627, 2, 67, 4).
product(судак, 84, 19.2, 0.7, 0).
product("лимонный сок", 16, 0.9, 0.1, 3.0).
product("оливковое масло", 898, 0, 100, 0).
product(шпинат, 23, 3, 0.4, 4).

%  правила для калорийности
b(X, 'very low', R):- X<30, X1 is ((X-90)/20), pow(X1, 2, X2), R is 2*X2.
b(X, 'low', R):- X>=30, X<70, X1 is ((110-X)/20), pow(X1, 3, X2), R is 1-2*X2.
b(X, 'average', R):- X>=70, X<200, X1 is ((110-X)/20), pow(X1, 4, X2), R is 1-2*X2.
b(X, 'hight', R):- X>=200, X=<400, X1 is ((110-X)/20), pow(X1, 5, X2), R is 1-2*X2.
b(X, 'very hight', R):- X>400,X1 is ((110-X)/20), pow(X1, 6, X2), R is 1-2*X2.
