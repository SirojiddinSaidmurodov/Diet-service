from multiprocessing import Pool


def process(data):
    return pool.apply(get_dishes, (data,))


def initialise():
    global prolog
    from pyswip import Prolog
    prolog = Prolog()
    prolog.consult("diet.pl", catcherrors=True)


def encode(result: dict):
    for key in result.keys():
        if type(result.get(key)) == bytes:
            result[key] = result.get(key).decode('utf-8')


def get_dishes(symptom):
    global prolog

    result = []
    for solution in prolog.query(
            "dish(X,Y),dishProducts(Y,P), symptoms({}, Diet), diet(Diet,_,Allowed), common_elements(Allowed,P), pfc(Y,Calories,Proteins,Fats,Carbohydrates), b(Calories, Level, _).".format(
                symptom)):
        encode(solution)
        result.append(solution)

    return result


pool = Pool(None, initialise)

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
