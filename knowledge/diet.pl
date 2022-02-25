member(X, [X | _]).
member(X, [_ | Hv]) :- member(X, Hv).
common_elements([H | _], L2) :- member(H, L2).
common_elements([_ | T], L2) :- common_elements(T, L2).

symptoms(кандида,антикандида).

diet(антикандида,[говядина,телятина,молоко,рис],[птица,сельд,яйца,бобы,гречка]).

dish(йогурт,[молоко,клубника,закваска]).
dish(\"зразы из индейки\", [курица, лук, соль, яйцо, укроп, \"зеленый салат\", \"сливочное масло\"]).


? dish(X,Y) ,symptoms(\"кандида\",D), diet(D,_,A), common_elements(A,Y)