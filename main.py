class Question :
    def __init__(self, question, propositions, reponse) -> None:
        self.question = question
        self.propositions = propositions
        self.reponse = reponse

    def poser(self):
        choix = self.propositions
        bonne_reponse = self.reponse
        print("QUESTION")
        print(" " + self.question)
        for i in range(len(choix)) :
            print(" ", i+1, "-", choix[i])

        print()
        resultat_reponse_correcte = False
        reponse_int = Question.demander_reponse_numerique_utilisateur(1, len(choix))
        if choix[reponse_int-1].lower() == bonne_reponse.lower() :
            print("Bonne reponse")
            resultat_reponse_correcte = True
        else : 
            print("Mauvaise reponse")

        print()
        return resultat_reponse_correcte

    def demander_reponse_numerique_utilisateur(min, max) :
        reponse_str = input("Votre reponse (entre " + str(min) + " et " + str(max) + ") : " )
        try :
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        
        except :
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utilisateur(min, max)


class Questionnaire : 
    def __init__(self, questions) -> None:
        self.questions = questions

    def lancer(self) :
        score = 0
        for question in self.questions :
            if question.poser() :
                score += 1
        print("Score final :", score, "sur", len(self.questions))


Questionnaire(
    (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    Question("Quelle est la capitale de l'Italie' ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liege"), "Bruxelles")

    )
).lancer()