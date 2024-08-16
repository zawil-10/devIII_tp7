class ValueZero(Exception):
    pass


class Fraction:
    """Classe représentant une fraction et des opérations.

    Cette classe permet des manipulations de fractions à travers plusieurs opérations.
    """

    def __init__(self, num, den):
        """Cela crée une fraction basée sur un numérateur et un dénominateur..

        PRE :   le numérateur et le dénominateur doivent etre des entiers.
        POST :  construit une instance de la classe Fraction possédant un numérateur et un dénominateur.
        RAISES : TypeError si le numérateur ou le dénominateur n'est pas un entier.
                 ValueError si le dénominateur == 0.
        """
        try:
            if not isinstance(num, int) or not isinstance(den, int):
                raise TypeError("Le numérateur et le dénominateur doivent être des entiers.")
            
            if den == 0:
                raise ValueError("Le dénominateur doit être différent de 0.")
            

            self.__numerator = num
            self.__denominator = den

        except ValueZero as e:
            print(f"TypeError: {e}")
            self.__numerator = 0
            self.__denominator = 1

        except TypeError as e:
            print(f"TypeError: {e}")
            self.__numerator = 0
            self.__denominator = 1

    @property
    def get_numerator(self):
        return self.__numerator

    @property
    def get_denominator(self):
        return self.__denominator

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Renvoie une représentation textuelle de la forme réduite de la fraction

        PRE :   la méthode traite une fraction
        POST :  renvoi une chaine de caractère contenant la forme réduite de la fraction
        """
        if self.__denominator == 1:
            return "{}".format(self.__numerator)

        elif self.__numerator == self.__denominator:
            return "1"

        elif self.__numerator == 0:
            return "0"

        elif type(self.__numerator) is float:
            return "{}".format(self.__numerator / self.__denominator)

        else:
            num = self.__numerator
            den = self.__denominator

            produit_facteur = num
            div = den
            while div != 0:
                reste = produit_facteur % div
                produit_facteur = div
                div = reste

            if int(self.__denominator / produit_facteur) == 1:
                return "{}".format(int(self.__numerator / produit_facteur))

            return "{}\n-\n{}".format(int(num / produit_facteur), int(den / produit_facteur))

    def as_mixed_number(self, entier: int):
        """Renvoie une représentation textuelle de la forme réduite de la fraction sous forme de nombre mixte
           Un nombre mixte est la somme d'un entier et d'une fraction propre

        PRE :   le paramètre 'entier' doit etre un entier, la méthode traite une fraction
        POST :  renvoi une chaine de caractère contenant la forme réduite de l'addition des 2 termes
        Raise : renvoi TypeError si le type du parametre != int
        """
        nom = self.__numerator
        den = self.__denominator

        try:
            if type(entier) != int:
                raise ValueError

            else:
                somme_entier = den * entier
                nom = nom + somme_entier

                return Fraction(nom, den)

        except ValueError:
            return "le parametre saisi doit etre un entier"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Surcharge de l'opérateur (+) pour les fractions

         PRE : self et other sont des Fraction.
         POST : Renvoie self + other si self et other sont des fractions, sinon, renvoie -1

         Raise : TypeError si other n'est pas additionnable
         """
        try:
            if type(other) == int:
                return Fraction(
                    (self.get_numerator * 1) + (self.get_denominator * other),
                    (self.get_denominator * 1))

            elif type(other) == Fraction:
                if self.get_denominator == other.get_denominator:
                    return Fraction((self.get_numerator + other.get_numerator), self.get_denominator)

                else:
                    return Fraction(
                        (self.get_numerator * other.get_denominator) + (self.get_denominator * other.get_numerator),
                        (self.get_denominator * other.get_denominator))
            else:
                raise TypeError

        except TypeError:
            return 'type invalide'

    def __sub__(self, other):
        """Surcharge de l'opérateur (-) pour les fractions

        PRE :  le numérateur et le dénominateur doivent etre différents de 0
        POST : renvoi le résultat de l'addition des 2 termes si les préconditions sont respectées.

        Raise : TypeError si other n'est pas soustrayable
        """
        try:
            if type(other) == int:
                return Fraction(
                    (self.get_numerator * 1) - (self.get_denominator * other),
                    (self.get_denominator * 1))

            elif type(other) == Fraction:
                if self.get_denominator == other.get_denominator:
                    return Fraction((self.get_numerator - other.get_numerator), self.get_denominator)

                else:
                    return Fraction(
                        (self.get_numerator * other.get_denominator) - (self.get_denominator * other.get_numerator),
                        (self.get_denominator * other.get_denominator))
            else:
                raise TypeError

        except TypeError:
            return 'type invalide'

    def __mul__(self, other):
        """Surcharge de l'opérateur (*) pour les fractions

        PRE : self et other sont des Fraction.
        POST : Renvoie self * other si self et other sont des fractions, sinon, renvoie -1

        Raise : TypeError si other n'est pas multipliable
        """
        try:
            if type(other) is Fraction:
                num = self.get_numerator * other.get_numerator
                den = self.get_denominator * other.get_denominator

                return Fraction(num, den)

            elif type(other) is int or type(other) is float:
                return Fraction(self.get_numerator * other, self.get_denominator)

            else:
                raise TypeError

        except TypeError:
            return 'type invalide'

    def __truediv__(self, other):
        """Surcharge de l'opérateur (/) pour les fractions

         PRE :  la méthode doit traiter 2 fractions
         POST : renvoi le résultat de la division de 2 fractions

         Raise : TypeError si other n'est pas un diviseur correct
        """
        try:
            if type(other) is Fraction:
                num = self.get_numerator * other.get_denominator
                den = self.get_denominator * other.get_numerator

                return Fraction(num, den)

            elif type(other) is int or type(other) is float:
                return Fraction(self.get_numerator * 1, self.get_denominator * other)

            else:
                raise TypeError

        except TypeError:
            return 'type invalide'

    def __pow__(self, other):
        """Surcharge de l'opérateur (**) pour les fractions

        PRE :   le dénominateur doit etre différent de 0 ainsi que le dénominateur de la puissance
        POST :  renvoi le résultat de la puissance d'une fraction

        Raise : TyperError si other est de type de string
        """
        try:
            if type(other) is Fraction:
                num = self.get_numerator ** (other.get_numerator / other.get_denominator)
                den = self.get_denominator ** (other.get_numerator / other.get_denominator)
                return Fraction(num, den)

            elif type(other) is int or type(other) is float:
                return Fraction(self.__numerator ** other, self.__denominator ** other)
            else:
                raise TypeError

        except TypeError:
            return "Ceci n'est pas un attribut valable"

    def __eq__(self, other):
        """Surcharge de l'opérateur (==) pour les fractions

        PRE :   le dénominateur de chacun des termes doivent etre différents de 0
        POST :  renvoi True ou False si les termes sont égaux ou non

        """
        try:
            if type(other) is Fraction:
                if self.__numerator / self.__denominator == other.get_numerator / other.get_denominator:
                    return True
                else:
                    return False

            elif type(other) is int or type(other) is float:
                if self.__numerator / self.__denominator == other:
                    return True
                else:
                    return False

            else:
                raise TypeError

        except TypeError:
            return "'" + str(other) + "'" + " n'est pas un attribut valable."

    def __float__(self):
        """Renvoie la valeur décimale de la fraction

        PRE :   le dénominateur doit etre différent de 0
        POST :  renvoi la forme décimale de la fraction

        """

        return self.__numerator / self.__denominator

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Vérifier si la valeur d'une fraction est 0

        PRE : le dénominateur doit etre différent de 0
        POST : renvoi True si la valeur de Fraction vaut 0 sinon False
        """
        try:
            if self.__denominator == 0:
                raise ValueZero("le dénominateur doit etre différent de 0")

            elif self.__numerator == 0:
                return True

            else:
                return False

        except ValueZero as e:
            print(e)

    def is_integer(self):
        """Vérifiez si une fraction est un entier (ex : 8/4, 3, 2/2, ...)

        PRE :   /
        POST :  renvoi True si le résultat de la fraction est un entier sinon retourne False
        """
        if self.__numerator % self.__denominator == 0:
            return True

        else:
            return False

    def is_proper(self):
        """Vérifiez si la valeur absolue de la fraction est < 1

        PRE :   le dénominateur doit etre différent de 0
        POST :  renvoi True si la valeur absolue de la fraction est <1 sinon False

        """
        if abs(self.__numerator / self.__denominator) < 1:
            return True
        else:
            return False

    def is_unit(self):
        """Vérifiez si la valeur absolue de la fraction est < 1

        PRE :  -
        POST : Renvoie True si le numérateur de self à sa forme réduite == 1, sinon, False.

        """
        produit_facteur = self.__numerator
        div = self.__denominator
        while div != 0:
            reste = produit_facteur % div
            produit_facteur = div
            div = reste
        if self.__numerator / produit_facteur == 1:
            return True
        else:
            return False

    def is_adjacent_to(self, other):
        """Vérifiez si deux fractions diffèrent d'une fraction unitaire

            Deux fractions sont adjacentes si la valeur absolue de la différence entre elles est une fraction unitaire

        PRE :   les 2 termes comparés doivent etre des fractions
        POST :  renvoi True si la différence des valeurs absolues de chaque termes vaut 1 sinon False
        """
        try:
            if type(other) is Fraction:
                num_1 = self.__numerator
                den_1 = self.__denominator
                num_2 = other.get_numerator
                den_2 = other.get_denominator
                sub = Fraction((num_1 * den_2) - (den_1 * num_2), den_1 * den_2)
                return abs(sub.get_numerator / sub.get_denominator) == 1
            else:
                raise TypeError()
        except TypeError:
            return "'" + str(other) + "'" + " n'est pas un attribut valable."
