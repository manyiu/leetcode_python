from typing import List
import unittest


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        can_cook = {s: True for s in supplies}
        recipe_index = {r: i for i, r in enumerate(recipes)}

        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            
            if r not in recipe_index:
                return False

            can_cook[r] = False

            for nei in ingredients[recipe_index[r]]:
                if not dfs(nei):
                    return False
                
            can_cook[r] = True

            return True

        return [r for r in recipes if dfs(r)]

    # def findAllRecipes(
    #     self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    # ) -> List[str]:
    #     adj_list = {}

    #     can_make = set(supplies)

    #     for recipe, ingredient in zip(recipes, ingredients):
    #         if recipe not in adj_list:
    #             adj_list[recipe] = []

    #         for ing in ingredient:
    #             if ing not in adj_list:
    #                 adj_list[ing] = []
    #             adj_list[recipe].append(ing)

    #     def dfs(node: str, path: set) -> bool:
    #         if node in can_make:
    #             return True

    #         if node in path:
    #             return False

    #         path.add(node)

    #         if len(adj_list[node]) == 0:
    #             return False

    #         for nei in adj_list[node]:
    #             if not dfs(nei, path):
    #                 return False

    #         can_make.add(node)
    #         return True

    #     res = []

    #     for recipe in recipes:
    #         if dfs(recipe, set()):
    #             res.append(recipe)

    #     return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        recipes = ["bread"]
        ingredients = [["yeast", "flour"]]
        supplies = ["yeast", "flour", "corn"]
        output = ["bread"]
        self.assertEqual(
            Solution().findAllRecipes(recipes, ingredients, supplies), output
        )

    def test_2(self):
        recipes = ["bread", "sandwich"]
        ingredients = [["yeast", "flour"], ["bread", "meat"]]
        supplies = ["yeast", "flour", "meat"]
        output = ["bread", "sandwich"]
        self.assertEqual(
            Solution().findAllRecipes(recipes, ingredients, supplies), output
        )

    def test_3(self):
        recipes = ["bread", "sandwich", "burger"]
        ingredients = [
            ["yeast", "flour"],
            ["bread", "meat"],
            ["sandwich", "meat", "bread"],
        ]
        supplies = ["yeast", "flour", "meat"]
        output = ["bread", "sandwich", "burger"]
        self.assertEqual(
            Solution().findAllRecipes(recipes, ingredients, supplies), output
        )
