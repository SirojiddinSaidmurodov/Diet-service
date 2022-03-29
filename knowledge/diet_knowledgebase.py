from multiprocessing import Pool


def process(data):
    return pool.apply(get_dishes, (data,))


def initialise():
    global prolog
    from pyswip import Prolog
    prolog = Prolog()
    prolog.consult('/Users/saidmurodov/Projects/Diet-service/knowledge/diet.pl', catcherrors=True)


def encode(result: dict):
    for key in result.keys():
        if type(result.get(key)) == bytes:
            result[key] = result.get(key).decode('utf-8')
        if type(result.get(key)) == list:
            temp = result.get(key)
            r = []
            for t in temp:
                if type(t) == bytes:
                    r.append(t.decode('utf-8'))
                else:
                    r.append(t)
            result[key] = r


def get_dishes(symptom):
    global prolog

    result = []
    for solution in prolog.query(
            "dish(X,Y),dishProducts(Y,P), symptoms({}, Diet), diet(Diet,_,Allowed), common_elements(Allowed,P), pfc(Y,Calories,Proteins,Fats,Carbohydrates), b(Calories, Level, _).".format(
                symptom)):
        encode(solution)
        s = {
            "X": str(solution["X"]),
            "P": str(solution["P"]),
            "Diet": str(solution["Diet"]),
            "Allowed": str(solution["Allowed"]),
            "Calories": str(solution["Calories"]),
            "Proteins": str(solution["Proteins"]),
            "Fats": str(solution["Fats"]),
            "Carbohydrates": str(solution["Carbohydrates"]),
            "Level": str(solution["Level"])
        }
        result.append(s)

    return result


pool = Pool(1, initialise)

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
