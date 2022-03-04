from pyswip import Prolog

if __name__ == '__main__':
    prolog = Prolog()
    prolog.consult("diet.pl")

    for solution in prolog.query(
            "dish(X,Y),dishProducts(Y,P), symptoms(\"пищевая зависимость\", D), diet(D,_,A), common_elements(A,P)."):
        print("Diet for candida is ", solution["D"], ", dish is ", solution["X"])
