from pyswip import Prolog

prolog = Prolog()
prolog.consult("diet.pl", catcherrors=True)


def encode(result: dict):
    for key in result.keys():
        if type(result.get(key)) == bytes:
            result[key] = result.get(key).decode('utf-8')


def get_dishes(symptom):
    result = []
    for solution in prolog.query(
            "dish(X,Y),dishProducts(Y,P), symptoms({}, Diet), diet(Diet,_,Allowed), common_elements(Allowed,P), pfc(Y,Calories,Proteins,Fats,Carbohydrates).".format(
                symptom)):
        encode(solution)
        result.append(solution)

    return result


if __name__ == '__main__':

    # for solution in prolog.query(
    #         "dish(X,Y),dishProducts(Y,P), symptoms(\"пищевая зависимость\", D), diet(D,_,A), common_elements(A,P)."):
    #     encode(solution)
    #     print("Diet for candida is ", solution["D"], ", dish is ", solution["X"])

    results = get_dishes("кандида")
    for solution in results:
        print("Diet for candida is ", solution["Diet"], ", dish is ", solution["X"], "pfc:", solution["Calories"],
              "p: ",
              solution["Proteins"], "f: ", solution["Fats"], "c: ", solution["Carbohydrates"])
