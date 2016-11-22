class Recipe(object):
    p = {
        "Frosting":     [4,-2,0,0,5],
        "Candy":        [0,5,-1,0,8],
        "Butterscotch": [-1,0,5,0,6],
        "Sugar":        [0,0,-2,2,1]
    }

    def __init__(self, frosting, candy, butterscotch, sugar):
        self.cap = self.cost(0, frosting, candy, butterscotch, sugar)
        if self.cap < 0:
            self.cap = 0
        self.dur = self.cost(1, frosting, candy, butterscotch, sugar)
        if self.dur < 0:
            self.dur = 0
        self.flavor = self.cost(2, frosting, candy, butterscotch, sugar)
        if self.flavor < 0:
            self.flavor = 0
        self.texture = self.cost(3, frosting, candy, butterscotch, sugar)
        if self.texture < 0:
            self.texture = 0
        self.calories = self.cost(4, frosting, candy, butterscotch, sugar)
        self.compute_score()

    def cost(self, property_nr, frosting, candy, butterscotch, sugar):
        return Recipe.p["Frosting"][property_nr] * frosting \
                + Recipe.p["Candy"][property_nr] * candy \
                + Recipe.p["Butterscotch"][property_nr] * butterscotch \
                + Recipe.p["Sugar"][property_nr] * sugar \

    def compute_score(self):
        self.score = self.cap * self.dur * self.flavor * self.texture


def main():
    # BRUTE FORCE EVERYTHING
    teaspoons = 100
    max = 0
    # try all recipes
    for i in range(teaspoons):
        for j in range(teaspoons-i):
            for k in range(teaspoons-i-j):
                l = teaspoons - i - j - k
                recipe = Recipe(i, j, k, l)
                if recipe.score > max and recipe.calories == 500:
                    max = recipe.score
    print(max)


if __name__ == "__main__":
    main()
