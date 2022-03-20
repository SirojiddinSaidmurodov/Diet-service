from pyswip import Prolog

if __name__ == '__main__':
    prolog = Prolog()
    prolog.consult("diet.pl", catcherrors=True)


    def encode(result: dict):
        for key in result.keys():
            if type(result.get(key)) == bytes:
                result[key] = result.get(key).decode('utf-8')


    for solution in prolog.query(
            "dish(X,Y),dishProducts(Y,P), symptoms(\"пищевая зависимость\", D), diet(D,_,A), common_elements(A,P)."):
        encode(solution)
        print("Diet for candida is ", solution["D"], ", dish is ", solution["X"])
